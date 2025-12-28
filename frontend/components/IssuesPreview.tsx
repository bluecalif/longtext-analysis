'use client'

import { useState } from 'react'
import type { IssueCard } from '@/types/api'

interface IssuesPreviewProps {
  issues: IssueCard[]
}

/**
 * Issues 미리보기 컴포넌트
 * 
 * Issue Card 리스트 표시
 * 카드 클릭 시 상세 정보 표시 (증상, 원인, 조치, 검증)
 * 관련 스니펫 링크 표시
 * Timeline Section 연결 표시
 */
export function IssuesPreview({ issues }: IssuesPreviewProps) {
  const [expandedIssues, setExpandedIssues] = useState<Set<string>>(new Set())

  const toggleIssue = (issueId: string) => {
    const newExpanded = new Set(expandedIssues)
    if (newExpanded.has(issueId)) {
      newExpanded.delete(issueId)
    } else {
      newExpanded.add(issueId)
    }
    setExpandedIssues(newExpanded)
  }

  if (issues.length === 0) {
    return (
      <div className="text-center text-gray-400 py-12">
        Issue Cards 데이터가 없습니다. 파일을 업로드하세요.
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {issues.map((card) => {
        const isExpanded = expandedIssues.has(card.issue_id)

        return (
          <div
            key={card.issue_id}
            className="border border-gray-200 rounded-lg overflow-hidden"
          >
            {/* Issue Card 헤더 */}
            <div
              className="p-4 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors"
              onClick={() => toggleIssue(card.issue_id)}
            >
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <h3 className="font-semibold text-gray-900 mb-1">{card.title}</h3>
                  <div className="flex items-center gap-2 mt-1">
                    {card.root_cause && (
                      <span
                        className={`px-2 py-1 text-xs rounded ${
                          card.root_cause.status === 'confirmed'
                            ? 'bg-green-100 text-green-700'
                            : 'bg-yellow-100 text-yellow-700'
                        }`}
                      >
                        {card.root_cause.status === 'confirmed' ? '확인됨' : '가설'}
                      </span>
                    )}
                    {card.section_title && (
                      <span className="px-2 py-1 text-xs bg-blue-100 text-blue-700 rounded">
                        {card.section_title}
                      </span>
                    )}
                  </div>
                </div>
                <svg
                  className={`w-5 h-5 text-gray-400 transition-transform ${
                    isExpanded ? 'transform rotate-180' : ''
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M19 9l-7 7-7-7"
                  />
                </svg>
              </div>
            </div>

            {/* Issue Card 상세 내용 */}
            {isExpanded && (
              <div className="p-4 space-y-4">
                {/* 증상 */}
                {card.symptoms.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">증상</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                      {card.symptoms.map((symptom, idx) => (
                        <li key={idx}>{symptom}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* 원인 */}
                {card.root_cause && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">원인</h4>
                    <div className="p-3 bg-gray-50 rounded border border-gray-200">
                      <div className="text-sm text-gray-700">{card.root_cause.text}</div>
                      <div className="mt-1 text-xs text-gray-500">
                        상태: {card.root_cause.status === 'confirmed' ? '확인됨' : '가설'}
                      </div>
                    </div>
                  </div>
                )}

                {/* 조치 */}
                {card.fix.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">조치</h4>
                    <div className="space-y-2">
                      {card.fix.map((fixItem, idx) => (
                        <div
                          key={idx}
                          className="p-3 bg-blue-50 rounded border border-blue-200"
                        >
                          <div className="text-sm text-gray-700">{fixItem.summary}</div>
                          {fixItem.snippet_refs && fixItem.snippet_refs.length > 0 && (
                            <div className="mt-2 text-xs text-blue-600">
                              스니펫: {fixItem.snippet_refs.join(', ')}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 검증 */}
                {card.validation.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">검증</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                      {card.validation.map((validation, idx) => (
                        <li key={idx}>{validation}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* 관련 스니펫 */}
                {card.snippet_refs.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">관련 스니펫</h4>
                    <div className="flex flex-wrap gap-2">
                      {card.snippet_refs.map((snippetId) => (
                        <span
                          key={snippetId}
                          className="px-2 py-1 text-xs bg-blue-50 text-blue-700 rounded border border-blue-200"
                        >
                          {snippetId}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {/* Timeline Section 연결 */}
                {card.section_id && card.section_title && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">연결된 Timeline Section</h4>
                    <div className="p-2 bg-gray-50 rounded border border-gray-200">
                      <div className="text-sm text-gray-700">{card.section_title}</div>
                      <div className="text-xs text-gray-500 mt-1">Section ID: {card.section_id}</div>
                    </div>
                  </div>
                )}

                {/* 관련 Artifacts */}
                {card.related_artifacts.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">관련 Artifacts</h4>
                    <div className="space-y-1">
                      {card.related_artifacts.map((artifact, idx) => (
                        <div key={idx} className="text-sm text-gray-600">
                          {artifact.path && <span className="font-mono">{artifact.path}</span>}
                          {artifact.kind && <span className="ml-2 text-gray-500">({artifact.kind})</span>}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        )
      })}
    </div>
  )
}

