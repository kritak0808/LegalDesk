'use client';

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import {
  Briefcase,
  FileText,
  ShieldCheck,
  Building2,
  Users,
  KeyRound,
  Laptop,
  UserCheck,
  AlertTriangle,
  Clock,
  CheckCircle2,
  FileCheck,
  Sparkles,
  Search,
  Plus,
  Share2,
  Eye,
  Sliders,
  Building,
  Globe,
  Smartphone,
  Check,
  X,
  Trash2,
  RefreshCw,
  LogOut,
  ChevronRight,
  ExternalLink,
  Kanban,
  MessageSquare,
  Paperclip,
  Pin,
  Send,
  Calendar,
  Layers,
  Filter,
  ArrowRight,
  BookOpen,
  CheckSquare,
  DollarSign,
  FileCode,
  GitBranch,
  Network,
  Cpu,
  BrainCircuit,
  Zap,
  SlidersHorizontal,
  Scale,
  Gavel,
  ShieldAlert,
  FileSpreadsheet,
  Grid,
  Landmark,
  Bot,
  FileCheck2,
  Library,
  Bookmark,
  FileSearch,
  Workflow,
  Play,
  RotateCcw,
  SlidersVertical,
  Crown,
  TrendingUp,
  PieChart,
  Brain,
  BarChart3,
  Download,
  Link2,
  Mail,
  PenTool,
  Radio,
  Activity,
  Shield,
  Gauge,
  Server,
  Database,
} from 'lucide-react';
import { useWorkspaceStore } from '@/store/useWorkspaceStore';
import { cn } from '@/lib/utils';

export const WorkspaceCanvas: React.FC = () => {
  const { activeView, activeMatterId, activeContractId, activeCaseId } = useWorkspaceStore();

  return (
    <main className="flex-1 bg-canvas canvas-grid overflow-y-auto p-6 h-[calc(100vh-3.5rem)] relative">
      <motion.div
        key={activeView}
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.25 }}
        className="max-w-7xl mx-auto space-y-6 pb-24"
      >
        {activeView === 'operations_center' && <OperationsCenterView />}
        {activeView === 'security_operations' && <SecurityOperationsView />}
        {activeView === 'observability_studio' && <ObservabilityStudioView />}
        {activeView === 'job_monitoring' && <JobMonitoringView />}
        {activeView === 'backup_recovery' && <BackupRecoveryView />}
        {activeView === 'integration_hub' && <IntegrationHubView />}
        {activeView === 'email_intelligence_center' && <EmailIntelligenceView />}
        {activeView === 'esignature_tracker' && <ESignatureTrackerView />}
        {activeView === 'webhook_explorer' && <WebhookExplorerView />}
        {activeView === 'executive_command_center' && <ExecutiveCommandCenterView />}
        {activeView === 'general_counsel_studio' && <GeneralCounselStudioView />}
        {activeView === 'legal_spend_center' && <LegalSpendCenterView />}
        {activeView === 'predictive_intelligence' && <PredictiveIntelligenceView />}
        {activeView === 'board_reporting_center' && <BoardReportingCenterView />}
        {activeView === 'matters' && <MatterStudioView matterId={activeMatterId} />}
        {activeView === 'matter_explorer' && <MatterExplorerView />}
        {activeView === 'contracts' && <ContractStudioView contractId={activeContractId} />}
        {activeView === 'contract_explorer' && <ContractExplorerView />}
        {activeView === 'clause_library' && <ClauseLibraryView />}
        {activeView === 'renewal_center' && <RenewalCenterView />}
        {activeView === 'ai_review_studio' && <AIReviewStudioView />}
        {activeView === 'document_intelligence' && <DocumentIntelligenceView />}
        {activeView === 'semantic_search' && <SemanticSearchView />}
        {activeView === 'knowledge_graph' && <KnowledgeGraphView />}
        {activeView === 'negotiation_assistant' && <NegotiationAssistantView />}
        {activeView === 'litigation' && <LitigationCanvasView caseId={activeCaseId} />}
        {activeView === 'evidence_studio' && <EvidenceStudioView />}
        {activeView === 'court_calendar' && <CourtCalendarView />}
        {activeView === 'settlement_workspace' && <SettlementWorkspaceView />}
        {activeView === 'compliance' && <ComplianceMatrixView />}
        {activeView === 'policy_studio' && <PolicyStudioView />}
        {activeView === 'risk_register' && <RiskRegisterView />}
        {activeView === 'board_governance' && <BoardGovernanceView />}
        {activeView === 'ai_governance' && <AIGovernanceView />}
        {activeView === 'legal_research_studio' && <LegalResearchStudioView />}
        {activeView === 'citation_explorer' && <CitationExplorerView />}
        {activeView === 'ai_research_assistant' && <AIResearchAssistantView />}
        {activeView === 'memorandum_workspace' && <MemorandumWorkspaceView />}
        {activeView === 'workflow_studio' && <WorkflowStudioView />}
        {activeView === 'approval_center' && <ApprovalCenterView />}
        {activeView === 'process_explorer' && <ProcessExplorerView />}
        {activeView === 'automation_center' && <AutomationCenterView />}
        {activeView === 'governance' && <BoardGovernanceView />}
        {activeView === 'organizations' && <OrganizationStudioView />}
        {activeView === 'people' && <PeopleDirectoryView />}
        {activeView === 'teams' && <TeamsStructureView />}
        {activeView === 'roles' && <RBACMatrixView />}
        {activeView === 'sessions' && <SessionsDeviceView />}
        {activeView === 'profile' && <UserProfileView />}
        {activeView === 'security' && <SecurityAuditView />}
      </motion.div>
    </main>
  );
};

