# Fontes técnicas do ApolloAI

O corpus combina uma síntese curada do NREL com 19 PDFs originais da IEA Photovoltaic Power Systems Programme (IEA PVPS), incorporados em 22 de agosto de 2026. O pipeline preserva nome do documento, página, trecho, seção inferida e URL institucional. Os arquivos originais permanecem em `data/solar/documentos/`.

## NREL

### New Best-Practices Guide for Photovoltaic System Operations and Maintenance

- Autor: H. Walker / National Renewable Energy Laboratory (NREL)
- Identificador: NREL/FS-7A40-68281
- URL: https://www.nrel.gov/docs/fy17osti/68281.pdf
- Artefato: `nrel_pv_om_best_practices_sintese.md`, síntese técnica curada e parafraseada.

## IEA PVPS — Task 13

Página institucional: https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-systems/

| Identificador | Tema | Arquivo |
|---|---|---|
| T13-27:2024 | Desempenho de geradores parcialmente sombreados | `IEA-PVPS-T13-27-2024.pdf` |
| T13-28:2024 | Boas práticas para KPIs técnicos e econômicos | `IEA-PVPS-T13-28-2024-REPORT-Technical-and-Economic-KPIs.pdf` |
| T13-29:2025 | Uso conjunto da terra, agricultura e agrivoltaicos | `IEA-PVPS-T13-29-2025-REPORT-Dual-Land-Use.pdf` |
| T13-29:2025 | Fact sheet sobre agrivoltaicos | `IEA-PVPS-T13-2026-FS-Agrivoltaics.pdf` |
| T13-30:2025 | Degradação e falhas em células e módulos | `IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf` |
| T13-30:2025 | Anexo de fichas de falhas fotovoltaicas | `IEA-PVPS-T13-30-2025-PVFS-ANNEX-Degradation-and-Failure.pdf` |
| T13-31:2025 | Plantas fotovoltaicas flutuantes | `IEA-PVPS-T13-31-2025-REPORT-Floating-PV-Plants.pdf` |
| T13-32:2025 | Otimização fotovoltaica para diferentes climas | `IEA-PVPS-T13-32-2025-REPORT-Climate-Optimisation-2025.pdf` |
| T13-32:2025 | Fact sheet de otimização climática | `FS-Climate-Optimisation-2025.pdf` |
| T13-33:2025 | Impactos operacionais e econômicos de clima extremo | `IEA-PVPS-T13-33-2025-REPORT-Extreme-Weather-Impacts.pdf` |
| T13-34:2026 | Digitalização e gêmeos digitais | `IEA-PVPS-T13-34-2026-REPORT-Digitalisation-Twins.pdf` |
| T13-35:2026 | Confiabilidade de sistemas PV+BESS | `IEA-PVPS-T13-35-2026-REPORT-PV-BESS-2026.pdf` |
| T13-36:2026 | Decisões de projetos: qualidade, desempenho e valor | `IEA-PVPS-T13-36-2026-REPORT-pv-project-decisions.pdf` |
| T13-37:2026 | Desempenho e confiabilidade de módulos de segunda vida | `IEA-PVPS-T13-37-2026-REPORT-Second-Life-PV.pdf` |
| T13-39:2026 | Otimização de sistemas PV para diferentes aplicações | `IEA-PVPS-T13-39-2026-REPORT-Optimisation-PV.pdf` |
| T13-40:2026 | Fotovoltaicos e segurança energética no Ártico | `IEA-PVPS-T13-40-2026-REPORT-Arctic-PV.pdf` |

## IEA PVPS — Task 12

Página institucional: https://iea-pvps.org/research-tasks/pv-sustainability/

| Tema | Arquivo |
|---|---|
| Diretrizes metodológicas de avaliação de ciclo de vida fotovoltaico | `IEA_Task12_LCA_Guidelines.pdf` |
| Análise ambiental e financeira preliminar do reuso de módulos | `IEA_PVPS_T12_Preliminary-EnvEcon-Analysis-of-module-reuse_2021_report.pdf` |
| Diretrizes metodológicas para análise de energia líquida | `IEA_PVPS_Task12_Methodological_Guidelines_NEA_2021_report.pdf` |

## Uso no RAG

Os PDFs são publicações técnicas, não substituem normas vigentes, manuais do fabricante, procedimentos internos, inspeções ou medições. O ApolloAI deve apresentar os trechos recuperados como evidência, preservar a página e não extrapolar procedimentos ou valores ausentes.
