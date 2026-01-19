'use client'

import { useState, useEffect } from 'react'
import axios from 'axios'
import {
  PlayCircle, CheckCircle, XCircle, Clock, Brain, BarChart3, Sparkles,
  FileText, TrendingUp, AlertTriangle, Target, Users, DollarSign,
  Zap, Shield, Activity, Database, ChevronRight, Award
} from 'lucide-react'

const API_URL = 'http://localhost:8000'

interface Scenario {
  id: string
  name: string
  description: string
  category: string
}

interface WorkflowResult {
  workflow_id: string
  status: string
  progress?: number
  current_stage?: string
  results?: any
  error?: string
  scenario_type?: string
}

const SCENARIO_DATA: Record<string, any> = {
  emergency: {
    title: "Hurricane Disaster Response",
    context: "Emergency resource allocation across 3 affected regions",
    dataPoints: {
      "Total Population Affected": "7.5 Million",
      "Emergency Budget": "$50 Million",
      "Available Medical Teams": "15 Teams",
      "Critical Timeline": "24 Hours"
    },
    regions: [
      {
        name: "Region A",
        population: "2.5M",
        powerOutage: "60%",
        hospitals: "3 at capacity",
        supplies: "Water: 40%, Medical: 30%",
        severity: "High"
      },
      {
        name: "Region B",
        population: "1.8M",
        powerOutage: "85%",
        hospitals: "1 offline",
        supplies: "Water: 15%, Medical: 20%",
        severity: "Critical"
      },
      {
        name: "Region C",
        population: "3.2M",
        powerOutage: "30%",
        hospitals: "5 operational",
        supplies: "Water: 70%, Medical: 60%",
        severity: "Moderate"
      }
    ]
  },
  infrastructure: {
    title: "National Infrastructure Investment",
    context: "$300 Billion allocation over 5 years",
    dataPoints: {
      "Total Budget": "$300 Billion",
      "Timeline": "5 Years",
      "Sectors": "3 (Transport, Energy, Telecom)",
      "Population Impact": "328 Million"
    },
    sectors: [
      {
        name: "Transportation",
        issue: "35% of bridges need repair",
        cost: "$120B/year congestion",
        status: "Critical"
      },
      {
        name: "Energy Grid",
        issue: "60% infrastructure over 30 years old",
        cost: "15 blackout incidents/year",
        status: "Urgent"
      },
      {
        name: "Telecommunications",
        issue: "25M without broadband",
        cost: "$80B/year economic impact",
        status: "High Priority"
      }
    ]
  }
}