/* =========================================================================
   1. ENTERPRISE OPERATIONS CENTER (PHASE 12 FLAGSHIP)
   ========================================================================= */
const OperationsCenterView: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-emerald-950 to-slate-900 text-white border border-emerald-800/40 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <Activity className="w-4 h-4 text-emerald-400" />
            <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
              RELIABILITY & PLATFORM OPERATIONS HUB
            </span>
          </div>
          <h1 className="text-2xl font-bold tracking-tight">Enterprise Operations & Health Matrix</h1>
          <p className="text-sm text-slate-300 mt-1">Real-time platform availability (99.99%), API P99 latency (42ms), and infrastructure node health.</p>
        </div>

        <button className="px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-semibold text-white transition-all shadow-lg flex items-center gap-2 font-bold">
          <RefreshCw className="w-4 h-4 text-white animate-spin" />
          Live Metrics Streaming
        </button>
      </div>

      {/* Infrastructure Health Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { label: 'Platform Availability', val: '99.99%', sub: 'Zero Active Outages', icon: Activity, color: 'text-emerald-400' },
          { label: 'API P99 Latency', val: '42 ms', sub: 'Target Threshold: <100ms', icon: Gauge, color: 'text-brand-400' },
          { label: 'Database Health', val: 'PostgreSQL 16', sub: 'Primary + 2 Replicas', icon: Database, color: 'text-indigo-400' },
          { label: 'Background Queues', val: '12 Workers', sub: '0 Dead Letter Jobs', icon: Server, color: 'text-gold-400' },
        ].map((sc, idx) => {
          const Icon = sc.icon;
          return (
            <div key={idx} className="p-4 rounded-2xl glass-panel flex flex-col justify-between shadow-sm border border-slate-200 dark:border-slate-800">
              <div className="flex items-center justify-between">
                <span className="text-xs font-medium text-slate-500 dark:text-slate-400">{sc.label}</span>
                <Icon className={cn('w-4 h-4', sc.color)} />
              </div>
              <div className="mt-2">
                <div className="text-2xl font-bold text-slate-900 dark:text-slate-100">{sc.val}</div>
                <div className="text-[11px] text-slate-400 mt-0.5">{sc.sub}</div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Component Status Table */}
      <div className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-3">
        <h3 className="text-sm font-semibold text-slate-900 dark:text-slate-100 flex items-center gap-2">
          <Server className="w-4 h-4 text-emerald-400" />
          Component Health & Node Status
        </h3>
        <div className="space-y-2 text-xs text-slate-300">
          {[
            { name: 'API Gateway (FastAPI Uvicorn Cluster)', status: 'Healthy', latency: '18.5 ms', uptime: '99.99%' },
            { name: 'PostgreSQL 16 Database Cluster (Async SQLAlchemy 2.0)', status: 'Healthy', latency: '4.2 ms', uptime: '99.99%' },
            { name: 'Redis Enterprise Cache & Pub/Sub Cluster', status: 'Healthy', latency: '1.1 ms', uptime: '100.0%' },
            { name: 'Celery Background Worker Nodes (12 Active Workers)', status: 'Healthy', latency: '320.0 ms', uptime: '99.98%' },
          ].map((c, i) => (
            <div key={i} className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between">
              <div>
                <span className="font-bold text-slate-100">{c.name}</span>
                <span className="text-[10px] text-slate-400 block">Avg Response: {c.latency}</span>
              </div>
              <div className="text-right">
                <span className="px-2 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-bold">
                  {c.status}
                </span>
                <span className="text-[10px] text-slate-400 block mt-0.5">Uptime: {c.uptime}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

/* =========================================================================
   2. SECURITY OPERATIONS CENTER (SOC)
   ========================================================================= */
const SecurityOperationsView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-rose-950 to-slate-900 text-white border border-rose-800/40 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Security Operations Center (SOC)</h1>
      <p className="text-sm text-slate-300 mt-1">Real-time threat detection, authentication logs, permission violation audits, and IP throttling.</p>
    </div>

    <div className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-3 text-xs text-slate-200">
      <div className="flex items-center justify-between">
        <div>
          <div className="font-bold text-slate-100">Suspicious Login Location Throttled</div>
          <div className="text-[10px] text-slate-400">Source IP: 198.51.100.42 • MFA Challenge Enforced & Session Audited</div>
        </div>
        <span className="px-3 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">
          MFA Enforced
        </span>
      </div>
    </div>
  </div>
);

/* =========================================================================
   3. OBSERVABILITY & TRACING
   ========================================================================= */
const ObservabilityStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-gold-950 to-slate-900 text-white border border-gold-800/40 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Distributed Tracing & Request Observability</h1>
      <p className="text-sm text-slate-300 mt-1">Request Correlation IDs, microsecond latency breakdowns, and Redis cache hit ratios (96.8%).</p>
    </div>

    <div className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-3 text-xs text-slate-200">
      <div className="flex items-center justify-between">
        <div>
          <div className="font-bold text-slate-100">Trace ID: tr-8947291847 (POST /api/v1/ai/review/contract)</div>
          <div className="text-[10px] text-slate-400">Total Duration: 142.5ms • Postgres Query: 4.5ms • RAG Vector Search: 118.2ms</div>
        </div>
        <span className="px-3 py-1 rounded bg-gold-500/20 text-gold-300 font-bold border border-gold-500/30">
          200 OK (142ms)
        </span>
      </div>
    </div>
  </div>
);

/* =========================================================================
   4. BACKGROUND JOB MONITORING
   ========================================================================= */
const JobMonitoringView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white border border-indigo-800/40 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Celery Background Job & Worker Queue Center</h1>
      <p className="text-sm text-slate-300 mt-1">Worker node status, queue latency, execution retry history, and dead letter queue management.</p>
    </div>

    <div className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-3 text-xs text-slate-200">
      <div className="flex items-center justify-between">
        <div>
          <div className="font-bold text-slate-100">Queue: celery-high-priority (4 Active Workers)</div>
          <div className="text-[10px] text-slate-400">Queue Depth: 0 Jobs • Completed 24h: 1,420 • Failed 24h: 0</div>
        </div>
        <span className="px-3 py-1 rounded bg-indigo-500/20 text-indigo-300 font-bold border border-indigo-500/30">
          0 Pending Jobs
        </span>
      </div>
    </div>
  </div>
);

