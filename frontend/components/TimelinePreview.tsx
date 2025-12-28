'use client'

import { useState } from 'react'
import type { TimelineSection, Event } from '@/types/api'

interface TimelinePreviewProps {
  sections: TimelineSection[]
  events: Event[]
}

/**
 * Timeline 미리보기 컴포넌트
 *
 * Timeline Section 리스트 표시
 * 각 Section의 이벤트 표시
 * 이슈 연결 표시 (has_issues, issue_refs)
 * 작업 결과 연결 정보 표시 (코드 스니펫, 파일, Artifact)
 */
export function TimelinePreview({ sections, events }: TimelinePreviewProps) {
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set())

  const toggleSection = (sectionId: string) => {
    const newExpanded = new Set(expandedSections)
    if (newExpanded.has(sectionId)) {
      newExpanded.delete(sectionId)
    } else {
      newExpanded.add(sectionId)
    }
    setExpandedSections(newExpanded)
  }

  // Event seq로 Event 객체 찾기
  const getEventBySeq = (seq: number): Event | undefined => {
    return events.find((e) => e.seq === seq)
  }

  if (sections.length === 0) {
    return (
      <div className="text-center text-gray-400 py-12">
        Timeline 데이터가 없습니다. 파일을 업로드하세요.
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {sections.map((section) => {
        const isExpanded = expandedSections.has(section.section_id)
        const sectionEvents = section.events
          .map((seq) => getEventBySeq(seq))
          .filter((e): e is Event => e !== undefined)

        return (
          <div
            key={section.section_id}
            className="border border-gray-200 rounded-lg overflow-hidden"
          >
            {/* Section 헤더 */}
            <div
              className="p-4 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors"
              onClick={() => toggleSection(section.section_id)}
            >
              <div className="flex items-center justify-between">
                <div className="flex-1">
                  <h3 className="font-semibold text-gray-900 mb-1">{section.title}</h3>
                  <p className="text-sm text-gray-600">{section.summary}</p>
                </div>
                <div className="ml-4 flex items-center gap-2">
                  {section.has_issues && (
                    <span className="px-2 py-1 text-xs bg-red-100 text-red-700 rounded">
                      이슈 {section.issue_refs.length}개
                    </span>
                  )}
                  <span className="px-2 py-1 text-xs bg-blue-100 text-blue-700 rounded">
                    이벤트 {sectionEvents.length}개
                  </span>
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
            </div>

            {/* Section 상세 내용 */}
            {isExpanded && (
              <div className="p-4 space-y-4">
                {/* Phase/Subphase 정보 */}
                {(section.phase !== undefined || section.subphase !== undefined) && (
                  <div className="text-sm text-gray-600">
                    Phase: {section.phase !== undefined ? section.phase : 'N/A'}
                    {section.subphase !== undefined && `-${section.subphase}`}
                  </div>
                )}

                {/* 이벤트 리스트 */}
                <div>
                  <h4 className="text-sm font-medium text-gray-700 mb-2">이벤트</h4>
                  <div className="space-y-2">
                    {sectionEvents.map((event) => (
                      <div
                        key={event.seq}
                        className="p-3 bg-gray-50 rounded border border-gray-200"
                      >
                        <div className="flex items-start justify-between mb-1">
                          <span className="text-xs font-medium text-gray-500">
                            #{event.seq} - {event.type}
                          </span>
                        </div>
                        <p className="text-sm text-gray-700">{event.summary}</p>
                        {event.snippet_refs.length > 0 && (
                          <div className="mt-2 text-xs text-blue-600">
                            스니펫: {event.snippet_refs.join(', ')}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

                {/* 작업 결과 연결 정보 */}
                {section.detailed_results && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">작업 결과</h4>
                    <div className="space-y-2">
                      {section.detailed_results.code_snippets &&
                        section.detailed_results.code_snippets.length > 0 && (
                          <div className="text-xs text-gray-600">
                            코드 스니펫: {section.detailed_results.code_snippets.length}개
                          </div>
                        )}
                      {section.detailed_results.files &&
                        section.detailed_results.files.length > 0 && (
                          <div className="text-xs text-gray-600">
                            파일: {section.detailed_results.files.join(', ')}
                          </div>
                        )}
                      {section.detailed_results.artifacts &&
                        section.detailed_results.artifacts.length > 0 && (
                          <div className="text-xs text-gray-600">
                            Artifacts: {section.detailed_results.artifacts.length}개
                          </div>
                        )}
                    </div>
                  </div>
                )}

                {/* 이슈 연결 */}
                {section.has_issues && section.issue_refs.length > 0 && (
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">연결된 이슈</h4>
                    <div className="flex flex-wrap gap-2">
                      {section.issue_refs.map((issueId) => (
                        <span
                          key={issueId}
                          className="px-2 py-1 text-xs bg-red-50 text-red-700 rounded border border-red-200"
                        >
                          {issueId}
                        </span>
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

