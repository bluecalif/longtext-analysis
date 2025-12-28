"""
API Contract 검증 스크립트

백엔드 Pydantic 모델과 프론트엔드 TypeScript 타입이 일치하는지 검증합니다.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent
BACKEND_MODELS = PROJECT_ROOT / "backend" / "core" / "models.py"
FRONTEND_TYPES = PROJECT_ROOT / "frontend" / "types" / "api.ts"


def extract_backend_enums() -> Dict[str, List[str]]:
    """백엔드 Enum 정의 추출"""
    enums = {}
    
    with open(BACKEND_MODELS, "r", encoding="utf-8") as f:
        content = f.read()
    
    # EventType Enum 추출
    if "class EventType(str, Enum):" in content:
        event_type_start = content.find("class EventType(str, Enum):")
        event_type_end = content.find("\n\n", event_type_start)
        if event_type_end == -1:
            event_type_end = len(content)
        
        event_type_section = content[event_type_start:event_type_end]
        event_types = []
        for line in event_type_section.split("\n"):
            if "=" in line and '"' in line:
                # STATUS_REVIEW = "status_review" 형식
                parts = line.strip().split("=")
                if len(parts) == 2:
                    value = parts[1].strip().strip('"').strip("'")
                    event_types.append(value)
        enums["EventType"] = sorted(event_types)
    
    # ArtifactAction Enum 추출
    if "class ArtifactAction(str, Enum):" in content:
        artifact_action_start = content.find("class ArtifactAction(str, Enum):")
        artifact_action_end = content.find("\n\n", artifact_action_start)
        if artifact_action_end == -1:
            artifact_action_end = len(content)
        
        artifact_action_section = content[artifact_action_start:artifact_action_end]
        artifact_actions = []
        for line in artifact_action_section.split("\n"):
            if "=" in line and '"' in line:
                parts = line.strip().split("=")
                if len(parts) == 2:
                    value = parts[1].strip().strip('"').strip("'")
                    artifact_actions.append(value)
        enums["ArtifactAction"] = sorted(artifact_actions)
    
    # ExportFormat Enum 추출
    if "class ExportFormat(str, Enum):" in content:
        export_format_start = content.find("class ExportFormat(str, Enum):")
        export_format_end = content.find("\n\n", export_format_start)
        if export_format_end == -1:
            export_format_end = len(content)
        
        export_format_section = content[export_format_start:export_format_end]
        export_formats = []
        for line in export_format_section.split("\n"):
            if "=" in line and '"' in line:
                parts = line.strip().split("=")
                if len(parts) == 2:
                    value = parts[1].strip().strip('"').strip("'")
                    export_formats.append(value)
        enums["ExportFormat"] = sorted(export_formats)
    
    # IssueStatus Enum 추출
    if "class IssueStatus(str, Enum):" in content:
        issue_status_start = content.find("class IssueStatus(str, Enum):")
        issue_status_end = content.find("\n\n", issue_status_start)
        if issue_status_end == -1:
            issue_status_end = len(content)
        
        issue_status_section = content[issue_status_start:issue_status_end]
        issue_statuses = []
        for line in issue_status_section.split("\n"):
            if "=" in line and '"' in line:
                parts = line.strip().split("=")
                if len(parts) == 2:
                    value = parts[1].strip().strip('"').strip("'")
                    issue_statuses.append(value)
        enums["IssueStatus"] = sorted(issue_statuses)
    
    return enums


def extract_frontend_enums() -> Dict[str, List[str]]:
    """프론트엔드 Enum 타입 정의 추출"""
    enums = {}
    
    with open(FRONTEND_TYPES, "r", encoding="utf-8") as f:
        content = f.read()
    
    # EventType 추출
    if "export type EventType" in content:
        event_type_start = content.find("export type EventType")
        event_type_end = content.find(";", event_type_start)
        if event_type_end != -1:
            event_type_section = content[event_type_start:event_type_end]
            event_types = []
            for line in event_type_section.split("\n"):
                if "|" in line and "'" in line:
                    # | 'status_review' 형식
                    value = line.strip().strip("|").strip().strip("'").strip('"')
                    if value:
                        event_types.append(value)
            enums["EventType"] = sorted(event_types)
    
    # ArtifactAction 추출
    if "export type ArtifactAction" in content:
        artifact_action_start = content.find("export type ArtifactAction")
        artifact_action_end = content.find(";", artifact_action_start)
        if artifact_action_end != -1:
            artifact_action_section = content[artifact_action_start:artifact_action_end]
            artifact_actions = []
            for line in artifact_action_section.split("\n"):
                if "|" in line and "'" in line:
                    value = line.strip().strip("|").strip().strip("'").strip('"')
                    if value:
                        artifact_actions.append(value)
            enums["ArtifactAction"] = sorted(artifact_actions)
    
    # ExportFormat 추출
    if "export type ExportFormat" in content:
        export_format_start = content.find("export type ExportFormat")
        export_format_end = content.find(";", export_format_start)
        if export_format_end != -1:
            export_format_section = content[export_format_start:export_format_end]
            export_formats = []
            for line in export_format_section.split("\n"):
                if "|" in line and "'" in line:
                    value = line.strip().strip("|").strip().strip("'").strip('"')
                    if value:
                        export_formats.append(value)
            enums["ExportFormat"] = sorted(export_formats)
    
    # IssueStatus 추출
    if "export type IssueStatus" in content:
        issue_status_start = content.find("export type IssueStatus")
        issue_status_end = content.find(";", issue_status_start)
        if issue_status_end != -1:
            issue_status_section = content[issue_status_start:issue_status_end]
            issue_statuses = []
            for line in issue_status_section.split("\n"):
                if "|" in line and "'" in line:
                    value = line.strip().strip("|").strip().strip("'").strip('"')
                    if value:
                        issue_statuses.append(value)
            enums["IssueStatus"] = sorted(issue_statuses)
    
    return enums


def verify_enums() -> tuple[bool, List[str]]:
    """Enum 값 일치 확인"""
    backend_enums = extract_backend_enums()
    frontend_enums = extract_frontend_enums()
    
    errors = []
    all_match = True
    
    for enum_name in backend_enums:
        if enum_name not in frontend_enums:
            errors.append(f"[FAIL] {enum_name}: 프론트엔드에 정의되지 않음")
            all_match = False
            continue
        
        backend_values = set(backend_enums[enum_name])
        frontend_values = set(frontend_enums[enum_name])
        
        if backend_values != frontend_values:
            missing_in_frontend = backend_values - frontend_values
            extra_in_frontend = frontend_values - backend_values
            
            if missing_in_frontend:
                errors.append(
                    f"[FAIL] {enum_name}: 프론트엔드에 누락된 값: {missing_in_frontend}"
                )
            if extra_in_frontend:
                errors.append(
                    f"[FAIL] {enum_name}: 프론트엔드에 추가된 값: {extra_in_frontend}"
                )
            all_match = False
        else:
            errors.append(f"[PASS] {enum_name}: 일치 ({len(backend_values)}개 값)")
    
    return all_match, errors


def main():
    """메인 함수"""
    print("=" * 60)
    print("API Contract 검증")
    print("=" * 60)
    print()
    
    # Enum 검증
    print("1. Enum 값 일치 확인")
    print("-" * 60)
    all_match, errors = verify_enums()
    for error in errors:
        print(error)
    print()
    
    # TypeScript 컴파일 확인
    print("2. TypeScript 컴파일 확인")
    print("-" * 60)
    import subprocess
    result = subprocess.run(
        ["npx", "tsc", "--noEmit"],
        cwd=PROJECT_ROOT / "frontend",
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("[PASS] TypeScript 컴파일 성공 (타입 오류 없음)")
    else:
        print("[FAIL] TypeScript 컴파일 실패:")
        print(result.stdout)
        print(result.stderr)
    print()
    
    # 최종 결과
    print("=" * 60)
    if all_match and result.returncode == 0:
        print("[PASS] API Contract 검증 통과")
        sys.exit(0)
    else:
        print("[FAIL] API Contract 검증 실패")
        sys.exit(1)


if __name__ == "__main__":
    main()

