"""
FastAPI 애플리케이션 진입점

이 모듈은 FastAPI 앱을 초기화하고, CORS 설정, 라우터 등록, 예외 처리를 구성합니다.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict, Any

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="Longtext Analysis API",
    description="Cursor IDE 세션 대화 마크다운 파일을 파싱하여 Timeline, Issue Cards, 코드 스니펫을 생성하는 API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS 설정
# 개발 환경: Next.js 프론트엔드 (localhost:3000) 허용
# 프로덕션 환경에서는 환경 변수로 관리 권장
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js 개발 서버
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 예외 처리 핸들러
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """HTTP 예외 처리"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """일반 예외 처리"""
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal server error: {str(exc)}"},
    )


# Health Check 엔드포인트
# E2E 테스트에서 서버 상태 확인용
@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    서버 상태 확인 엔드포인트

    Returns:
        {"status": "ok"}
    """
    return {"status": "ok"}


# 라우터 등록
# Phase 6에서 실제 라우터 구현 예정
# 현재는 구조만 준비

# TODO: Phase 6에서 구현 예정
# from backend.api.routes import parse, timeline, issues, snippets, export
#
# app.include_router(parse.router)
# app.include_router(timeline.router)
# app.include_router(issues.router)
# app.include_router(snippets.router)
# app.include_router(export.router)


# 루트 엔드포인트
@app.get("/")
async def root() -> Dict[str, Any]:
    """
    루트 엔드포인트

    Returns:
        API 정보 및 사용 가능한 엔드포인트
    """
    return {
        "message": "Longtext Analysis API",
        "version": "0.1.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

