from typing import List, Dict, Any


class TracingService:
    @staticmethod
    async def get_recent_traces() -> List[Dict[str, Any]]:
        return [
            {
                "trace_id": "tr-8947291847",
                "correlation_id": "req-984729",
                "endpoint": "POST /api/v1/ai/review/contract",
                "method": "POST",
                "status_code": 200,
                "total_duration_ms": 142.5,
                "spans": [
                    {"name": "Auth Middleware", "duration_ms": 2.1},
                    {"name": "Tenant Isolation Check", "duration_ms": 1.2},
                    {"name": "Postgres Query (Contract Fetch)", "duration_ms": 4.5},
                    {"name": "Celery Task Dispatch (AI OCR)", "duration_ms": 14.8},
                    {"name": "RAG Vector Cosine Search", "duration_ms": 118.2}
                ]
            }
        ]
