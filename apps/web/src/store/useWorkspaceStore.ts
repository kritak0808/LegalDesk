import { create } from 'zustand';

export type WorkspaceViewMode = 
  | 'matters' 
  | 'contracts' 
  | 'litigation' 
  | 'governance' 
  | 'compliance'
  | 'organizations'
  | 'people'
  | 'teams'
  | 'roles'
  | 'sessions'
  | 'security'
  | 'profile'
  | 'settings'
  | 'matter_explorer'
  | 'contract_explorer'
  | 'clause_library'
  | 'template_studio'
  | 'renewal_center'
  | 'obligation_tracker'
  | 'ai_review_studio'
  | 'risk_explorer'
  | 'document_intelligence'
  | 'entity_explorer'
  | 'comparison_studio'
  | 'semantic_search'
  | 'knowledge_graph'
  | 'negotiation_assistant'
  | 'litigation_explorer'
  | 'evidence_studio'
  | 'discovery_center'
  | 'court_calendar'
  | 'settlement_workspace'
  | 'filing_explorer'
  | 'compliance_center'
  | 'policy_studio'
  | 'risk_register'
  | 'control_library'
  | 'incident_center'
  | 'vendor_compliance'
  | 'board_governance'
  | 'ai_governance'
  | 'legal_research_studio'
  | 'citation_explorer'
  | 'precedent_graph'
  | 'research_notebook'
  | 'memorandum_workspace'
  | 'ai_research_assistant'
  | 'jurisdiction_navigator'
  | 'workflow_studio'
  | 'process_explorer'
  | 'automation_center'
  | 'approval_center'
  | 'business_rule_builder'
  | 'execution_monitor'
  | 'workflow_analytics'
  | 'executive_command_center'
  | 'general_counsel_studio'
  | 'legal_spend_center'
  | 'predictive_intelligence'
  | 'board_reporting_center'
  | 'executive_copilot_studio'
  | 'executive_kpi_explorer'
  | 'integration_hub'
  | 'email_intelligence_center'
  | 'calendar_intelligence'
  | 'esignature_tracker'
  | 'api_management'
  | 'webhook_explorer'
  | 'collaboration_hub'
  | 'operations_center'
  | 'security_operations'
  | 'observability_studio'
  | 'job_monitoring'
  | 'backup_recovery'
  | 'feature_flag_studio'
  | 'ai_operations_center';

export type MatterDetailTab = 
  | 'overview' 
  | 'timeline' 
  | 'tasks' 
  | 'comments' 
  | 'participants' 
  | 'vault';

export type ContractDetailTab = 
  | 'overview' 
  | 'versions' 
  | 'parties' 
  | 'approvals' 
  | 'obligations' 
  | 'renewals';

export type CaseDetailTab = 
  | 'overview' 
  | 'timeline' 
  | 'evidence' 
  | 'discovery' 
  | 'hearings' 
  | 'filings' 
  | 'settlements';

interface WorkspaceState {
  activeView: WorkspaceViewMode;
  activeMatterTab: MatterDetailTab;
  activeContractTab: ContractDetailTab;
  activeCaseTab: CaseDetailTab;
  leftPanelOpen: boolean;
  rightCopilotOpen: boolean;
  commandPaletteOpen: boolean;
  activeMatterId: string | null;
  activeContractId: string | null;
  activeCaseId: string | null;
  activeDocumentId: string | null;
  
  setActiveView: (view: WorkspaceViewMode) => void;
  setActiveMatterTab: (tab: MatterDetailTab) => void;
  setActiveContractTab: (tab: ContractDetailTab) => void;
  setActiveCaseTab: (tab: CaseDetailTab) => void;
  toggleLeftPanel: () => void;
  toggleRightCopilot: () => void;
  setLeftPanelOpen: (open: boolean) => void;
  setRightCopilotOpen: (open: boolean) => void;
  setCommandPaletteOpen: (open: boolean) => void;
  setActiveMatter: (id: string | null) => void;
  setActiveContract: (id: string | null) => void;
  setActiveCase: (id: string | null) => void;
  setActiveDocument: (id: string | null) => void;
}

export const useWorkspaceStore = create<WorkspaceState>((set) => ({
  activeView: 'matters',
  activeMatterTab: 'overview',
  activeContractTab: 'overview',
  activeCaseTab: 'overview',
  leftPanelOpen: true,
  rightCopilotOpen: true,
  commandPaletteOpen: false,
  activeMatterId: 'MAT-2026-089',
  activeContractId: 'CTR-2026-089',
  activeCaseId: 'LIT-2026-089',
  activeDocumentId: 'DOC-MASTER-SERVICES-AGREEMENT.pdf',

  setActiveView: (view) => set({ activeView: view }),
  setActiveMatterTab: (tab) => set({ activeMatterTab: tab }),
  setActiveContractTab: (tab) => set({ activeContractTab: tab }),
  setActiveCaseTab: (tab) => set({ activeCaseTab: tab }),
  toggleLeftPanel: () => set((state) => ({ leftPanelOpen: !state.leftPanelOpen })),
  toggleRightCopilot: () => set((state) => ({ rightCopilotOpen: !state.rightCopilotOpen })),
  setLeftPanelOpen: (open) => set({ leftPanelOpen: open }),
  setRightCopilotOpen: (open) => set({ rightCopilotOpen: open }),
  setCommandPaletteOpen: (open) => set({ commandPaletteOpen: open }),
  setActiveMatter: (id) => set({ activeMatterId: id }),
  setActiveContract: (id) => set({ activeContractId: id }),
  setActiveCase: (id) => set({ activeCaseId: id }),
  setActiveDocument: (id) => set({ activeDocumentId: id }),
}));