/* =========================================================================
   5. BACKUP & DISASTER RECOVERY
   ========================================================================= */
const BackupRecoveryView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-brand-950 to-slate-900 text-white border border-brand-800/40 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Backup & Disaster Recovery Center</h1>
      <p className="text-sm text-slate-300 mt-1">Point-in-time database recovery, AES-256 encrypted archives, and restore drill validation.</p>
    </div>

    <div className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-3 text-xs text-slate-200">
      <div className="flex items-center justify-between">
        <div>
          <div className="font-bold text-slate-100">Backup BKP-2026-089: Point-in-Time Database Backup</div>
          <div className="text-[10px] text-slate-400">Size: 4.2 GB • Encryption: AES-256 • Verified: 2026-07-24 03:00:00</div>
        </div>
        <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">
          Verified & Encrypted
        </span>
      </div>
    </div>
  </div>
);

/* =========================================================================
   6. INTEGRATION ECOSYSTEM & CONNECTED HUBS
   ========================================================================= */
const IntegrationHubView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white border border-indigo-800/40 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div className="flex items-center gap-2 mb-2">
          <Link2 className="w-4 h-4 text-indigo-400" />
          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
            ENTERPRISE INTEGRATION HUB
          </span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">Ecosystem Connections & Connectors</h1>
        <p className="text-sm text-slate-300 mt-1">Bi-directional synchronization with M365, Google Workspace, DocuSign, Salesforce, Workday & Slack.</p>
      </div>
      <button className="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-semibold text-white transition-all shadow-lg flex items-center gap-2">
        <Plus className="w-4 h-4" /> Add Integration
      </button>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {[
        { name: 'Microsoft 365 / Outlook', category: 'Email & Calendar', status: 'Connected', sync: '2 mins ago', icon: Mail, color: 'text-blue-400' },
        { name: 'Google Workspace', category: 'Cloud Storage & Docs', status: 'Connected', sync: 'Just now', icon: Globe, color: 'text-rose-400' },
        { name: 'DocuSign e-Signature', category: 'CLM & Signature', status: 'Connected', sync: '15 mins ago', icon: PenTool, color: 'text-amber-400' },
        { name: 'Salesforce CRM', category: 'Contract Ingestion', status: 'Connected', sync: '1 hour ago', icon: Database, color: 'text-sky-400' },
        { name: 'Workday Enterprise', category: 'HR & Employee IAM', status: 'Connected', sync: 'Syncing...', icon: Building2, color: 'text-indigo-400' },
        { name: 'Slack Enterprise Grid', category: 'Real-Time Alerts', status: 'Connected', sync: 'Live', icon: Radio, color: 'text-emerald-400' },
      ].map((int, i) => {
        const Icon = int.icon;
        return (
          <div key={i} className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                  <Icon className={cn('w-5 h-5', int.color)} />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-slate-100">{int.name}</h3>
                  <p className="text-[11px] text-slate-400">{int.category}</p>
                </div>
              </div>
              <span className="px-2 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-bold">
                {int.status}
              </span>
            </div>
            <div className="flex items-center justify-between text-xs text-slate-400 pt-2 border-t border-slate-800">
              <span>Last Sync: {int.sync}</span>
              <button className="text-brand-400 hover:text-brand-300 font-semibold text-[11px]">Configure →</button>
            </div>
          </div>
        );
      })}
    </div>
  </div>
);

const EmailIntelligenceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Email Intelligence & Thread Parsing</h1>
      <p className="text-sm text-slate-300 mt-1">Automated attorney-client privilege classification, key dates extraction, and attachment indexing.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-3">
      <div className="flex items-center justify-between text-xs text-slate-300">
        <div>
          <div className="font-bold text-slate-100">Thread: Re: Acquisition Terms & Regulatory Indemnity</div>
          <div className="text-[10px] text-slate-400">From: legal-ops@acme.com • Privilege Tag: CONFIDENTIAL & PRIVILEGED</div>
        </div>
        <span className="px-3 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">Privileged</span>
      </div>
    </div>
  </div>
);

const ESignatureTrackerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">E-Signature Lifecycle & Envelope Tracker</h1>
      <p className="text-sm text-slate-300 mt-1">Real-time status of active DocuSign and Adobe Sign execution envelopes.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-3">
      <div className="flex items-center justify-between text-xs text-slate-300">
        <div>
          <div className="font-bold text-slate-100">Envelope ENV-2026-9812: Master Services Agreement v3</div>
          <div className="text-[10px] text-slate-400">Signers: 2/2 Completed • Hash Vault SHA-256 Verified</div>
        </div>
        <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">Fully Executed</span>
      </div>
    </div>
  </div>
);

const WebhookExplorerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Webhook Explorer & Event Bus</h1>
      <p className="text-sm text-slate-300 mt-1">Manage outbound webhooks, HMAC signature secret keys, and payload dispatch delivery logs.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="flex items-center justify-between">
        <div>
          <div className="font-bold text-slate-100">Endpoint: https://hooks.acme-corp.internal/legal/matter-updated</div>
          <div className="text-[10px] text-slate-400">Events: matter.created, matter.closed • Success Rate: 100% (4,120 dispatches)</div>
        </div>
        <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">Active</span>
      </div>
    </div>
  </div>
);

/* =========================================================================
   7. EXECUTIVE INTELLIGENCE & SPEND SUITE
   ========================================================================= */
const ExecutiveCommandCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-gold-950 to-slate-900 text-white border border-gold-800/40 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div className="flex items-center gap-2 mb-2">
          <Crown className="w-4 h-4 text-gold-400" />
          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-gold-500/20 text-gold-300 border border-gold-500/30">
            EXECUTIVE HQ & GENERAL COUNSEL STUDIO
          </span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">Executive Intelligence Command Center</h1>
        <p className="text-sm text-slate-300 mt-1">Strategic legal risk exposure ($42.5M), external counsel spend efficiency, and board compliance score.</p>
      </div>
      <div className="flex items-center gap-2">
        <button className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 rounded-xl border border-slate-700 transition-all">
          Export Board Deck
        </button>
      </div>
    </div>

    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {[
        { label: 'Active Litigation Risk Exposure', val: '$42.5M', sub: '3 High-Value Claims', icon: Gavel, color: 'text-rose-400' },
        { label: 'CLM Contract Velocity', val: '3.4 Days', sub: '32% Faster Than Q1', icon: FileText, color: 'text-brand-400' },
        { label: 'Legal Spend YTD', val: '$1.28M', sub: '92% of Budget Target', icon: DollarSign, color: 'text-gold-400' },
        { label: 'Platform Risk Score Index', val: '94 / 100', sub: 'Low Enterprise Risk', icon: ShieldCheck, color: 'text-emerald-400' },
      ].map((kpi, idx) => {
        const Icon = kpi.icon;
        return (
          <div key={idx} className="p-5 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-medium text-slate-400">{kpi.label}</span>
              <Icon className={cn('w-4 h-4', kpi.color)} />
            </div>
            <div className="text-2xl font-bold text-slate-100">{kpi.val}</div>
            <div className="text-[11px] text-slate-400">{kpi.sub}</div>
          </div>
        );
      })}
    </div>
  </div>
);

const GeneralCounselStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">General Counsel Strategy Studio</h1>
      <p className="text-sm text-slate-300 mt-1">High-stakes corporate decisions, regulatory response matrix, and strategic external counsel allocation.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Strategic Priority: Cross-Border EU AI Act Article 10 Compliance</div>
      <div className="text-[11px] text-slate-400">Assigned Partner Firm: Skadden, Arps • Budget Cap: $250,000 • Status: On Track</div>
    </div>
  </div>
);

const LegalSpendCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Legal Spend & External Counsel Analytics</h1>
      <p className="text-sm text-slate-300 mt-1">Law firm rate card benchmarking, invoice LEDES validation, and budget variance tracking.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Latham & Watkins LLP — Q3 Retainer & Invoice LEDES-98</div>
        <div className="text-[10px] text-slate-400">Invoice Total: $142,500 • Blended Rate: $850/hr • AFAs Applied: 15% Discount</div>
      </div>
      <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">Approved for Payment</span>
    </div>
  </div>
);

const PredictiveIntelligenceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Predictive AI Outcome Engine</h1>
      <p className="text-sm text-slate-300 mt-1">Machine learning trial win probability forecasts, settlement range estimators, and judicial motion analysis.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Case LIT-2026-089: Trial Win Probability Model</div>
        <div className="text-[10px] text-slate-400">Predicted Win Likelihood: 84.2% • Settlement Valuation Range: $1.4M – $1.8M</div>
      </div>
      <span className="px-3 py-1 rounded bg-brand-500/20 text-brand-400 font-bold border border-brand-500/30">High Confidence (94%)</span>
    </div>
  </div>
);

const BoardReportingCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Board Reporting & Governance Deck Builder</h1>
      <p className="text-sm text-slate-300 mt-1">Automated quarterly legal risk slides, ESG compliance metrics, and board resolution summaries.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Q3 2026 Board of Directors Legal Briefing Package</div>
      <div className="text-[10px] text-slate-400">Generated: 2026-07-24 • Includes: Litigation Exposure, CLM Velocity, GRC Status • Format: PDF / PPTX</div>
    </div>
  </div>
);

/* =========================================================================
   8. MATTER & CONTRACT WORKSTATIONS
   ========================================================================= */
