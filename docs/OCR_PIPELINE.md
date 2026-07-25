# LegalDesk AI — Enterprise OCR Pipeline Specification

## 1. Overview

The **Enterprise OCR Pipeline** processes scanned contracts, image-based PDFs, and multi-format documents — extracting raw text, calculating page-level confidence scores, and preserving page coordinates (bounding boxes).

---

## 2. OCR Execution & Page Mapping

- **Multi-Format Ingestion**: PDF, DOCX, DOC, TXT, RTF, HTML, TIFF, PNG, JPEG.
- **Bounding Box Mapping**: `[x, y, width, height]` coordinates mapped to raw text snippets.
- **OCR Quality Score**: High confidence thresholding (>0.95 confidence).
