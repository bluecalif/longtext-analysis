'use client'

import { useState } from 'react'
import type { SessionMeta } from '@/types/api'

interface SessionMetaPreviewProps {
  sessionMeta: SessionMeta | null
  onMetaUpdate?: (meta: Partial<SessionMeta>) => void
}

/**
 * 세션 메타 정보 표시 컴포넌트
 * 
 * Session Meta 정보를 표시하고, Phase/Subphase를 수동으로 입력할 수 있는 기능 제공
 */
export function SessionMetaPreview({
  sessionMeta,
  onMetaUpdate,
}: SessionMetaPreviewProps) {
  const [isEditing, setIsEditing] = useState(false)
  const [editedPhase, setEditedPhase] = useState<string>('')
  const [editedSubphase, setEditedSubphase] = useState<string>('')

  if (!sessionMeta) {
    return (
      <div className="p-3 bg-gray-50 rounded-lg">
        <div className="text-sm text-gray-400 text-center">
          파일을 업로드한 후<br />세션 정보가 표시됩니다.
        </div>
      </div>
    )
  }

  const handleSave = () => {
    if (onMetaUpdate) {
      const updates: Partial<SessionMeta> = {}
      if (editedPhase !== '') {
        const phaseNum = parseInt(editedPhase, 10)
        if (!isNaN(phaseNum)) {
          updates.phase = phaseNum
        }
      }
      if (editedSubphase !== '') {
        const subphaseNum = parseInt(editedSubphase, 10)
        if (!isNaN(subphaseNum)) {
          updates.subphase = subphaseNum
        }
      }
      onMetaUpdate(updates)
    }
    setIsEditing(false)
  }

  const handleCancel = () => {
    setEditedPhase('')
    setEditedSubphase('')
    setIsEditing(false)
  }

  return (
    <div className="p-3 bg-gray-50 rounded-lg">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-semibold">세션 정보</h3>
        {onMetaUpdate && (
          <button
            onClick={() => setIsEditing(!isEditing)}
            className="text-xs text-blue-600 hover:text-blue-800"
          >
            {isEditing ? '취소' : '편집'}
          </button>
        )}
      </div>

      <div className="text-xs space-y-2">
        {/* Session ID */}
        <div>
          <span className="font-medium text-gray-700">Session ID:</span>
          <div className="text-gray-600 break-all mt-1 font-mono text-xs">
            {sessionMeta.session_id}
          </div>
        </div>

        {/* Phase/Subphase */}
        {isEditing ? (
          <div className="space-y-2">
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">
                Phase:
              </label>
              <input
                type="number"
                value={editedPhase || sessionMeta.phase || ''}
                onChange={(e) => setEditedPhase(e.target.value)}
                placeholder="Phase 번호"
                className="w-full px-2 py-1 text-xs border border-gray-300 rounded"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">
                Subphase:
              </label>
              <input
                type="number"
                value={editedSubphase || sessionMeta.subphase || ''}
                onChange={(e) => setEditedSubphase(e.target.value)}
                placeholder="Subphase 번호"
                className="w-full px-2 py-1 text-xs border border-gray-300 rounded"
              />
            </div>
            <div className="flex gap-2">
              <button
                onClick={handleSave}
                className="flex-1 px-2 py-1 text-xs bg-blue-600 text-white rounded hover:bg-blue-700"
              >
                저장
              </button>
              <button
                onClick={handleCancel}
                className="flex-1 px-2 py-1 text-xs bg-gray-200 text-gray-700 rounded hover:bg-gray-300"
              >
                취소
              </button>
            </div>
          </div>
        ) : (
          <div>
            <span className="font-medium text-gray-700">Phase:</span>{' '}
            {sessionMeta.phase !== undefined ? (
              <span className="text-gray-600">
                {sessionMeta.phase}
                {sessionMeta.subphase !== undefined && `-${sessionMeta.subphase}`}
              </span>
            ) : (
              <span className="text-gray-400">미지정</span>
            )}
          </div>
        )}

        {/* Exported At */}
        {sessionMeta.exported_at && (
          <div>
            <span className="font-medium text-gray-700">Exported:</span>{' '}
            <span className="text-gray-600">{sessionMeta.exported_at}</span>
          </div>
        )}

        {/* Cursor Version */}
        {sessionMeta.cursor_version && (
          <div>
            <span className="font-medium text-gray-700">Cursor Version:</span>{' '}
            <span className="text-gray-600">{sessionMeta.cursor_version}</span>
          </div>
        )}

        {/* Source Doc */}
        {sessionMeta.source_doc && (
          <div>
            <span className="font-medium text-gray-700">Source:</span>{' '}
            <span className="text-gray-600 break-all">{sessionMeta.source_doc}</span>
          </div>
        )}
      </div>
    </div>
  )
}