const MatterStudioView: React.FC<{ matterId: string | null }> = ({ matterId }) => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl flex items-center justify-between">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <Briefcase className="w-4 h-4 text-brand-400" />
          <span className="text-xs font-mono text-brand-300">{matterId || 'MAT-2026-089'}</span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">Acme / Mergers & Acquisitions NDA Matter</h1>
        <p className="text-sm text-slate-300 mt-1">Lead Counsel: Jonathan Vance, Esq. • Practice Area: M&A Corporate • Status: In Review</p>
      </div>
      <span className="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-bold">Active Matter</span>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-2">
        <span className="text-xs text-slate-400">Risk Assessment Index</span>
        <div className="text-xl font-bold text-emerald-400">Low Risk (12/100)</div>
      </div>
      <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-2">
        <span className="text-xs text-slate-400">Budget vs Actual</span>
        <div className="text-xl font-bold text-slate-100">$45,000 / $60,000</div>
      </div>
      <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-2">
        <span className="text-xs text-slate-400">Vault Document Count</span>
        <div className="text-xl font-bold text-brand-400">14 Verified Files</div>
      </div>
    </div>
  </div>
);

const MatterExplorerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Matter Operating Explorer</h1>
      <p className="text-sm text-slate-300 mt-1">Centralized directory of corporate legal matters across all global entities and practice groups.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 space-y-2 text-xs text-slate-300">
      {[
        { id: 'MAT-2026-089', title: 'Acme / Mergers & Acquisitions NDA', area: 'M&A Corporate', risk: 'Low', status: 'Active' },
        { id: 'MAT-2026-104', title: 'SaaS Algorithm Patent Defense', area: 'IP Litigation', risk: 'Medium', status: 'In Trial' },
        { id: 'MAT-2026-201', title: 'EU AI Act Article 10 Regulatory Audit', area: 'GRC & Privacy', risk: 'High', status: 'Under Review' },
      ].map((m, i) => (
        <div key={i} className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between">
          <div>
            <span className="font-mono text-brand-400 mr-2">{m.id}</span>
            <span className="font-bold text-slate-100">{m.title}</span>
            <span className="text-[10px] text-slate-400 block mt-0.5">Practice Area: {m.area}</span>
          </div>
          <div className="text-right">
            <span className="px-2 py-0.5 rounded text-[10px] bg-slate-800 text-slate-300 font-bold border border-slate-700">{m.status}</span>
          </div>
        </div>
      ))}
    </div>
  </div>
);

const ContractStudioView: React.FC<{ contractId: string | null }> = ({ contractId }) => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl flex items-center justify-between">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <FileText className="w-4 h-4 text-brand-400" />
          <span className="text-xs font-mono text-brand-300">{contractId || 'CTR-2026-089'}</span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">Master Services Agreement (MSA) Lifecycle Studio</h1>
        <p className="text-sm text-slate-300 mt-1">Counterparty: Globex Tech Solutions Inc. • Value: $1,250,000 / yr • Effective: 2026-08-01</p>
      </div>
      <span className="px-3 py-1 rounded-full bg-brand-500/20 text-brand-400 border border-brand-500/30 text-xs font-bold">AI Redlined</span>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Key Clause Analysis: Indemnification Liability Cap</div>
      <div className="text-[10px] text-slate-400">Current Clause: Standard Mutual 2x Annual Contract Value ($2,500,000) • AI Compliance: 98%</div>
    </div>
  </div>
);

const ContractExplorerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Contract Repository & Repository Explorer</h1>
      <p className="text-sm text-slate-300 mt-1">Searchable database of executed contracts, counterparty metadata, key obligation dates, and renewals.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Contract CTR-2026-089: Enterprise SaaS Cloud License</div>
      <div className="text-[10px] text-slate-400">Counterparty: Salesforce Inc. • Renewal Date: 2026-11-15 • Value: $480,000</div>
    </div>
  </div>
);

const ClauseLibraryView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Enterprise Clause Library & Fallback Playbook</h1>
      <p className="text-sm text-slate-300 mt-1">Approved standard clauses, fallback language options, and negotiation risk thresholds.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Standard Clause #CL-402: Limitation of Liability (Mutual Cap)</div>
      <div className="text-[10px] text-slate-400">Fallback Level 1: 1x Fees Paid in 12 Months • Fallback Level 2: $1,000,000 Fixed Cap</div>
    </div>
  </div>
);

const RenewalCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Contract Renewal & Expiration Center</h1>
      <p className="text-sm text-slate-300 mt-1">Proactive 30/60/90 day contract renewal alerts, auto-renewal opt-out workflow triggers.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Vendor Contract: AWS Enterprise Support Agreement</div>
        <div className="text-[10px] text-slate-400">Auto-Renewal Notice Deadline: 2026-08-15 (21 Days Remaining)</div>
      </div>
      <span className="px-3 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">Action Needed</span>
    </div>
  </div>
);

const AIReviewStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-brand-950 to-slate-900 text-white border border-brand-800/40 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">AI Contract Review & Automated Redlining Studio</h1>
      <p className="text-sm text-slate-300 mt-1">Automated risk identification, one-click fallback insertion, and compliance scoring (94/100).</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="flex justify-between items-center">
        <div className="font-bold text-slate-100">Clause Flagged: Unlimited Indirect Damages Waiver</div>
        <span className="px-2.5 py-0.5 rounded bg-rose-500/20 text-rose-400 font-bold border border-rose-500/30">High Risk Flag</span>
      </div>
      <p className="text-[11px] text-slate-400">Recommendation: Insert Standard Consequential Damages Exclusion clause from Enterprise Library.</p>
    </div>
  </div>
);

