'use client'

import { useState } from 'react'
import { api } from '@/lib/api'
import type { Snippet } from '@/types/api'

interface SnippetsPreviewProps {
  snippets: Snippet[]
}

/**
 * Snippets 미리보기 컴포넌트
 * 
 * 언어별 필터 (sql/ts/py 등)
 * 스니펫 목록 표시 (snippet_id, 언어, 코드 일부)
 * 코드 접기/펼치기 기능
 * 스니펫 상세 조회 (API 호출)
 */
export function SnippetsPreview({ snippets }: SnippetsPreviewProps) {
  const [expandedSnippets, setExpandedSnippets] = useState<Set<string>>(new Set())
  const [selectedLang, setSelectedLang] = useState<string>('all')
  const [loadingSnippets, setLoadingSnippets] = useState<Set<string>>(new Set())
  const [fullCodeCache, setFullCodeCache] = useState<Map<string, string>>(new Map())

  // 사용 가능한 언어 목록 추출
  const languages = Array.from(new Set(snippets.map((s) => s.lang))).sort()

  // 필터링된 스니펫
  const filteredSnippets =
    selectedLang === 'all'
      ? snippets
      : snippets.filter((s) => s.lang === selectedLang)

  const toggleSnippet = (snippetId: string) => {
    const newExpanded = new Set(expandedSnippets)
    if (newExpanded.has(snippetId)) {
      newExpanded.delete(snippetId)
    } else {
      newExpanded.add(snippetId)
      // 확장 시 전체 코드 로드 (캐시에 없으면)
      if (!fullCodeCache.has(snippetId)) {
        loadFullCode(snippetId)
      }
    }
    setExpandedSnippets(newExpanded)
  }

  const loadFullCode = async (snippetId: string) => {
    if (loadingSnippets.has(snippetId) || fullCodeCache.has(snippetId)) {
      return
    }

    setLoadingSnippets((prev) => new Set(prev).add(snippetId))

    try {
      const response = await api.getSnippet(snippetId)
      setFullCodeCache((prev) => new Map(prev).set(snippetId, response.snippet.code))
    } catch (error) {
      console.error(`Failed to load snippet ${snippetId}:`, error)
    } finally {
      setLoadingSnippets((prev) => {
        const newSet = new Set(prev)
        newSet.delete(snippetId)
        return newSet
      })
    }
  }

  if (snippets.length === 0) {
    return (
      <div className="text-center text-gray-400 py-12">
        Snippets 데이터가 없습니다. 파일을 업로드하세요.
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {/* 언어 필터 */}
      <div className="flex items-center gap-2 flex-wrap">
        <span className="text-sm font-medium text-gray-700">언어 필터:</span>
        <button
          onClick={() => setSelectedLang('all')}
          className={`px-3 py-1 text-xs rounded transition-colors ${
            selectedLang === 'all'
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          }`}
        >
          전체 ({snippets.length})
        </button>
        {languages.map((lang) => {
          const count = snippets.filter((s) => s.lang === lang).length
          return (
            <button
              key={lang}
              onClick={() => setSelectedLang(lang)}
              className={`px-3 py-1 text-xs rounded transition-colors ${
                selectedLang === lang
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {lang || 'unknown'} ({count})
            </button>
          )
        })}
      </div>

      {/* 스니펫 리스트 */}
      <div className="space-y-3">
        {filteredSnippets.map((snippet) => {
          const isExpanded = expandedSnippets.has(snippet.snippet_id)
          const isLoading = loadingSnippets.has(snippet.snippet_id)
          const fullCode = fullCodeCache.get(snippet.snippet_id) || snippet.code

          return (
            <div
              key={snippet.snippet_id}
              className="border border-gray-200 rounded-lg overflow-hidden"
            >
              {/* 스니펫 헤더 */}
              <div
                className="p-3 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors"
                onClick={() => toggleSnippet(snippet.snippet_id)}
              >
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-mono text-gray-700">
                        {snippet.snippet_id}
                      </span>
                      <span className="px-2 py-0.5 text-xs bg-gray-200 text-gray-700 rounded">
                        {snippet.lang || 'unknown'}
                      </span>
                      {snippet.links.issue_id && (
                        <span className="px-2 py-0.5 text-xs bg-red-100 text-red-700 rounded">
                          Issue: {snippet.links.issue_id}
                        </span>
                      )}
                    </div>
                    <div className="mt-1 text-xs text-gray-500">
                      {snippet.code.length} characters
                      {snippet.aliases.length > 0 && ` • ${snippet.aliases.length} aliases`}
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

              {/* 스니펫 코드 */}
              {isExpanded && (
                <div className="p-4 bg-gray-900">
                  {isLoading ? (
                    <div className="text-sm text-gray-400">코드 로딩 중...</div>
                  ) : (
                    <pre className="text-xs text-gray-100 overflow-x-auto">
                      <code>{fullCode}</code>
                    </pre>
                  )}
                </div>
              )}

              {/* 축약된 코드 미리보기 (축소 시) */}
              {!isExpanded && (
                <div className="p-3 bg-gray-900">
                  <pre className="text-xs text-gray-400 overflow-x-auto">
                    <code>{snippet.code.substring(0, 200)}...</code>
                  </pre>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}

