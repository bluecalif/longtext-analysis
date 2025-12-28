'use client'

import { useState, useCallback } from 'react'

interface FileUploadProps {
  onFileSelect: (file: File) => void
  isProcessing?: boolean
  disabled?: boolean
}

/**
 * 파일 업로드 컴포넌트
 * 
 * 드래그&드롭 및 파일 선택 기능 제공
 * 파일 검증 (.md 확장자, 크기 제한)
 */
export function FileUpload({
  onFileSelect,
  isProcessing = false,
  disabled = false,
}: FileUploadProps) {
  const [isDragging, setIsDragging] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // 파일 검증
  const validateFile = (file: File): string | null => {
    // 확장자 검증
    if (!file.name.endsWith('.md')) {
      return '마크다운 파일(.md)만 업로드할 수 있습니다.'
    }

    // 파일 크기 제한 (10MB)
    const MAX_SIZE = 10 * 1024 * 1024
    if (file.size > MAX_SIZE) {
      return `파일 크기는 ${MAX_SIZE / 1024 / 1024}MB를 초과할 수 없습니다. (현재: ${(file.size / 1024 / 1024).toFixed(2)}MB)`
    }

    return null
  }

  const handleFile = useCallback(
    (file: File) => {
      setError(null)

      // 파일 검증
      const validationError = validateFile(file)
      if (validationError) {
        setError(validationError)
        return
      }

      // 파일 선택 콜백 호출
      onFileSelect(file)
    },
    [onFileSelect]
  )

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      handleFile(file)
    }
    // 같은 파일을 다시 선택할 수 있도록 value 초기화
    e.target.value = ''
  }

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault()
    if (!disabled && !isProcessing) {
      setIsDragging(true)
    }
  }

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)

    if (disabled || isProcessing) {
      return
    }

    const file = e.dataTransfer.files[0]
    if (file) {
      handleFile(file)
    }
  }

  return (
    <div>
      <div
        className={`border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-colors ${
          isDragging
            ? 'border-blue-500 bg-blue-50'
            : disabled || isProcessing
            ? 'border-gray-200 bg-gray-50 cursor-not-allowed'
            : 'border-gray-300 hover:border-blue-400'
        }`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept=".md"
          onChange={handleFileInputChange}
          disabled={disabled || isProcessing}
          className="hidden"
          id="file-upload"
        />
        <label
          htmlFor="file-upload"
          className={`cursor-pointer block ${disabled || isProcessing ? 'cursor-not-allowed' : ''}`}
        >
          <div className="text-gray-400 mb-2">
            <svg
              className="mx-auto h-12 w-12"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 48 48"
            >
              <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                strokeWidth={2}
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </div>
          <div className="text-sm text-gray-600">
            {isProcessing
              ? '처리 중...'
              : disabled
              ? '업로드 불가'
              : isDragging
              ? '파일을 놓아주세요'
              : '파일을 드래그하거나 클릭하여 업로드'}
          </div>
          <div className="text-xs text-gray-400 mt-1">.md 파일만 지원</div>
        </label>
      </div>

      {/* 에러 메시지 */}
      {error && (
        <div className="mt-3 p-3 bg-red-50 rounded-lg border border-red-200">
          <div className="text-sm font-medium text-red-900">오류</div>
          <div className="text-xs text-red-700 mt-1">{error}</div>
        </div>
      )}
    </div>
  )
}

