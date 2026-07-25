from typing import Any, Dict, Optional
from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.core.logging import logger


class LegalDeskException(Exception):
    def __init__(
        self,
        message: str,
        code: str = "INTERNAL_ERROR",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class NotFoundException(LegalDeskException):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            message=f"{resource} with identifier '{identifier}' not found.",
            code="NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )


class UnauthorizedException(LegalDeskException):
    def __init__(self, message: str = "Invalid authentication credentials"):
        super().__init__(
            message=message,
            code="UNAUTHORIZED",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class PermissionDeniedException(LegalDeskException):
    def __init__(self, permission: str):
        super().__init__(
            message=f"Permission '{permission}' is required to perform this action.",
            code="PERMISSION_DENIED",
            status_code=status.HTTP_403_FORBIDDEN
        )


class ValidationException(LegalDeskException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            message=message,
            code="VALIDATION_ERROR",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            details=details
        )


async def legaldesk_exception_handler(request: Request, exc: LegalDeskException) -> JSONResponse:
    request_id = getattr(request.state, "request_id", "unknown")
    logger.error(
        "domain_exception_occurred",
        path=request.url.path,
        code=exc.code,
        message=exc.message,
        request_id=request_id
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
                "request_id": request_id,
            }
        }
    )