/* =========================================================================
   9. AI PLATFORM & SEARCH ENGINE
   ========================================================================= */
const DocumentIntelligenceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">OCR & Document Intelligence Engine</h1>
      <p className="text-sm text-slate-300 mt-1">Multi-modal OCR extraction, document metadata classification, and page layout segmentation.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Processed Document: Executed_Commercial_Lease_2026.pdf</div>
      <div className="text-[10px] text-slate-400">Pages: 48 • OCR Confidence: 99.8% • Extracted Entities: 142 • Status: Vectorized</div>
    </div>
  </div>
);

const SemanticSearchView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Vector RAG & Semantic Search Studio</h1>
      <p className="text-sm text-slate-300 mt-1">High-dimensional vector embeddings search across 50,000+ indexed legal documents & precedents.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Query: "indemnification scope for third party IP infringement in SaaS agreements"</div>
      <div className="text-[10px] text-slate-400">Top Matches: 14 documents found • Similarity Cosine Score: 0.942 • Instant Retrieval</div>
    </div>
  </div>
);

const KnowledgeGraphView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Legal Knowledge Graph & Relationship Network</h1>
      <p className="text-sm text-slate-300 mt-1">Graph entity visualization connecting corporate entities, contracts, litigation cases & regulations.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Entity Node: Acme Holdings Corp (Subsidiary Network)</div>
      <div className="text-[10px] text-slate-400">Nodes Connected: 42 Contracts • 8 Regulatory Frameworks • 3 Litigation Matters</div>
    </div>
  </div>
);

const NegotiationAssistantView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">AI Negotiation Assistant & Playbook Assistant</h1>
      <p className="text-sm text-slate-300 mt-1">Real-time counterparty negotiation strategy advice, concession boundaries, and counter-drafting.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Negotiation Playbook: Counterparty Requesting Governing Law in Delaware</div>
      <div className="text-[10px] text-slate-400">AI Position Strategy: Accept Delaware venue in exchange for New York substantive law compromise.</div>
    </div>
  </div>
);

/* =========================================================================
   10. LITIGATION & EVIDENCE CUSTODY
   ========================================================================= */
const LitigationCanvasView: React.FC<{ caseId: string | null }> = ({ caseId }) => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl flex justify-between items-center">
      <div>
        <div className="flex items-center gap-2 mb-1">
          <Gavel className="w-4 h-4 text-rose-400" />
          <span className="text-xs font-mono text-rose-300">{caseId || 'LIT-2026-089'}</span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">SaaS Algorithm Patent Infringement Defense</h1>
        <p className="text-sm text-slate-300 mt-1">Court: U.S. District Court (S.D.N.Y.) • Judge: Hon. Sarah Jenkins • Claim Amount: $12,500,000</p>
      </div>
      <span className="px-3 py-1 rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold">Discovery Phase</span>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Upcoming Deadline: Motion to Dismiss Brief Due</div>
      <div className="text-[10px] text-slate-400">Filing Deadline: 2026-08-10 • Draft Status: 85% Completed</div>
    </div>
  </div>
);

const EvidenceStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Evidence Custody & SHA-256 Hash Vault</h1>
      <p className="text-sm text-slate-300 mt-1">Immutable digital evidence repository, chain of custody logging, and cryptographic verification.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Evidence Item #EV-901: Source Code Repository Snapshot v4.2</div>
        <div className="text-[10px] font-mono text-slate-400">SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</div>
      </div>
      <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">Verified Sealed</span>
    </div>
  </div>
);

const CourtCalendarView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Court Calendar & Filing Deadline Tracker</h1>
      <p className="text-sm text-slate-300 mt-1">Master calendar of court hearings, judicial conferences, discovery deadlines, and depositions.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Deposition: Lead Technical Architect (Dr. Aris Vance)</div>
      <div className="text-[10px] text-slate-400">Date: 2026-08-04 10:00 AM EST • Venue: S.D.N.Y. Courtroom 14B</div>
    </div>
  </div>
);

const SettlementWorkspaceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Dispute Settlement & Mediation Workspace</h1>
      <p className="text-sm text-slate-300 mt-1">NPV financial loss distribution, settlement proposal modeling, and mediation offer tracking.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Mediation Counter-Offer Model #2</div>
      <div className="text-[10px] text-slate-400">Settlement Lump-Sum: $1,200,000 • Paid Over 12 Months • Includes Mutual Release</div>
    </div>
  </div>
);

/* =========================================================================
   11. GRC & REGULATORY COMPLIANCE
   ========================================================================= */
const ComplianceMatrixView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Regulatory Compliance & Governance Matrix</h1>
      <p className="text-sm text-slate-300 mt-1">Real-time compliance index across EU AI Act, GDPR, SOC 2 Type II, CCPA, HIPAA, ISO 27001.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      {[
        { name: 'EU AI Act (High-Risk AI Systems Article 10)', score: '96%', status: 'Compliant' },
        { name: 'GDPR Cross-Border Data Transfer (SCCs)', score: '98%', status: 'Compliant' },
        { name: 'SOC 2 Type II Security & Confidentiality', score: '100%', status: 'Certified' },
      ].map((rule, idx) => (
        <div key={idx} className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between">
          <span className="font-bold text-slate-100">{rule.name}</span>
          <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-[10px] font-bold">
            {rule.score} • {rule.status}
          </span>
        </div>
      ))}
    </div>
  </div>
);

const PolicyStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Corporate Policy Lifecycle Studio</h1>
      <p className="text-sm text-slate-300 mt-1">Internal legal policy drafting, annual policy reviews, and employee sign-off tracking (98.2%).</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Global AI Acceptable Use Policy v2.4 (2026 Edition)</div>
      <div className="text-[10px] text-slate-400">Employee Acknowledgment: 1,420 / 1,450 (97.9%) • Next Annual Review: 2027-01-15</div>
    </div>
  </div>
);

const RiskRegisterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Enterprise Risk Register & Mitigation Matrix</h1>
      <p className="text-sm text-slate-300 mt-1">Impact vs. likelihood scoring matrix, risk owners, and residual risk tracking.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Risk #RSK-104: Vendor Cloud Data Lock-in Exposure</div>
      <div className="text-[10px] text-slate-400">Inherited Risk: Medium • Residual Risk: Low • Owner: VP Infrastructure Legal</div>
    </div>
  </div>
);

const BoardGovernanceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Corporate Board Governance & Minute Book</h1>
      <p className="text-sm text-slate-300 mt-1">Shareholder resolutions, board meeting minutes vault, officer appointment ledger.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Unanimous Written Consent of Board: Series B Equity Authorization</div>
      <div className="text-[10px] text-slate-400">Executed: 2026-06-12 • Vault Verification: Cryptographically Signed</div>
    </div>
  </div>
);

const AIGovernanceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">AI Model Governance & EU AI Act Register</h1>
      <p className="text-sm text-slate-300 mt-1">Model bias testing logs, training data lineage, human-in-the-loop audit log, EU conformity.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Model: LegalDesk-RAG-v4 (LLM fine-tuned on SEC filings & contracts)</div>
      <div className="text-[10px] text-slate-400">EU AI Act Assessment: Low Risk • Human Override Enabled • Zero Hallucination Guardrail Active</div>
    </div>
  </div>
);

/* =========================================================================
   12. LEGAL RESEARCH & CITATIONS
   ========================================================================= */
const LegalResearchStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Legal Research & Precedent Search Studio</h1>
      <p className="text-sm text-slate-300 mt-1">Multi-jurisdictional federal & state case law search, statutory annotations, Shepard's treatment.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Precedent Search: 412 F.3d 890 (2d Cir. 2024) — Software Copyright Scope</div>
      <div className="text-[10px] text-slate-400">Treatment: Positive (Followed by 14 Courts) • Key Cite Status: Green Flag</div>
    </div>
  </div>
);

const CitationExplorerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Citation Tree Explorer & Authority Rank</h1>
      <p className="text-sm text-slate-300 mt-1">Visual judicial citation network showing overruling histories and circuit splits.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Citation Node: Alice Corp. v. CLS Bank Int'l, 573 U.S. 208 (2014)</div>
      <div className="text-[10px] text-slate-400">Citations in Network: 12,480 • Patent Subject Matter Eligibility Benchmark</div>
    </div>
  </div>
);

const AIResearchAssistantView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">AI Legal Research & Synthesis Assistant</h1>
      <p className="text-sm text-slate-300 mt-1">Interactive legal query assistant with automated case law synthesis and statutory interpretation.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Query: "Extraterritorial application of CCPA data privacy penalties to EU parent companies"</div>
      <div className="text-[10px] text-slate-400">Synthesized Opinion Ready • 6 Controlling Citations Referenced</div>
    </div>
  </div>
);

const MemorandumWorkspaceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Legal Memorandum Editor & IRAC Studio</h1>
      <p className="text-sm text-slate-300 mt-1">Structured Issue-Rule-Analysis-Conclusion legal memorandum builder with 1-click PDF export.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Memo: Legal Analysis of Trade Secret Misappropriation Risk in AI Training Sets</div>
      <div className="text-[10px] text-slate-400">Author: Senior Counsel • Length: 12 Pages • Format: IRAC Verified</div>
    </div>
  </div>
);

/* =========================================================================
   13. WORKFLOW AUTOMATION & PROCESS ORCHESTRATION
   ========================================================================= */
const WorkflowStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white border border-indigo-800/40 shadow-xl flex justify-between items-center">
      <div>
        <div className="flex items-center gap-2 mb-2">
          <Workflow className="w-4 h-4 text-indigo-400" />
          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
            VISUAL WORKFLOW ORCHESTRATOR
          </span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight">Workflow Studio & Process Builder</h1>
        <p className="text-sm text-slate-300 mt-1">Design automated approval loops, SLA timers, conditional triggers, and Celery retries.</p>
      </div>
      <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-xl transition-all shadow-md">
        + Build Workflow
      </button>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Active Workflow #WF-102: High-Value MSA Legal Sign-Off Loop</div>
      <div className="text-[10px] text-slate-400">Triggers: Contract Value &gt; $500k • Approval Nodes: General Counsel &rarr; Finance VP &rarr; CEO</div>
    </div>
  </div>
);

const ApprovalCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Approval Center & Execution Queue</h1>
      <p className="text-sm text-slate-300 mt-1">Pending legal approvals for contracts, spend authorizations, settlement caps, and policies.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Approval Request #APP-891: Globex Contract Exception Request</div>
        <div className="text-[10px] text-slate-400">Requested By: Enterprise Sales VP • Time Pending: 4 Hours</div>
      </div>
      <div className="flex gap-2">
        <button className="px-3 py-1 rounded bg-emerald-600 text-white font-bold text-[11px]">Approve</button>
        <button className="px-3 py-1 rounded bg-rose-600 text-white font-bold text-[11px]">Reject</button>
      </div>
    </div>
  </div>
);

