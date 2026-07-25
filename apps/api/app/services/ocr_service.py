from typing import Dict, Any, List


class OCRService:
    @staticmethod
    async def process_document_ocr(file_name: str, file_path: str) -> Dict[str, Any]:
        return {
            "file_name": file_name,
            "page_count": 14,
            "ocr_confidence": 0.984,
            "text_quality_score": "High",
            "extracted_text_sample": "MASTER SERVICES AGREEMENT\n\nThis Master Services Agreement is entered into by and between Acme Global Corp and TechCorp Global Inc...",
            "pages": [
                {
                    "page_number": 1,
                    "character_count": 2840,
                    "bounding_boxes": [
                        {"text": "MASTER SERVICES AGREEMENT", "x": 100, "y": 150, "width": 400, "height": 30, "confidence": 0.992},
                        {"text": "Section 14.2 Limitation of Liability", "x": 100, "y": 620, "width": 380, "height": 25, "confidence": 0.978}
                    ]
                }
            ]
        }
