'use client'

import { useState } from 'react'
import { api, ApiError } from '@/lib/api'

/**
 * Phase 8.2 브라우저 확인용 임시 페이지
 *
 * API 클라이언트를 브라우저에서 테스트할 수 있도록 구성
 * - 콘솔에서 `window.api`로 접근 가능
 * - 파일 업로드 테스트 버튼 제공
 */
export default function Home() {
  const [status, setStatus] = useState<string>('Ready')
  const [error, setError] = useState<string | null>(null)

  // window 객체에 api 노출 (브라우저 콘솔에서 테스트용)
  if (typeof window !== 'undefined') {
    ;(window as any).api = api
    ;(window as any).ApiError = ApiError
  }

  const handleFileSelect = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setStatus('Uploading...')
    setError(null)

    try {
      const result = await api.parseFile(file)
      setStatus(`Success! Session ID: ${result.session_meta.session_id}`)
      console.log('Parse result:', result)
    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API Error (${err.statusCode}): ${err.detail || err.message}`)
      } else {
        setError(`Error: ${err instanceof Error ? err.message : String(err)}`)
      }
      setStatus('Failed')
      console.error('Parse error:', err)
    }
  }

  return (
    <div className="min-h-screen p-8 bg-gray-50">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Longtext Analysis - API Client Test</h1>

        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4">Phase 8.2: API Client Browser Test</h2>

          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">
              Test File Upload (Markdown file)
            </label>
            <input
              type="file"
              accept=".md"
              onChange={handleFileSelect}
              className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>

          <div className="mb-4">
            <div className="text-sm font-medium mb-1">Status:</div>
            <div className={`p-2 rounded ${status === 'Ready' ? 'bg-gray-100' : status.includes('Success') ? 'bg-green-100' : status === 'Failed' ? 'bg-red-100' : 'bg-yellow-100'}`}>
              {status}
            </div>
          </div>

          {error && (
            <div className="mb-4">
              <div className="text-sm font-medium mb-1 text-red-600">Error:</div>
              <div className="p-2 rounded bg-red-50 text-red-700 text-sm">
                {error}
              </div>
            </div>
          )}

          <div className="mt-6 p-4 bg-blue-50 rounded">
            <h3 className="font-semibold mb-2">Browser Console Test:</h3>
            <p className="text-sm text-gray-700 mb-2">
              Open browser console (F12) and try:
            </p>
            <code className="block text-xs bg-white p-2 rounded mb-2">
              window.api.parseFile(file)
            </code>
            <code className="block text-xs bg-white p-2 rounded">
              // Check Network tab for use_llm query parameter (snake_case)
            </code>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold mb-4">API Client Functions Available:</h2>
          <ul className="list-disc list-inside space-y-1 text-sm">
            <li><code>api.parseFile(file, use_llm?)</code></li>
            <li><code>api.createTimeline(request, use_llm?)</code></li>
            <li><code>api.createIssues(request, use_llm?)</code></li>
            <li><code>api.processSnippets(request)</code></li>
            <li><code>api.getSnippet(snippetId)</code></li>
            <li><code>api.exportTimeline(request)</code></li>
            <li><code>api.exportIssues(request)</code></li>
            <li><code>api.exportAll(request)</code></li>
          </ul>
        </div>
      </div>
    </div>
  )
}