const ProcessExplorerView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Process Explorer & Bottleneck Analytics</h1>
      <p className="text-sm text-slate-300 mt-1">Analyze process velocity, identify SLA delays, and track execution completion metrics.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Process Metric: NDA Review Turnaround Time</div>
      <div className="text-[10px] text-slate-400">Average Duration: 4.2 Hours • SLA Compliance Rate: 99.4% • Bottlenecks: None</div>
    </div>
  </div>
);

const AutomationCenterView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Scheduled Automation Rules Engine</h1>
      <p className="text-sm text-slate-300 mt-1">Background automation triggers, daily risk reports, expiration notification dispatches.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Rule #AUT-401: Daily Expiration Alert Dispatch</div>
      <div className="text-[10px] text-slate-400">Schedule: Every Day at 08:00 UTC • Action: Send Slack Notification to #legal-ops</div>
    </div>
  </div>
);

/* =========================================================================
   14. IAM, USER DIRECTORY & SECURITY AUDIT
   ========================================================================= */
const OrganizationStudioView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Organization Studio & Multi-Tenant Setup</h1>
      <p className="text-sm text-slate-300 mt-1">Tenant isolation configuration, parent/subsidiary hierarchy, storage and compute quotas.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Tenant: Acme Global Corporation (Enterprise Tier)</div>
      <div className="text-[10px] text-slate-400">Storage Used: 142 GB / 5,000 GB • Active Users: 124 / 500 • Isolation: Dedicated DB Schema</div>
    </div>
  </div>
);

const PeopleDirectoryView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Legal Team & User Directory</h1>
      <p className="text-sm text-slate-300 mt-1">Active attorneys, paralegals, compliance officers, external counsel, and bar admissions.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      {[
        { name: 'Jonathan Vance, Esq.', role: 'General Counsel', bar: 'NY State Bar #481920', status: 'Active' },
        { name: 'Elena Rostova, Esq.', role: 'VP IP & Litigation', bar: 'CA State Bar #294012', status: 'Active' },
      ].map((u, i) => (
        <div key={i} className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 flex justify-between items-center">
          <div>
            <span className="font-bold text-slate-100">{u.name}</span>
            <span className="text-[10px] text-slate-400 block">{u.role} • {u.bar}</span>
          </div>
          <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30 text-[10px]">{u.status}</span>
        </div>
      ))}
    </div>
  </div>
);

const TeamsStructureView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Practice Group & Team Structure</h1>
      <p className="text-sm text-slate-300 mt-1">Departmental team allocation, cross-functional legal pods, and workload distribution.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300">
      <div className="font-bold text-slate-100">Team: Commercial Contracts & Licensing Pod</div>
      <div className="text-[10px] text-slate-400">Members: 8 Attorneys • Active Contracts Under Review: 34 • Workload: Balanced</div>
    </div>
  </div>
);

const RBACMatrixView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Role-Based Access Control (RBAC) Matrix</h1>
      <p className="text-sm text-slate-300 mt-1">Granular permission matrix (Super Admin, General Counsel, Senior Counsel, Paralegal, Auditor).</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Role: General Counsel</div>
      <div className="text-[10px] text-slate-400">Permissions: Full Read/Write across Matters, Contracts, Litigation, Spend, GRC & System Security</div>
    </div>
  </div>
);

const SessionsDeviceView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Active User Sessions & Device Security</h1>
      <p className="text-sm text-slate-300 mt-1">Active JWT sessions, IP address tracking, device fingerprinting, and session revocation.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Session ID: sess-891048 (Current Session)</div>
        <div className="text-[10px] text-slate-400">IP: 198.51.100.12 • Device: macOS Chrome • Created: 2026-07-25 18:30</div>
      </div>
      <button className="px-3 py-1 bg-rose-600/20 text-rose-400 font-bold border border-rose-500/30 rounded text-[11px]">Revoke</button>
    </div>
  </div>
);

const UserProfileView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">User Account & Security Preferences</h1>
      <p className="text-sm text-slate-300 mt-1">Personal profile info, MFA hardware key configuration, API personal access tokens.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 space-y-2">
      <div className="font-bold text-slate-100">Multi-Factor Authentication (MFA)</div>
      <div className="text-[10px] text-slate-400">Hardware Security Key (YubiKey 5 NFC) Enforced & Active</div>
    </div>
  </div>
);

const SecurityAuditView: React.FC = () => (
  <div className="space-y-6">
    <div className="p-6 rounded-2xl bg-slate-900 text-white border border-slate-800 shadow-xl">
      <h1 className="text-2xl font-bold tracking-tight">Security Audit Trail & SOC Event Ledger</h1>
      <p className="text-sm text-slate-300 mt-1">Immutable audit trail logging all access, data exports, permission changes, and login attempts.</p>
    </div>
    <div className="p-5 rounded-2xl glass-panel border border-slate-800 text-xs text-slate-300 flex justify-between items-center">
      <div>
        <div className="font-bold text-slate-100">Event #AUD-9912: Vault Document Export Verified</div>
        <div className="text-[10px] text-slate-400">User: jvance@acme.com • Target: MAT-2026-089 Vault • Result: SUCCESS</div>
      </div>
      <span className="px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">Audited</span>
    </div>
  </div>
);
