from typing import List, Dict, Any


class JobMonitoringService:
    @staticmethod
    async def get_background_queues() -> List[Dict[str, Any]]:
        return [
            {
                "queue_name": "celery-high-priority",
                "active_workers": 4,
                "queue_depth": 0,
                "completed_24h": 1420,
                "failed_24h": 0,
                "avg_execution_ms": 120.0
            },
            {
                "queue_name": "celery-ocr-processing",
                "active_workers": 8,
                "queue_depth": 1,
                "completed_24h": 480,
                "failed_24h": 0,
                "avg_execution_ms": 1450.0
            }
        ]