export default function Home() {
  const [scenarios, setScenarios] = useState<Scenario[]>([])
  const [selectedScenario, setSelectedScenario] = useState<string>('')
  const [workflow, setWorkflow] = useState<WorkflowResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [showDataPreview, setShowDataPreview] = useState(false)

  useEffect(() => {
    fetchScenarios()
  }, [])

  const fetchScenarios = async () => {
    try {
      const response = await axios.get(`${API_URL}/scenarios`)
      setScenarios(response.data.scenarios)
    } catch (error) {
      console.error('Error fetching scenarios:', error)
    }
  }

  const runWorkflow = async () => {
    if (!selectedScenario) return

    setLoading(true)
    setShowDataPreview(true)

    try {
      const response = await axios.post(`${API_URL}/workflow/run`, {
        scenario_type: selectedScenario
      })

      const workflowId = response.data.workflow_id
      setWorkflow({
        workflow_id: workflowId,
        status: 'running',
        progress: 0,
        scenario_type: selectedScenario
      })

      pollWorkflowStatus(workflowId)
    } catch (error) {
      console.error('Error starting workflow:', error)
      setLoading(false)
    }
  }

  const pollWorkflowStatus = async (workflowId: string) => {
    const pollInterval = setInterval(async () => {
      try {
        const response = await axios.get(`${API_URL}/workflow/${workflowId}`)
        setWorkflow(response.data)

        if (response.data.status === 'completed' || response.data.status === 'failed') {
          clearInterval(pollInterval)
          setLoading(false)
        }
      } catch (error) {
        console.error('Error polling workflow:', error)
        clearInterval(pollInterval)
        setLoading(false)
      }
    }, 2000)
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'running':
        return <Clock className="w-6 h-6 text-blue-500 animate-spin" />
      case 'completed':
        return <CheckCircle className="w-6 h-6 text-green-500" />
      case 'failed':
        return <XCircle className="w-6 h-6 text-red-500" />
      default:
        return <Clock className="w-6 h-6 text-gray-500" />
    }
  }

  const renderDataPreview = () => {
    if (!selectedScenario || !showDataPreview) return null

    const data = SCENARIO_DATA[selectedScenario]
    if (!data) return null

    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl p-8 mb-8">
        <div className="flex items-center mb-6">
          <Database className="w-8 h-8 text-blue-600 mr-3" />
          <div>
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
              Data Being Analyzed
            </h2>
            <p className="text-gray-600 dark:text-gray-400">
              {data.context}
            </p>
          </div>
        </div>

        {/* Key Metrics */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {Object.entries(data.dataPoints).map(([key, value]: [string, any]) => (
            <div key={key} className="bg-gradient-to-br from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 rounded-lg p-4 border border-blue-100 dark:border-blue-800">
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-1">{key}</p>
              <p className="text-2xl font-bold text-blue-600 dark:text-blue-400">{value}</p>
            </div>
          ))}
        </div>

        {/* Detailed Data */}
        {selectedScenario === 'emergency' && data.regions && (
          <div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <Target className="w-5 h-5 mr-2" />
              Regional Breakdown
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {data.regions.map((region: any, idx: number) => (
                <div key={idx} className="border border-gray-200 dark:border-gray-700 rounded-lg p-4 hover:shadow-lg transition-shadow">
                  <div className="flex items-center justify-between mb-3">
                    <h4 className="font-bold text-lg text-gray-900 dark:text-white">{region.name}</h4>
                    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                      region.severity === 'Critical' ? 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300' :
                      region.severity === 'High' ? 'bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300' :
                      'bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300'
                    }`}>
                      {region.severity}
                    </span>
                  </div>
                  <div className="space-y-2 text-sm">
                    <div className="flex items-center justify-between">
                      <span className="text-gray-600 dark:text-gray-400">Population:</span>
                      <span className="font-semibold text-gray-900 dark:text-white">{region.population}</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-gray-600 dark:text-gray-400">Power Outage:</span>
                      <span className="font-semibold text-red-600 dark:text-red-400">{region.powerOutage}</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-gray-600 dark:text-gray-400">Hospitals:</span>
                      <span className="font-semibold text-gray-900 dark:text-white">{region.hospitals}</span>
                    </div>
                    <div className="text-gray-600 dark:text-gray-400 mt-2 pt-2 border-t border-gray-200 dark:border-gray-700">
                      <span className="text-xs">Supplies: {region.supplies}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {selectedScenario === 'infrastructure' && data.sectors && (
          <div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <TrendingUp className="w-5 h-5 mr-2" />
              Sector Analysis
            </h3>
            <div className="space-y-4">
              {data.sectors.map((sector: any, idx: number) => (
                <div key={idx} className="border border-gray-200 dark:border-gray-700 rounded-lg p-4 hover:shadow-lg transition-shadow">
                  <div className="flex items-center justify-between mb-2">
                    <h4 className="font-bold text-gray-900 dark:text-white">{sector.name}</h4>
                    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                      sector.status === 'Critical' ? 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300' :
                      sector.status === 'Urgent' ? 'bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300' :
                      'bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300'
                    }`}>
                      {sector.status}
                    </span>
                  </div>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
                    <div>
                      <span className="text-gray-600 dark:text-gray-400 block mb-1">Issue:</span>
                      <span className="text-gray-900 dark:text-white font-medium">{sector.issue}</span>
                    </div>
                    <div>
                      <span className="text-gray-600 dark:text-gray-400 block mb-1">Economic Impact:</span>
                      <span className="text-red-600 dark:text-red-400 font-semibold">{sector.cost}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    )
  }

  const renderAgentProgress = () => {
    if (!workflow || workflow.status !== 'running') return null

    const stages = [
      { name: 'Data Ingestion', icon: Database, description: 'Processing unstructured data from multiple sources' },
      { name: 'Analysis', icon: BarChart3, description: 'Identifying constraints, risks, and key insights' },
      { name: 'Reasoning', icon: Brain, description: 'Evaluating options against constraints' },
      { name: 'Decision', icon: Target, description: 'Synthesizing recommendations' },
      { name: 'Execution Planning', icon: Zap, description: 'Generating action plans' }
    ]

    const currentStageIndex = stages.findIndex(s => workflow.current_stage?.includes(s.name))

    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl p-8 mb-8">
        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
          <Activity className="w-6 h-6 mr-2 text-blue-600" />
          AI Agents Working
        </h3>
        <div className="space-y-4">
          {stages.map((stage, idx) => {
            const Icon = stage.icon
            const isActive = idx === currentStageIndex
            const isCompleted = idx < currentStageIndex

            return (
              <div key={stage.name} className={`
                flex items-start p-4 rounded-lg border-2 transition-all
                ${isActive ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20' :
                  isCompleted ? 'border-green-500 bg-green-50 dark:bg-green-900/20' :
                  'border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900/20'}
              `}>
                <div className="flex-shrink-0">
                  {isCompleted ? (
                    <CheckCircle className="w-6 h-6 text-green-600" />
                  ) : isActive ? (
                    <Icon className="w-6 h-6 text-blue-600 animate-pulse" />
                  ) : (
                    <Icon className="w-6 h-6 text-gray-400" />
                  )}
                </div>
                <div className="ml-4 flex-1">
                  <h4 className={`font-semibold ${
                    isActive ? 'text-blue-600' :
                    isCompleted ? 'text-green-600' :
                    'text-gray-600 dark:text-gray-400'
                  }`}>
                    {stage.name}
                    {isActive && <span className="ml-2 text-sm">(In Progress...)</span>}
                    {isCompleted && <span className="ml-2 text-sm">(✓ Complete)</span>}
                  </h4>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                    {stage.description}
                  </p>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    )
  }

  const renderExecutiveSummary = () => {
    if (!workflow?.results?.stages?.decision?.data?.decision) return null

    const decision = workflow.results.stages.decision.data.decision
    const analysis = workflow.results.stages.analysis

    return (
      <div className="bg-gradient-to-br from-blue-600 to-purple-700 rounded-lg shadow-2xl p-8 mb-8 text-white">
        <div className="flex items-center mb-6">
          <Award className="w-12 h-12 mr-4" />
          <div>
            <h2 className="text-3xl font-bold">Executive Summary</h2>
            <p className="text-blue-100">AI-Generated Decision Analysis</p>
          </div>
        </div>

        <div className="bg-white/10 backdrop-blur-sm rounded-lg p-6 mb-6">
          <h3 className="text-xl font-semibold mb-3 flex items-center">
            <ChevronRight className="w-5 h-5 mr-2" />
            Recommended Decision
          </h3>
          <p className="text-lg leading-relaxed">
            {decision['RECOMMENDED DECISION'] || decision.decision_summary}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <div className="flex items-center mb-2">
              <Shield className="w-5 h-5 mr-2" />
              <span className="text-sm text-blue-100">Confidence</span>
            </div>
            <p className="text-2xl font-bold">{decision['CONFIDENCE LEVEL'] || 'N/A'}</p>
          </div>
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <div className="flex items-center mb-2">
              <Zap className="w-5 h-5 mr-2" />
              <span className="text-sm text-blue-100">Priority</span>
            </div>
            <p className="text-2xl font-bold">{decision['IMPLEMENTATION PRIORITY'] || 'N/A'}</p>
          </div>
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <div className="flex items-center mb-2">
              <Activity className="w-5 h-5 mr-2" />
              <span className="text-sm text-blue-100">Status</span>
            </div>
            <p className="text-2xl font-bold">Ready to Execute</p>
          </div>
        </div>
      </div>
    )
  }

  const renderDetailedResults = () => {
    if (!workflow?.results?.stages?.decision?.data?.decision) return null

    const decision = workflow.results.stages.decision.data.decision

    return (
      <div className="space-y-6">
        {/* Key Supporting Factors */}
        {decision['KEY SUPPORTING FACTORS'] && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <Sparkles className="w-6 h-6 text-yellow-500 mr-2" />
              Key Supporting Factors
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {decision['KEY SUPPORTING FACTORS'].map((factor: string, idx: number) => (
                <div key={idx} className="flex items-start p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-800">
                  <CheckCircle className="w-5 h-5 text-green-600 mr-3 flex-shrink-0 mt-0.5" />
                  <span className="text-gray-800 dark:text-gray-200">{factor}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Implementation Roadmap */}
        {decision['NEXT STEPS'] && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <Target className="w-6 h-6 text-blue-600 mr-2" />
              Implementation Roadmap
            </h3>
            <div className="space-y-3">
              {decision['NEXT STEPS'].map((step: string, idx: number) => (
                <div key={idx} className="flex items-start p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border-l-4 border-blue-600">
                  <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold mr-4">
                    {idx + 1}
                  </div>
                  <div className="flex-1">
                    <p className="text-gray-800 dark:text-gray-200 font-medium">{step}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Risk Analysis */}
        {decision['IDENTIFIED RISKS'] && decision['IDENTIFIED RISKS'].length > 0 && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <AlertTriangle className="w-6 h-6 text-red-600 mr-2" />
              Risk Analysis & Mitigation
            </h3>
            <div className="space-y-3">
              {decision['IDENTIFIED RISKS'].map((risk: any, idx: number) => (
                <div key={idx} className="flex items-start p-4 bg-red-50 dark:bg-red-900/20 rounded-lg border-l-4 border-red-600">
                  <AlertTriangle className="w-5 h-5 text-red-600 mr-3 flex-shrink-0 mt-0.5" />
                  <span className="text-gray-800 dark:text-gray-200">
                    {typeof risk === 'string' ? risk : JSON.stringify(risk)}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Success Metrics */}
        {decision['SUCCESS METRICS'] && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center">
              <TrendingUp className="w-6 h-6 text-green-600 mr-2" />
              Success Metrics
            </h3>
            <div className="prose dark:prose-invert max-w-none">
              <p className="text-gray-700 dark:text-gray-300">{decision['SUCCESS METRICS']}</p>
            </div>
          </div>
        )}
      </div>
    )
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center mb-4">
            <Brain className="w-16 h-16 text-blue-600 animate-pulse" />
          </div>
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-4">
            Agentic AI System
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            National-Scale Operational Decision Making
          </p>
          <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
            Multi-Agent GenAI • Constraint-Based Reasoning • Automated Workflows
          </p>
        </div>

        {/* Scenario Selection */}
        {!workflow && (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl p-8 mb-8">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
              Select a Scenario
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              {scenarios.map((scenario) => (
                <div
                  key={scenario.id}
                  onClick={() => setSelectedScenario(scenario.id)}
                  className={`
                    cursor-pointer rounded-lg p-6 border-2 transition-all
                    ${selectedScenario === scenario.id
                      ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20 shadow-lg scale-105'
                      : 'border-gray-200 dark:border-gray-700 hover:border-blue-300 hover:shadow-md'
                    }
                  `}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                        {scenario.name}
                      </h3>
                      <p className="text-sm text-gray-600 dark:text-gray-300 mb-2">
                        {scenario.description}
                      </p>
                      <span className="inline-block px-3 py-1 text-xs font-semibold text-blue-600 bg-blue-100 dark:bg-blue-900 dark:text-blue-300 rounded-full">
                        {scenario.category}
                      </span>
                    </div>
                    {selectedScenario === scenario.id && (
                      <CheckCircle className="w-6 h-6 text-blue-600 flex-shrink-0 ml-4" />
                    )}
                  </div>
                </div>
              ))}
            </div>

            <button
              onClick={runWorkflow}
              disabled={!selectedScenario || loading}
              className={`
                w-full py-4 px-6 rounded-lg font-semibold text-white text-lg
                flex items-center justify-center space-x-2
                transition-all transform hover:scale-105
                ${!selectedScenario || loading
                  ? 'bg-gray-400 cursor-not-allowed'
                  : 'bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 shadow-lg'
                }
              `}
            >
              <PlayCircle className="w-6 h-6" />
              <span>{loading ? 'Starting Analysis...' : 'Run AI Analysis'}</span>
            </button>
          </div>
        )}

        {/* Data Preview */}
        {renderDataPreview()}

        {/* Agent Progress */}
        {renderAgentProgress()}

        {/* Results */}
        {workflow && workflow.status === 'completed' && (
          <>
            {renderExecutiveSummary()}
            {renderDetailedResults()}

            <button
              onClick={() => {
                setWorkflow(null)
                setSelectedScenario('')
                setShowDataPreview(false)
              }}
              className="mt-8 w-full py-3 px-6 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 rounded-lg font-semibold transition-colors"
            >
              Run Another Analysis
            </button>
          </>
        )}

        {/* Error State */}
        {workflow && workflow.status === 'failed' && (
          <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-6">
            <div className="flex items-center mb-4">
              <XCircle className="w-8 h-8 text-red-600 mr-3" />
              <h3 className="text-xl font-semibold text-red-800 dark:text-red-300">
                Analysis Failed
              </h3>
            </div>
            <p className="text-red-800 dark:text-red-300 mb-4">{workflow.error}</p>
            <button
              onClick={() => {
                setWorkflow(null)
                setSelectedScenario('')
                setShowDataPreview(false)
              }}
              className="px-6 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold transition-colors"
            >
              Try Again
            </button>
          </div>
        )}
      </div>
    </main>
  )
}
