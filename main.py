from modules.scanner import scan_documents
from modules.extractor import extract_text
from modules.classifier import classify_document
from modules.report_generator import generate_report
from modules.cache_manager import load_cache, save_cache
from modules.logger import logger

# Application Started
logger.info("Application Started")

# Scan all documents
documents = scan_documents()

logger.info("Scanning input_documents folder completed")

results = []

for doc in documents:

    print("=" * 50)
    print("File :", doc["File Name"])

    logger.info(f"Processing file: {doc['File Name']}")

    if doc["Status"] == "Supported":

        logger.info(f"Extracting text from {doc['File Name']}")

        # Check Cache
        text = load_cache(doc["File Path"])

        if text is None:

            logger.info("Cache Miss")

            text = extract_text(doc["File Path"])

            save_cache(doc["File Path"], text)

        else:

            logger.info("Cache Hit")

        logger.info(f"Text extracted successfully from {doc['File Name']}")

        # Machine Learning Classification
        category, confidence = classify_document(text)

        logger.info(
            f"{doc['File Name']} classified as {category} with confidence {confidence:.2f}%"
        )

        # Low confidence warning
        if confidence < 40:
            logger.warning(
                f"Low confidence ({confidence:.2f}%) for {doc['File Name']}"
            )

        print("Status :", doc["Status"])
        print("Category :", category)
        print("Confidence :", confidence, "%")

    else:

        category = "Unsupported"
        confidence = 0

        logger.warning(
            f"Unsupported file skipped: {doc['File Name']}"
        )

        print("Status :", doc["Status"])
        print("Unsupported File")

    results.append({

        "File Name": doc["File Name"],
        "File Type": doc["Extension"],
        "Category": category,
        "Confidence": confidence,
        "Status": doc["Status"]

    })

print("\nRESULTS:")

for item in results:
    print(item)

# Generate CSV
generate_report(results)

logger.info("CSV Report Generated Successfully")
logger.info("Document Analysis Completed Successfully")

print("\nCSV Report Generated Successfully!")
print("Saved in : output/classification_results.csv")