# IEA-PVPS-T13-30-2025-PVFS-ANNEX-Degradation-and-Failure

Fonte original: `IEA-PVPS-T13-30-2025-PVFS-ANNEX-Degradation-and-Failure.pdf`

## Página 1

Task 13  Reliability and Performance of Photovoltaic Systems

Photovoltaic Failure
Fact Sheets (PVFS)
2025
Report IEA-PVPS T13-30:2025
PVPS
Safety category Description
 Failure has no effect on safety.

Failure may cause a fire (f), electrical shock (e) or a physical dan-
ger (m) if a follow-up failure and/or a second failure occurs.

Failure can directly cause a fire (f), electrical shock (e) or a physi-
cal danger (m).

Performance category Description

The defect has no direct effect on performance.

The defect has a minor impact on performance.

The defect has a moderate impact on performance.

The defect has a high impact on performance.

The defect has a catastrophic impact on performance.

Task 13  Reliability and Performance of Photovoltaic Systems

## Página 2

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in  1974, is an autonomous  body within the framework of the Organization for E conomic
Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with a belief that the future of energy
security and sustainability starts with global collaboration. The programme is made up of 6.000 experts across government, academia, and
industry dedicated to advancing common research and the application of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCP’s within the IEA and was established in 1993. The mission
of the programme is to “enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone
in the transition to sustainable energy systems.” In order to achieve this, the Programme’s participants have undertaken a v ariety of joint
research projects in PV power systems applications. The overall programme is headed by an Executive Committee, comprised of one dele-
gate from each country or organisation member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.
The IEA PVPS participating countries are Australia, Austria, Belgium, Canada, China, Denmark, Finland, France, Germany, India,
Israel, Italy, Japan, Korea, Malaysia, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain, Sweden, Switzerland, Thailand,
Türkiye, and the United States of America. The European Commission, Solar Energy Research Institute of Singapore and Solar Power
Europe are also members.
Visit us at: www.iea-pvps.org
What is IEA PVPS Task 13?
Within the framework of IEA PVPS, Task 13 aims to provide support to market actors working to improve the operation, the reliability and the
quality of PV components and systems. Operational data from PV systems in different climate zones compiled within t he project will help
provide the basis for estimates of the current situation regarding PV reliability and performance.
The general setting of Task 13 provides a common platform to summarize and report on technical aspects affecting the quality, performance,
reliability and lifetime of PV systems in a wide variety of environments and applications. By working together across national boundaries we
can all take advantage of research and experience from each member country and combine and integrate this knowledge into valu able
summaries of best practices and methods for ensuring PV systems perform at their optimum and continue  to provide competitive return on
investment.
Task 13 has so far managed to create the right framework for the calculations of various parameters that can give an indication of the quality
of PV components and systems. The framework is now there and can be used by the industry who has expressed appreciation towards the
results included in the high-quality reports.
The IEA PVPS countries participating in Task 13 are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany,
Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand, the United States of America, and the So lar Energy
Research Institute of Singapore.
DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and publica-
tions of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual  member countries.
COVER PICTURE
Infrared image of an energised module string at night. One module has a not connected bypass diode. Thanks to photovoltaikbue ro Ternus & Diehl GbR for the
permission to use the image.
ISBN 978-3-907281-71-0: Task 13 Report: PV Failure Fact Sheets (PVFS) – Review 2025

## Página 3

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
3
AUTHORS
Main Contributors to PVFS Review 2025
Gabi Friesen, SUPSI, Switzerland
Marc Köntges, ISFH, Germany
Jay Lin, PV Guider
Gernot Oreski, PCCL, Austria
Gabriele C. Eder, OFI, Austria
Peter Hacke, NREL, USA
Paul Gebhardt, Fraunhofer ISE, Germany
Ebra Özkalay, SUPSI, Switzerland
Christof Bucher, BFH, Switzerland
Mauro Caccivio, SUPSI, Switzerland
Romain Couderc, CEA, France
Sergiu Viorel Spataru, DTU, Denmark
Editors
Gabi Friesen, SUPSI, Switzerland
Jay Lin, PV Guider
Ulrike Jahn, Fraunhofer CSP, Germany

## Página 4

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
4
TABLE OF CONTENTS
Acknowledgements ................................ ................................ ................................ .. 5
Introduction ................................ ................................ ................................ ........ 6
1.1 PVFS structure ................................ ................................ ......................... 6
1.2 Example PVFS: Front delamination ................................ .......................... 9
1.3 List of PVFS ................................ ................................ ........................... 12
References ................................ ................................ ................................ ............. 13
ANNEX (PV FAILURE FACT SHEETS) ................................ ................................ . 15

## Página 5

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
5
ACKNOWLEDGEMENTS
This report is supported by the German Federal Ministry for Economic Affairs and Climate
Action (BMWK) under contract no. 03EE1120A, 03EE1120B and 03EE1120C, the Swiss Fed-
eral Office of Energy (SFOE) under the contract no. SI/502398 -01, the Austrian Federal Min-
istry for Climate Action, Environment, Energy and Mobility (BMK), the Danish Energy Technol-
ogy Development and Demonstration Programme (EUDP), project number 134 -22016, "IEA
PVPS Task13 - Reliability and performance of photovoltaic systems”, and the A ustrian Re-
search Agency (FFG) under contract no. FO999908094_05102023_160512119.
This work was authored in part by the National Renewable Energy Laboratory, operated by
Alliance for Sustainable Energy, LLC, for the U.S. Department of Energy (DOE) under Contract
No. DE-AC36-08GO28308 in the project 38263 “R&D to Ensure a Scientific Basi s of Qualifi-
cation Tests and Standards,” funded by the U.S. Department of Energy, Office of Energy Effi-
ciency and Renewable Energy, Solar Energy Technologies Office. The views expressed in the
article do not necessarily represent the views of the DOE or the U.S. Government.

## Página 6

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025

6
 INTRODUCTION
The photovoltaic failure fact sheets (PVFS) summarise some of the most important aspects of
single failures. The target audience of these PVFSs are PV planners, installers, investors, in-
dependent experts and insurance companies, and anyone interested in a brief description  of
failures with examples, an estimation of risks and suggestions of how to intervene or prevent
these failures.
The failure sheets are not intended to provide an in-depth exploration of the theoretical back-
ground of PV failures and their detection. Instead, they aim to summarize the key points out-
lined in the various IEA PVPS Task 13 technical reports [Herz22, Köntges14, Köntges16, Könt-
ges17, Schill21, Jahn18, Herrmann21] and reference documents [Sinclair17, Packard12,
Eder19, Moser17, Yang19, Walsh20, Petter11, India18, India13, PVSurvey19, DuPont20] that
were used to prepare the PVFSs listed in  Table 2. These failure sheets are specific to the
component where the failure occurs.
The PVFS have been reviewed in 2024 to include latest PV module failures observed in the
field and discussed in more detail in a technical IEA PVPS Task 13 report [Köntges25].
1.1 PVFS structure
The format of the PVFS is based on the failure description presented within the H2020 Solar
Bankability project [SolBank20]. A rating system for the estimation of the severity of a failure
is used here which simplifies the approach proposed within the IEA PVPS Task 13 [Köntges14]
by implementing the rating system proposed by the Sinclairs [Sinclair17]. The correlation be-
tween the different failures is highlighted in the text by using bold characters. Each PVFS is
structured into 1 to 3 pages. The first page is a descriptive page, whereas the remaining pages
contain examples composed of a picture, a legend and an estimation about its severity. The
first page is structured as follows:
Component
The PV system components are divided into:
(1) PV module (including junction box)
(2) Cables and interconnectors (at module, string and combiner box level)
(3) Mounting (structure, clamps and screws)
(4) Inverter
Defect
Short name describing the failure/defect.
Appearance
Description of how the defect looks like.
Detection
Description of methods which can be used to detect the failure. Detection methods in brackets
lists secondary methods, which do not detect the failure with absolute certainty or which can
be used in addition to other methods. Following abbreviations are used:

## Página 7

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
7
Table 1: Abbreviations of detection methods.
Abbreviation Detection methods
VI Visual inspection
IRT Infrared thermography
EL Electroluminescence
IV Daylight I-V measurement
UV UV fluorescence
STM Signal transmission method
MON Data monitoring
dIV Dark I-V measurement
BYT* Bypass diode testing
VOC Voc measurement
INS Insulation testing
*useful background information
https://photovoltaikbuero.de/en/pv-know-how-blog-en/checking-bypass-diodes-on-solar-panels-part-1/
https://www.hioki.com/euro-en/products/pv/solar-panel/id_6647
https://emazys.com/pv-module-test/
Origin
Description of the failure and its main causes and origin (1. Material and production, 2.
Transport and installation, 3. Operation and maintenance).
Impact
Description of the impact on the safety, performance and reliability of the component and sys-
tem and its severity. For every failure, a range of possible ratings is given, one for the safety
and one for the performance.
A failure is defined as a safety failure when it endangers somebody who is applying or working
with PV modules or simply passing the PV modules. Three categories are defined in Figure 1.
Safety category Description
 Failure has no effect on safety.

Failure may cause a fire (f), electrical shock (e) or a physical dan-
ger (m) if a follow-up failure and/or a second failure occurs.

Failure can directly cause a fire (f), electrical shock (e) or a physi-
cal danger (m).
Figure 1: Safety categories.

## Página 8

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025

8
A failure is defined as a performance failure when it impacts the performance and/or reliability
of a system. Five categories are defined in Figure 2. They go from 1 (low severity) to 5 (high
severity).

Performance category Description

The defect has no direct effect on performance.

The defect has a minor impact on performance.

The defect has a moderate impact on performance.

The defect has a high impact on performance.

The defect has a catastrophic impact on performance.
Figure 2: Performance categories.
For each category, the expected loss is estimated on the component level and if no mitigation
measure is implemented. It can range from no power degradation (0%), over power degrada-
tion below detection limit (< 2-3%), power degradation within warranty (<0.7 -1%/year) and
power degradation out warranty (>0.7-1%/year) to catastrophic power degradation (>3%/year).
Mitigation
Description of the corrective actions to be done on a short and medium term when detecting a
failure and preventive actions to be implemented to avoid the failure from the beginning. Pre-
ventive actions are separated into recommended actions, representing t he minimum require-
ment for small residential systems and optional actions for large scale systems.
The general rule for intervention in case of a failure is: All components with a direct safety risk
or a performance severity of 5, highlighted in red, should be replaced or repaired. Regular
inspections should be performed to monitor the status of the not replaced or repaired compo-
nents.

## Página 9

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
9
1.2 Example PVFS: Front delamination
The delamination of the encapsulant FS1-3: Front delamination is used here as an example
to explain the FS structure and rating system.

Figure 3: First page of PVFS example with general information.

## Página 10

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025

10

Figure 4: Remaining pages of a PVFS  contain examples composed of a picture,  a
legend, and an estimation about its severity.

The first section of the sheet describes the appearance or how to recognise a specific failure
and which detection methods are available. Delamination is generally easily detectable by
visual inspection (VI) of the modules from the front. Insulation measurements (INS) can give a
hint of a severe delamination, but it is not the first method to detect an early delaminati on,
reason why it is put in brackets.
The second section describes the origin or in which phase of the lifetime of a PV system the
failure occurs and what the main causes are. Delamination problems have its origin mainly in
the quality of the raw material, the manufacturing process and/or the environmental factors to
which the modu les are exposed during its operational lifetime. Transport and installation do
not generate any delamination problems.

The third section describes the impact the failure has on the safety and performance of the
component and PV system. Below the general description the severity rating according to Fi-
gure 1 and Figure 2 is given. The severity rating in the first page gives the full range of possible
ratings observable in the field and how the failure can evolve over the whole lifetime of a PV
system. The rating in the examples gives instead a snapshot of the gravity of the failure for a
specific case at a certain time. The pictures are taken from literature or case studies and give
only a partial picture of the situation and are used to explain the potential levels of impact here.
The delamination of the potting material does not automatically pose a safety risk. It is there-
fore often rated as not critical (see example 1.3.1 -1.3.7, 1.3.10 and 13.11  in Annex 1 ), but
depending on the propagation of the failure it can develop into a more severe safety failure.
When creating a continuous path between the electric circuit and the edge of the module (see

## Página 11

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
11
example 1.3.13-1.3.15), delamination can lead to electric leakage currents with a direct risk of
electrical shock or the risk can occur later, due to the progress of the delamination and/or the
ingress of moisture. This is particularly the case when the original delamination is close to the
edge of the module or the junction box, or if it is going over a very extended area (see example
1.3.8-1.3.12). The performance loss risk for modules with delamination problems ranges
from 1 to 5. Very small delamination  areas on top of a cell or outside the cell area and not
combined with other failures, are classified as having no impact (1) or a minor power loss
typically below the detection limit (2), if the failure is not increasing over time (see example
1.3.1-1.3.4, 1.3.8, 1.3.10 and 1.3.11). The severity is in the range of (2-4) when the delamina-
tion area is getting larger (see example 1.3.7 and 1.3.9) or if it is occurring in combination with
follow-up failures like moisture ingress (see example 1.3.14) or an insu lation failure (see ex-
ample 1.3.13). It increases also when occurring in combination with a second failure like dis-
coloration (yellowing or browning) of the encapsulant or backsheet (see example 1.3.6, 1.3.7,
1.3.13), or cell cracking (see example 1.3.5). A catastrophic performance loss of (5) is reached
when the cell mismatch is so large that one or more bypass diodes could be activated (s ee
example 1.3.13 and 1.3.14).
The last section describes the mitigation measures. In case of delamination, all modules that
no longer guarantee the electrical safety or insulation resistance or have an active bypass
diode, have to be replaced. Not replaced modules with minor delamination have to be moni-
tored by regular visual inspections and ground fault detection. Basic preventive measures con-
sist in selecting certified and tested products only. In case of large-scale systems regular sys-
tem inspection is recommended.

## Página 12

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025

12
1.3 List of PVFS
Table 2: List of PV Failure Fact Sheets.
No Component Failure name
1-1 PV module Cell cracks
1-2 PV module Discolouration of encapsulant or backsheet
1-3 PV module Front delamination
1-4 PV module Backsheet delamination
1-5 PV module Backsheet cracking
1-6 PV module Backsheet chalking (whitening)
1-7 PV module Burn marks
1-8 PV module Glass breakage
1-9 PV module Cell interconnection failure
1-10 PV module Potential induced degradation
1-11 PV module Metallisation discolouration/corrosion
1-12 PV module Glass corrosion or abrasion
1-13 PV module Defect or detached junction box
1-14 PV module Junction box interconnection failure
1-15 PV module Missing or insufficient bypass diode protection
1-16 PV module Not conform power rating
1-17 PV module Light induced degradation in c-Si modules
1-18 PV module Insulation failure
1-19 PV module Hot spot (thermal patterns)
1-20 PV module Soiling
2-1 Cable and Interconnector DC connector mismatch
2-2 Cable and Interconnector Defect DC connector/cable
2-3 Cable and Interconnector Insulation failure
2-4 Cable and Interconnector Thermal damage in combiner box
3-1 Mounting Bad module clamping
3-2 Mounting Inappropriate/defect mounting structure
3-3 Mounting Module shading
4-1 Inverter Overheating (temperature derating)
4-2 Inverter Incorrect installation
4-3 Inverter Complete failure (not operating)
The list does not pretend to be exhaustive or updated. The complete list with all PVFS

## Página 13

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
13
REFERENCES
[DuPont20]  DuPont global PV reliability, 2020 Field analysis, Dupont,
https://www.dupont.com/news/20200512-2020-global-pv-reliability-report.html, last a ccess
Nov 2024.
[Eder19]  G.C. Eder et al., “Error analysis of aged modules with cracked polyamide back-
sheets,” Solar Energy Materials & Solar Cells, Vol. 203, December 2019.
[Herrmann21]  W. Herrmann, G. C. Eder, B. Farnung, G. Friesen, M. Köntges, B. Kubicek, O.
Kunz, H. Liu, D. Parlevliet, I. Tsanakas and J. Vedde, Qualification of Photovoltaic (PV) Power
Plants using Mobile Test Equipment, Report IEA -PVPS T13-24: ISBN 978 -3-907281-12-3,
2021.
[Herz22]  M. Herz, G. Friesen, U. Jahn, M. Köntges, S. Lindig, D. Moser, IEA PVPS Task
13: Performance, Operation and Reliability of Photovoltaic Systems - Quantification of Tech-
nical Risks in PV Power systems, Report IEA -PVPS T13-23:2022: ISBN 978-3-907281-11-6,
2022.
[India13]  Y.R. Golive et al., “All-India India Survey of Photovoltaic Module Degradation:
2013,” Mumbai, India, 2013.
[India18]  R. Dubey et al., “All-India India Survey of Photovoltaic Module Degradation:
2013,” Mumbai, India, 2018.
[Jahn18]  U. Jahn, M. Herz, M. Köntges, D. Parlevliet, M. Paggi, I. Tsanakas, J. S. Stein,
K. A. Berger, S. Ranti, R. H. French, M. Richter and T. Tanahashi, "Review on Infrared and
Electroluminescence Imaging for PV Field Applications", Report IEA-PVPS T13-10:2018:
ISBN 978-3-906042-53-4, 2018.
[Köntges14]  M. Köntges, S. Kurtz, C. Packard, U. Jahn, K. A. Berger, K. Kato, T. Friesen, H.
Liu, M. Van Iseghem, J. Wohlgemuth, D. Miller, M. Kempe, P. Hacke, F. Reil, N. Bogdanski,
W. Herrmann, C. Buerhop Lutz and G. Friesen, Review of Failures of Photo voltaic Modules,
Report IEA-PVPS T13-01: ISBN 978-3-906042-16-9, 2014.
[Köntges16]  M. Köntges et al., “Mean Degradation rates in PV systems for various kinds of
PV module failures,” in Proc. 32nd Eur. Photovolt. Sol. Energy Conf. (EUPVSEC), 2016, pp.
1435 - 1443.
[Köntges17]  M. Köntges, G. Oreski, U. Jahn, M. Herz, P. Hacke, K. A. Weiss, G. Razongles,
M. Paggi, D. Parlevliet, T. Tanahashi and R. H. French, Assessment of Photovoltaic Module
Failures in the Field, Report IEA-PVPS T13-09: ISBN 978-3-906042-54-1, 2017.
[Köntges25] M. Köntges, J. Lin, A. Virtuani, G. Eder, J. Zhu, G. Oreski, P. Hacke, J.S. Stein,
L. Bruckman, P. Gebhardt, D. Barrit, M. Rasmussen, I. Martin, K.O. Davis, G. Cattaneo, B.
Hoex, Z. Hameiri, E. Özkalay, “Degradation and Failure Modes in Pholtovoltaic Cell and Mod-
ule Technologies”, Report IEA-PVPS T13-29:2025: ISBN  978-3-907281-71-0, 2025.
[Mahmood2024] A. Mahmood, R. Santamaria, T.r Kari, P.B. Poulsen, S.V. Spataru, “Di-
agnosing Potential Induced Degradation in Crystalline Silicon Photovoltaic Modules”, in Proc.
41st Eur. Photovolt. Sol. Energy Conf. (EUPVSEC), 2024.
[Moser17]  D. Moser et al., “Report on technical risks in PV project development and PV
plant operation,” https://www.tuv.com/content-media-files/master-

## Página 14

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025

14
content/services/products/p06-solar/solar-downloadpage/solar-bankability_d1.1_d2.1_tech-
nical-risks-in-pv-projects.pdf, last access Nov 2024.
[Schill21]  C. Schill, D. Parlevliet, A. Anderson, B. Stridh, L. Burnham, C. Baldus-Jeursen,
L. Micheli, E. Urrejola, E. Whitney and G. Mathiak, Soiling Losses – Impact on the Performance
of Photovoltaic Power Plants, Report IEA-PVPS T13-21: ISBN 978-3-907281-09-3, 2021.
[Sinclair17]  K. Sinclair, M. Sinclair, "Silicon solar module visual inspection guide: Catalogue
of Defects to be used as a Screening Tool", https://www.engineeringforchange.org/wp -con-
tent/uploads/2017/09/Solar-PV-Product-Visual-Inspection-Guide.pdf. last access Nov 2024.
[SolBank20]  "Solar Bankability project website," accessed: 2020 -04-28. [Online]. Available:
http://www.solarbankability.org/home.html.
[Packard12]  C. Packard, J. Wohlgemuth, S. Kurtz, “Development of a Visual Inspection Data
Collection Tool for Evaluation of Fielded PV Module Condition,” Technical Report NREL/TP -
5200-56154 August 2012, https://www.nrel.gov/docs/fy12osti/56154.pdf.
[Petter11]  K. Petter et al., “Long Term Stability of Solar Modules Made from Compensated
SoG-Si or UMG-Si,” Energy Procedia, Volume 8, page 365-370, 2011.
[PVFS21]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-
photovoltaic-systems/documents/ follow link to "PV Failure Fact Sheets", last access Aug
2021.
[PVSurvey19]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-
photovoltaic-systems/documents/, follow link “Explanation of the PV -System Survey sheet”
Version:21 October 2019, last access 04 March 2021.
[Walsh20]  T.M. Walsh et al., “Singapore Modules - Optimised PV Modules for the Tropics,”
Energy Procedia, Volume 15, page 388-395, 2020.
[Yang19]  H.E. Yang, R.H. French and L.S. Bruckman, “Durability and Reliability of Poly-
mers and Other Materials in Photovoltaic Modules,” ISBN 978-0-12-811545-9, 2019.

## Página 15

Task 13 Reliability and Performance of Photovoltaic Systems – PV Failure Fact Sheets (PVFS) – Review 2025
15
ANNEX (PV FAILURE FACT SHEETS)

## Página 16

16
Component
Defect
Module
Cell cracks PVFS 1-1vs.02
Appearance Cell cracks are cracks in the silicon substrate of the photovoltaic cells. Most of the cell cracks
cannot be seen by the naked eye. Only large cracks or where the backsheet is visible through
the cracks can be seen. Cell cracks can be easily detected throu gh imaging techniques like
electroluminescence or UV fluorescence. Cell cracks can have different lengths and orientations
(crack patterns). Small cell cracks (micro-cracks) become visible by eye when they form snail
tracks or when photobleaching or delamination takes place along the cracks. A snail track is
a discoloration of the silver paste of the front metallisation of solar cells which occurs typically 3
months to 1 year after installation of the PV modules. Affected metal fingers on cells may be
silver, yellow or brown in appearance, this effect can also be seen on cell edges. Photobleaching
is a counteracting effect to the yellowing of the encapsulant and it occurs along the cracks and
the borders of the cells. Sometimes delamination along cracks is visible as small bubbles along
the cell cracks.
Detection EL, UV (IRT, VI, IV)
Origin Cell cracks can have origin in all lifetime phases of a PV module: production,  transport, instal-
lation and operation. In production, cell cracks can occur during wafer, cell and module manu-
facturing. Especially the stringing and soldering process of the solar cells can damage the cells.
Furthermore the cutting of full cells to half or multiple cut cells can lead to cracking at the cutting
cell edge. After production, major sources for cell cracks are the packaging and transport of the
modules, and the installation. After installation, external forces like hail, heavy snow weight or
strong wind may result in cell cracks.  Once cell cracks are present, further mechanical and
thermomechanical stresses can lead to the propagation of the cracks into longer and wider
cracks. Some crack patterns can give indications on the origin of the failure, but the final cause
of cell break age is not always easy to identify. A repetitive crack pattern can be for example
caused by a production failure, whereas PV modules showing dendritic crack patterns have
been probably exposed to heavy mechanical loads. Snail tracks can be found in a great variety
of solar modules, but not in all. The combination of different materials (encapsulant and back
sheets) with UV radiation and temperature plays an important role in the creation of snail tracks.
Production  Installation Operation
Impact Cell cracking does not necessarily lead to a failure of the module. The presence of a crack of
any size that does not, or likely will not through its propagation, remove more than 10% of that
cell’s area from the electrical circuit can be considered to have limited to no impact on the per-
formance. Even if each cell in a 60 full-cell module is cracked, but do not lead to a separated
cell area, the power loss of the module is typically below 2.5 % of the nominal power. Compared
to former ribbon based modules with 2 to 4 cell interconnect ribbons, more recent multi wire/bus-
bar solar modules demonstrates much lower power losses due to cell cracks. For multi wire
PERC modules 0.2% power loss per dendritic like cracked half-cell is typical. In cold and snow
climate zones cell cracks seem to have a more pronounced impact. Here relatively high mean
degradation rates of up to 7%/y can be found  for full cell modules . Besides the risk of power
loss there is a risk of hot spots and burn marks due to inactive cell parts.  Snail tracks are
reported to have no influence on the performance of the PV module.
 Safety:   Performance:
Mitigation

Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules.
Adequate transport proce-
dures, installation and clean-
ing by trained personal, in
case of higher snow or hail
risk use of therefore certified
modules. Multiwire modules
mitigate degradation risk.
Request EL pictures from pro-
duction, pre-shipment or ware-
house inspection, EL images
with mobile laboratory before or
during installation, regular EL
inspection or after sever
weather conditions.

## Página 17

17
EXAMPLES (page1) PVFS 1-1vs.02
Examples
1-3

Cell chipping. A very small region
is missing from the edge of the
cell, but does not enter metal-
lized region [Köntges14].
Large crack at cell corner visible
by eye - small portion of the cell
(<10%) is no longer electrically
connected [Köntges14].
Cell crack with snail track. No iso-
lation of any cell part. The propa-
gation c ould isolate a cell area
>10% [Köntges14].
Severity
Examples
4-6

Cell cracks visible by the photo -
bleaching effect. This may not be
mistaken for snail tracks [Könt-
ges14].
Two cell cracks with extensive
delamination, EVA browning and
photo bleaching [Yang19].
EL image of 2 cell cracks which
isolates more than 10% of the cell
area [ By the courtesy of TUV
Rheinland].
Severity
Examples
7-9

Snail track example [Yang19]. Snail track example [Yang19]. EL of cell cracks w ith snail tracks
[Köntges14].
Severity

## Página 18

18
EXAMPLES (page2) PVFS 1-1vs.02
Examples
10-12

Zoom of snail track with delami-
nation [Yang19].
Zoom of snail track with browned
fingers [Sinclair17].
Zoom of snail track with delamina-
tion [ By the courtesy of SUPSI
PVLab].
Severity
Examples
13-15

Cell crack with EVA delamination
[By the courtesy of TUV Rhein-
land]. (see also PVFS 1-3)
Typical EL picture of a cell crack
caused by hail  [By the courtesy
of TUV Rheinland].
Repetitive crack pattern due to im-
pact of soldering machine [ By the
courtesy of SUPSI PVLab].
Severity
Examples
16-17

Typical EL picture of cell cracks caused by a heavy homoge-
neous mechanical load (X -crack pattern) also without glass
breakage [Köntges14].
Cell cracks in a module with shingled so-
lar cells [By the courtesy of Aerial Inspec-
tion].
Severity

## Página 19

19
EXAMPLES (page3) PVFS 1-1vs.02
Example
18

Manufacturer related cell cracks (a) in half cut cells and they grew into larger ones after transportation
with inactive cell areas below 5% per cell (B) [Köntges24] .
Severity

## Página 20

20
Component
Defect
Module
Discolouration of encapsulant or backsheet PVFS 1-2vs.02
Appearance The degradation of the encapsulation or backsheet materials is becoming visible as a light
yellow to dark brown discolouration. Colour can be next to or above the cells, along the bus-
bars or cell interconnects or on the back or front side of the backsheet. Often discolouration is
inhomogeneous and follows spatial patterns depending on the type of module construction.
Typically, for glass /backsheet modules the encapsulant discolouration occurs in the central
region of the cells with wide clear encapsulant areas, or “frames” around the cell edges. Dis-
colouration of the backsheet can be observed at the module edges of between  neighbouring
solar cells. For glass/glass module constructions the encapsulant discolouration is mostly spa-
tially uniform but can also show patterns of clearer areas over some cells. In glass/backsheet
modules the location of these patterns generally correlates with cell cracks. In some cases,
the discolouration is more pronounced in one or more cells of the module.
Detection VI, (IV, IRT)
Origin In the past, yellowing or browning was mostly associated with the degradation of the mostly
used encapsulant ethylene vinyl acetate (EVA) but this problem was greatly solved by im-
proved stabilisation of the polymer with additives, including UV absorbers an d thermal stabi-
lizers. If the choice of additives and/or their concentrations are inadequate, or the lamination
process is inadequate or incomplete, the encapsulation material may discolour over time. The
root cause of backsheet discolouration is either degradation of the cell side layer of the back-
sheet or caused by reactions of inter -diffusing additives at the encapsulant backsheet inter-
face. The patterns of discolouration observed in the field can be very complex because of the
diffusion of oxygen or the products of reaction, such as acetic acid, generated when heat and
UV light interact with EVA. The presence of oxygen leads to the so -called photobleaching
effect which creates a ring of transparent EVA around the perimeter of a cell or a cell crack.
The case of single cells which are far darker than the adjacent cells, implies that the most
discoloured cell was at higher temperature than the surrounding cells, perhaps because of
differences between the cells or the cell being located above the junction box.
Production  Installation Operation
Impact Discoloration is a sign that the polymeric compounds within the module started to degrade.
This type of degradation is predominantly considered to be first an aesthetic issue before a
decrease of module current and power production is detected. Typically, mean yearly degra-
dation rates due to yellowing are about 0.5%/a and may reach up to 1%/a in hot and humid or
moderate climates. While it is uncommon for EVA discolouration to induce other failures within
the cell, it may correlate to: high temperatures in the field, the generation of acetic acid and
concomitant corrosion and embrittlement. Unless discolouration is very severe and localized
at a single cell, where it could cause a substring bypass-diode to turn on, the discolouration of
EVA does not present any direct safety issues. More critical is the discolouration of UV sensi-
tive backsheets that in dependence of the used backsheet materials can be a precursor to  a
loss of mechanical properties (elastic behaviour) and cracking of backsheet due to thermo-
mechanical stresses.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules.
Check validity of IEC 61215
certification and BOM.
Regular system inspections
For areas with harsh climate,
request modules pass higher
test standards, like double or
triple IEC 61215 test condi-
tion.

## Página 21

21
EXAMPLES (page1) PVFS 1-2vs.02
Examples
1-3

Slightly browned EVA in the cen-
tre of the cell with photobleaching
at the edges [Köntges14].
Slightly browned EVA in the cen-
tre of the cell with photobleaching
at the edges [India18].
Yellowed backsheet from the in-
side [Sinclair17].
Severity
Examples
4-6

Dark discolouration at cell edges,
between cells and over gridlines
and busbars [Sinclair17].
Dark di scolouration over metali-
zation [Sinclair17].
Backsheet air side yellowing
[Sinclair17].
Severity
Examples
7-9

Single cell browned much faster
than the others due to local heat-
ing [Köntges14].
Yellowed backsheet from the in-
side [By the courtesy of PCLL].
Yellowing of the backsheet in
combination with cr acked back-
sheet caused by hot cell
[Eder19].
Severity

## Página 22

22
Component
Defect
Module
Front delamination PVFS 1-3vs.01
Appearance Any local separation of the layers between (i ) the front glass and the encapsulant or (ii) the
cell and the encapsulant, visible as bubbles or as bright, milky area/s. It may appear continu-
ous or in spots. The position and size of the delamination or bubble depends on the origin and
progress of the failure.
Detection VI, (INS)
Origin The adhesion between the glass, encapsulant, active layers, and back layers can be compro-
mised for many reasons. Typically, it is caused by the manufacturing process (e.g. poor cross
linking of EVA, too short lamination times, too high pressure in the laminator, contaminations,
improper cleaning of the glass, incompatibility of EVA with soldering flux, inadequate storage
of the raw material) or environmental factors (e.g. thermal stresses, external me chanical
stresses, UV).  Delamination is generally follow ed by moisture ingress  and corrosion. It is
therefore more frequent and severe under hot and humid conditions.
Production  Installation Operation
Impact Delamination or bubbles do not automatically pose a safety issue, but they can result in re-
duced insulation of the component and increased safety risk when they form a continuous
path between electric circuit and the edge due to possible water ingress. Moisture in the mod-
ule will decrease performance due to an increase of series resistance, affect long term rel ia-
bility and in some cases also the structural integrity of the module. Moreover, delamination at
interfaces in the optical path will result in additional optical reflection and subsequent decrease
in current. This can be the origin of current mismatch. If the mismatch is significant, it will
trigger the bypass diode and cause further power loss. The inverter might also shut down due
to leakage current’s leading to a further performance loss. Manufacturing related delamination
issues often affects a relevant percentage of modules within the same production batch and
consequentially has a big impact on system performance.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules. In case of in-
dividual module testing all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.
Check validity of IEC 61215
certification and BOM, ground
fault detection by inverter or
other devices at all time.
Extended testing (e.g. damp
heat), pre -shipment inspec-
tions (e.g. cross linking level
of EVA) regular visual system
inspections.

## Página 23

23
EXAMPLES (page1) PVFS 1-3vs.01
Examples
1-3

Encapsulant delamination in un-
critical position [ By the courtesy
of SUPSI PVLab].
Encapsulant delamination from
cell caused by production pro-
cess [By the courtesy of SUPSI
PVLab].
Encapsulant delamination from
cell along grid fingers and bus bar
[Packard12].
Severity
Examples
4-6

Encapsulant delamination from
glass (spotted due to glass tex-
ture) along the bus bars [Pack-
ard12].
Encapsulant delamination along
a cell crack [Köntges16]. (see
also PVFS 1-1)
Encapsulant delamination near
cell edges in combination with cell
browning [Packard12].
Severity
Examples
7-9

Delamination in front of cell in the
centre of the module [Moser17].
(see also FS 1-2)
Delamination at module insert
connections of a glass/glass
module (junction box) [By the
courtesy of SUPSI PVLab].
Delamination at cell edges [Könt-
ges14].
Severity

## Página 24

24
EXAMPLES (page2) PVFS 1-3vs.01
Examples
10-12

Encapsulant delamination at bor-
ders [Sinclair17].

Encapsulant delamination along
a bus -bar in a cell close to the
module edge [Moser17].
Encapsulant delamination of from
glass (spotted due to glass tex-
ture) at the edge of the cell [Sin-
clair17].
Severity
Examples
13-15

Delamination creating a continu-
ous path between electric circuit
and the edge [Moser17].
Delamination with corrosion
[Köntges17]. (see also FS1-11)
Delamination caused by detach-
ment of backsheet with exposure
of encapsulant from the back [ By
the courtesy of SUPSI PVLab].
Severity

## Página 25

25
Component
Defect
Module
Backsheet delamination PVFS 1-4vs.01
Appearance Any local separation of the polymeric back sheet layers leading to an air gap between the
backsheet and the rest of the module, or within the multilayer backsheet (=internal delamina-
tion). The backsheet may appear wavy, with locally limited bumps, bubbles or ripples. In the
worst case, one or more layers may peel off. The position and extent of the delamination will
depend on the cause and progression of the failure.
Detection VI, (INS)
Origin There are many different forms and compositions of polymeric multilayer backsheets on the
market. With laminated backsheets (polymeric layers adhered to each other by a thin adhesive
layer) internal delamination can appear: the multiple layers may delamina te upon adhesive
degradation, which may lead to local delamination of two subsequent layers or a peel -off of
one or more layers. Co-extruded backsheet are prone to internal lamination. Delamination of
the backsheet from the encapsulant can appear with all types of backsheets and originates
from a lack of adhesion between the backsheet and the encapsulation. The major drivers for
the delamination of or within the the backsheet are (i) thermo -mechanical stress originating
from differing CTE of the individual polymeric layers, (ii) chemical reactions at the interfaces
(material incompatibility) or deteriorated interfacial bonding as a result of the attack from heat,
UV and moisture or (iii) external mechanical stress applied on the module. Therefore, it is more
frequent and severe under hot and humid conditions. Delamination can be also caused by an
insufficient lamination process e.g. too short lamination times.
Production  Installation Operation
Impact If delamination occurs forming bubbles in a central, open area of the back, it will not present
an immediate safety issue. That area would likely operate at slightly higher temperatures as
the heat conduction/dissipation through the backsheet is disturbed. But as long as the bubble
is not further mechanically cracked or expanded, the performance and safety concerns are
minimal. However, if delamination of the backsheet occurs near a junction box, or near the
edge of a module there would be more serious safety concerns. Delamination at the edge may
provide a direct pathway for liquid water to enter the module during a rainstorm, or in response
to the presence of dew. That can provide a direct electrical pathway to ground creating a very
serious safety concern. Similarly, delamination near a junction box can cause its loosening,
putting mechanical stress on live components with the danger of breakage. A break might
cause a connection failure to a bypass diode and possibly result in an unmitigated arc at full
system voltage. In multilayer backsheets the severity depends also on which layer is affected.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules. In case of in-
dividual module testing all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.
Check validity of IEC 61215
certification and BOM.
Ground fault detection by in-
verter or other devices at all
time.
Regular system inspections.

## Página 26

26
EXAMPLES (page1) PVFS 1-4vs.01
Examples
1-3

Multiple bubbles in the centre
and edge of the backsheet [Könt-
ges16].
Blisters because of vapour bar-
rier, such as aluminium foil [Könt-
ges17].
Big central bubble + wavy delam-
ination [Köntges14].
Severity
Examples
4-5

Backsheet delamination with di-
rect exposure of encapsulant [By
the courtesy of SUPSI PVLab].
Delamination of top layer without
exposure of encapsulant [By the
courtesy of SUPSI PVLab].

Severity

## Página 27

27
Component
Defect
Module
Backsheet cracking PVFS 1-5vs.02
Appearance Any damage of the backsheet (surface or whole stack) that is visible as crack, burst or scratch.
The location and extent of the cracks depend on the cause and progression of the failure. The
cracked area may be localized (e.g bursted bubble, scratch), extend along specific module
areas (e.g. long or between the cells, along the busbars) or extend over large or the full area
of the module (e.g embrittled surface). The crack can be very deep and affect the back sheet
stack.
Detection VI, (INS)
Origin The degradation of the backsheet can be caused by environmental factors like UV-irradiation,
thermal stress, external mechanical stress or by internal stress (e.g. thermomechanical stress
with the multimaterial composite PV-module) or incorrect handling during transport and instal-
lation (local cuts, scratches). Deep backsheet cracking (whole backsheet stack split) is often
followed by moisture ingress and corrosion. This is more frequent and severe under hot and
humid conditions. The use of low -quality material (e.g. low UV resistance) or incompatible
material combinations (backsheet ↔ encapsulant) causes most of the premature degradation
failures. Discolouration and strong chalking can be precursors for backsheet cracking. Deep
cracks or bursted bubbles can be the result of local hotspots/burn marks that split or break
the backsheet.
Production  Installation Operation
Impact A broken backsheet can cause electrical insulation failure, posing a safety hazard and a
potential ground fault. On the long-term, power degradation due to the penetration of moisture
into the module which induces further failures (e.g. corrosion, delamination) can occur. In the
case of deep cracks reachi ng the active part of the cells, the insulation is immediately com-
promised and safety is not anymore fulfilled.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules. In case of in-
dividual module testing all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.
Ground fault detection by in-
verter or other devices at all
time, check validity of IEC
61215 certification and BOM,
visual inspection before in-
stallation.
Regular system inspections.
Installation of arc detection
tool.

## Página 28

28
EXAMPLES (page1) PVFS 1-5vs.02
Examples
1-3

Cracked backsheet in combina-
tion with yellowing under a hot
cell [Eder19].
Squared cracks beneath cell in-
terspaces [Eder19].
Cracking between cells [Pack-
ard12].
Severity
Examples
4-6

Longitudinal cracks located un -
der bus bars [Eder19].
Backsheet cracking [DuPont20]. Backsheet cracking [DuPont20].
Severity
Examples
7-8

Localized superficial damage
[Köntges17].
Deep scratch on backsheet [By
the courtesy of TUV Rheinland].
PVDF outer layer cracking [By the
courtesy of PCCL].
Severity

## Página 29

29
Component
Defect
Module
Backsheet chalking (whitening) PVFS 1-6vs.01
Appearance White powder is detectable on the external surface of the backsheet. It can be seen by passing
a finger over the backsheet. It can be removed. The backsheet has usually a rough or dull
appearance.
Detection VI
Origin Chalking is caused by the photothermal degradation of the polymers in the outer backsheet
layer containing inorganic pigments. For example, TiO 2 pigments are often used in the outer
layers as UV blocker.
Production  Installation Operation
Impact Chalking does not affect module safety or performance on first sight, but it can be a sign for
an ongoing degradation of the backsheet and a precursor for severe backsheet cracking. Due
to the degradation-induced reduction of UV protection, more serious fa ilures, such as back-
sheet cracking and insulation failures can occur. Enhanced moisture diffusion into the en-
capsulant/active PV-parts can lead to corrosion of cells and connectors, having a negative
impact also on the performance.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Regular inspections should
be done to monitor the pro-
gress of the observed failure.
Ground fault detection by in-
verter or other devices at all
time.
Check validity of IEC 61215
certification and BOM.
Regular system inspections.

## Página 30

30
EXAMPLES (page1) PVFS 1-6vs.01
Examples
1-2

Finger with white powder [ By the
courtesy of TUV Rheinland].
Fingerprint on a module with
chalking [By the courtesy of TUV
Rheinland].

Severity

## Página 31

31
Component
Defect
Module
Burn marks PVFS 1-7vs.01
Appearance Burn marks are visible with the naked eye as burnt, blackened area/s. The burn mark may
lead to bubbling or melting of the polymeric encapsulant , and/or glass breakage or a hole in
the backsheet.  Burn marks on the backheet may be not visible from the front requiring an
inspection with an IR camera if the back of the module is not accessible. They may however
not be visible by IR inspection in case no further or ongoing heating occurs.
Detection VI, IRT, (EL)
Origin The defect is associated with parts of the module that became very hot because of production
errors (e.g weak solder bonds, ribbon breakage, incomplete cell edge isolation, alignment er-
rors, metal particles) and/or transportation/handling errors (e.g,  cracked cells, damaged
back-sheet) in combination with one or more operational factors (e.g. shadowing, open cir-
cuited bypass diodes, reverse current flows).  Physical stress during PV module transporta-
tion, heavy snow loads, a lightning strike, thermal cycling, and/or hot spots by partial cell
shading during long-term PV system operation forces mechanical weak(ended) cell/connec-
tion parts to break. Burn marks occur for example when a reverse current flow causes heating
that further localizes the current flow, leading to a thermal runaway effect and the associated
burn mark.
Production  Installation Operation
Impact Burn marks on interconnections are often associated with power loss, but if redundant electri-
cal interconnections are provided, a failed solder bond may have negligible effect on the power
output. If all solder bonds for one cell break, then the current fl ow in that string is completely
blocked and an electric arc can result if the current cannot be bypassed by the bypass diode
and the system operates at high voltage. Performance, reliability and safety are likely to be
severely compromised. Such an arc can cause a fire if there happen to be flammable material
around. If there is a question about whether the existence of the burn mark requires replace-
ment of the module, an infrared image under illuminated and/or partially shaded conditions will
quickly identify whether the area is continuing to be hot and/or whether c urrent flow has
stopped in that part of the circuit. Temperature difference between neighbouring cells should
not be over 30 K. At this stage safety risk may still be not so high because the temperature of
this hot spot cell does not increase to more than around 100 °C. Also edge  isolation faults
on the solar cell level are under normal conditions not problematic, but when the bypass diode
is in open-circuit, the current is driven in reverse through the shunts of the solar cells and burns
the encapsulation.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules.
Visual inspection before in-
stallation, commissioning of
system with IRT.
Regular system inspections.

## Página 32

32
EXAMPLES (page1) PVFS 1-7vs.01
Examples
1-3

Burn mark at the backsheet with
cracked backsheet [Sinclair17].
Burn marks at the backsheet due
to heating along a busbar [Könt-
ges14].
Burn mark associated with over-
heating along the metallic inter-
connection (without back -sheet
damage) [Köntges14].
Severity
Examples
4-6

Front and back side view of burn marks caused by open-circuited by-
pass diodes and current mismatch conditions (due to shading or
cracked cells) [Köntges14].
Burn marks caused by defect
bypass diodes or an intercon -
nect failure in the junc. box
[Köntges14].
Severity
Examples
7-9

Burn mark with broken glass
caused by poor bussing ribbon
soldering [Yang19]. (see also
PVFS 1-8 and PVFS 1-8)
Burn mark due to intrinsic shunt -
ing caused by error in manufac -
turing process [Yang19].
Burn mark due to intrinsic
shunting caused by error in
manufacturing process
[Yang19].
Severity

## Página 33

33
Component
Defect
Module
Glass breakage PVFS 1-8vs.02
Appearance Glass is cracked locally or over the full area of the module. Glass breakage looks different
depending on the type of glass and the origin of the glass breakage. Thermally toughened or
tempered glass will shatter into small pieces, whereas annealed glass b reaks into larger
pieces. Heat -strengthened glass stays in between. Cracks occurring on the rear glass of
glass/glass modules are more difficult to see by eye especially in the case of thin heat -
strengthened glass.
Detection VI, (IRT)
Origin Glass breakages of the front glass can be caused by heavy impacts such as hail or stones or
other extreme mechanical stress onto the module frame due to external stresses or bad
mounting or internal stress due to h igh temperatures originating from hot-spots or arcing.
Annealed glass can break due to thermal gradients or stress induced by the lamination pro-
cess or cleaning of the modules. A relatively frequent failure in the field is glass breakage of
frameless PV modules and glass/glass modules. In particular bif acial modules with thin
glasses with a thickness of 2 mm to 1.6 mm, are more sensitive to glass breakage. This is due
to the fact that thin glass cannot be fully tempered like 3 mm thick glass, reducing the surface
resistance against stress, impacts and scratches. Very often the cracking of thin glass starts
on the rear glass. The origin is not fully understood. In some cases the origin is in the prepa-
ration of the cutting edges or the drilling of the holes for the connection to the junction box. At
the planning and installation stage failure occurs due to either (a) poor clamp geometry for the
module, e.g. sharp edges, (b) too short and too narrow clamps or (c) the positions, kind or
number of the clamps on the module not being chosen in accordance with the manufacturer’s
manual. The second origin which induces glass breakage could be excessively tightened
screws during the mounting phase or torsion of the module, not respecting requirements for
planarity. The glass of some PV modules may also break due to vibrations and shocks occur-
ring during transportation or handling. Another reason for glass breakage comes from impact
stresses on the glass edge. Sometimes vandalism or damages by animals occurs (e.g. ani-
mals climbing on the modules or birds dropping stones or other objects from the sky).
Production  Installation Operation
Impact Module mechanical integrity is compromised when the glass is broken. Over time glass break-
age leads to loss of performance due to cell and electrical circuit corrosion caused by the
penetration of oxygen and water vapour into the PV module. Shattering of tempered glass
usually also breaks the cells reducing the power of the module and increasing the risk of hot
spots and arcs. Mechanical and electrical safety is thus compromised. Firstly, the insulation of
the modules is no longer guaranteed, in particular in wet conditions and ground fault and in-
verter shutdown can occur. Secondly, glass breakage causes hot spots, which lead to over-
heating of the module and possible fire injection. A module with a completely broken glass
lead to current and power reductions in the whole string.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
All damaged modules have
to be replaced . In case of
known origin, the error must
be rectified. Regular visual in-
spections are recommended
in case of unknown causes
not related to external impact.
Adequate transport proce-
dures, installation and clean-
ing by trained personal, in
case of higher snow or hail
loads use of certified mod-
ules.
Qualification of modules and
mounting configuration with
expected mechanical load.

## Página 34

34
EXAMPLES (page1) PVFS 1-8vs.02
Examples
1-3

Chipped glass at the corner
[Packard12].
Glass breakage along the string
interconnect ribbons due to weak
manufacturing process [ By the
courtesy of SUPSI PVLab].
Glass breakage of tempered
glass induced by a hot -spot [By
the courtesy of SUPSI PVLab].
Severity
Examples
4-6

Glass breakage caused by too
tight screws [Köntges14]. (see
also PVFS 3-1)
Glass breakage caused due to
poor clamp design [Köntges14].
Glass breakage caused due to
poor clamp design [Köntges17].
(see also PVFS 3-1)
Severity
Examples
7-9

Glass breakage through high
temperature gradient and not
tempered glass [Köntges14].
Glass breakage of tempered
glass induced by burn mark
[Köntges17]. (see also PVFS 1 -7
and PVFS 1-9)
Breakage of tempered glass
[Köntges17].
Severity

## Página 35

35
EXAMPLES (page2) PVFS 1-8vs.02
Examples
10-12

Direct lightning stroke [Könt-
ges16].
Impact damage caused by a
heavy object [By the courtesy of
SUPSI PVLab].
Hail damage [By the courtesy of
SUPSI PVLab].
Severity
Examples
13-15

Broken thin (<=2 mm) rear
glass. Long (many dcm) crack
lines without splitting the crack
with no clear crack start.
Glass breakage on the rear side
of a bifacial module caused by
insufficient spacing between
modules (thermal expansion of
module frame is not considered).

Severity

## Página 36

36
Component
Defect
Module
Cell interconnection failure PVFS 1-9vs.02
Appearance Weak or broken interconnection of cells or substrings is not easy to be seen by the naked eye.
The failure can be identified as dark region in the electroluminescence image where the failed
interconnect would not be collecting carriers and result in a hot spot in the infrared image. In
a progressed stage burn marks and glass breakage can occur.
A short-circuited cell is also difficult to recognize with naked eye, while it appears as dark cell
in the EL image. For parallel connected substrings the substring with short -circuited cell ap-
pears brighter in an EL image and slightly warmer in IRT than o ther substrings in parallel
connection.
Detection EL, IRT, STM, (VI)
Origin Typically, it is caused by the manufacturing process (e.g. poor soldering, misplacement of
ribbons, too intense deformation of the ribbon kink, narrow distance between the cells, incor-
rect conductive glue application) followed by thermomechanical stress or repetitive wind load
caused by the outdoor operating environment. Electrochemical corrosion can be another
cause for the degradation of interconnections. Short circuited cell occurs when the intercon-
nection ribbon or conductive glue connects the front and rear sides of a cell.
Production  Installation Operation
Impact Poor interconnections (soldering bonds) lead to an increase of contact resistance, higher
power dissipation and localized heating. Broken connections are often associated with power
loss, but if redundant electrical interconnections are available, a failed  connection may have
negligible effect on the power output. Safety risk may be not so high until the temperature of
the induced hot spot does not increase to more than around 100 °C. If all busbars of a cell
are interrupted, then the current flow in that string is completely blocked and an electric arc
can result if the current is not bypassed by the bypass diode and the system operates at high
voltage. The safety risk depends on the durability of this bypass diode. A bypass diode, which
is continuously active over days can be damaged and pass into open -circuit or short circuit
state. As a result of an open circuited diode, the current goes through the failed cell string
and generates heat at the disconnected position. Very high temperatures or an electric arc
may cause fire, expose the electrical conducting parts to the user and destroy the mechanical
integrity of the module.
The power loss of a module with short-circuited cell depends on the interconnection profile of
the module. For series connected cells in a module only the power of the short-circuited cell(s)
is/are lost. The impact of short -circuited cells in a parallel connection has to be assessed in
detail, but it is lower than the power of cells equivalent to the number of parallel connected cell
times maximum number of shunted cells in one series connected substring . In most cases
there is no safety issue for short-circuited cells.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules.
Check proof of factory inspec-
tion according to IEC 62941.
Commissioning of system
with IRT.
Pre-shipment inspection or
sampling EL inspection when
modules arrive the installation
site.
Regular system inspections.

## Página 37

37
EXAMPLES (page1) PVFS 1-9vs.02
Examples
1-3

Zoom of a broken cell intercon -
nect [Yang19].
EL image of a module with 3 cells
with disconnected inter -connect
ribbons [Köntges14].
Disconnected cell interconnect
with delamination [Köntges17].
Severity
Examples
4-6

Dislocation of interconnection
ribbon [Sinclair17].
Poor soldering of string inter -
connect leading to burn mark and
broken glass [Yang19]. (see also
PVFS 1-7 and PVFS 1-8)
Mirco arc which occur if the con-
ductive glue on the string inter-
connect has an insufficient con-
tact [Köntges14].
Severity
Examples
7-9

IRT and EL image of short cir-
cuited shingled cells due to incor-
rectly applied conductive adhe-
sive [By the c ourtesy of Remy
Wedig, pvControl].

Severity

## Página 38

38
Component
Defect
Module
Potential induced degradation (PID) PVFS 1-10vs.02
Appearance S (shunting) and p (polarization) -type PID are not optically visible; however advanced stages
of c (corrosion) or d (delamination) -type PID are visible. PID causes a progressive power loss
and some PID modes may also manifest in discoloration and hot spots over time . PID-s can
be detected through IRT imaging of operational PV modules in direct sunlight or in the labor-
atory, where PID appears as warmer cells close to the bottom frame or patchwork patterns,
and is more significant in PV modules positioned close to one of the poles of the PV string.
PID-s is also detectable by EL imaging, especially under low current bias (1/10 rated current),
where the affected cells closer to the module frame show reduced luminescence. PID -s
causes a decreased shunt resistance, FF, and V oc in the IV curve, and is more noticeable
under low light. PID-p shows a decrease of luminescence and no low current bias dependency,
being harder to detect with EL images. IV measurements can be used to confirm the presence
of PID in combination with IRT or EL. PID-p causes a decrease in Isc and Voc, typically originat-
ing on the rear side of p -type-base cell modules (PERC) and the front of those using n -type
cells (PERT, TOPCon, IBC).
Detection IV, EL, IRT, (MON)
Origin PID is a degradation mode induced by a high voltage stress  with respect to ground. The oc-
currence of this failure depends on the magnitude of the voltage (number of serially connected
PV modules per string) and the polarity of the electrical field build -up between the fram-
ing/glass surface and the solar cells. The last depends on the inverter typology (transformer),
the grounding concept , and cell technology. Modules with p -type cells degrade in negative
polarity strings whereas modules with n-type cells in strings with positive polarity. The degra-
dation is accelerated by elevated temperature, humidity, rain (surface wetting), condensation
and soiling. PID-p is caused by the build-up of surface charges on the cells, which results in a
current loss. PID-s is induced by leakage currents coming from the displacement of Na+ ions
from the module’s front or rear glass and through the encapsulation material. The flow of Na+
ions creates shunts in the cells. For both PID types, module and cell design has a fundamental
influence if and how much a module is affected by PID. There are modules on the market that
are designed to be PID-resistant.
Production  Installation Operation
Impact Yield losses of 20 percent and more within 1 year were observed in the past. Due to its cata-
strophic performance loss, PID bears a high economic risk. PID-s is to some extent a reversi-
ble polarization type and can therefore be partially reversed or stopped when detected in time.
However, if detected too late, it can lead to irreversible power loss. The PID-p effect causes
instead a significant reduction of Isc, Voc and power. PID-p is thought to be fully regenerated
by reversing the polarity of the bias potential. In some cases, material degradation of the mod-
ules through corrosion and delamination occurs associated with e xcessive leakage current .
Up to now, safety problems directly related to the PID have not been reported, but hot spots
and corrosion caused by the strong cell mismatch may cause such safety issues.
Safety:   Performance:
Mitigation Corrective actions Preventive actions (recom-
mended)
Preventive actions
(optional)
Recovery of early-stage PID
is possible by placing mod-
ules in non-sensitive polarity
strings, applying a reverse
voltage. More advanced PID
cannot be fully recovered.
Modules successfully tested
per IEC 62804 -1 are less
prone to PID. Optional for
PID-resistant modules.
Placing the modules in non-
PID-sensitive DC voltage
strings with one terminal
grounded using an inverter
with a transformer or invert-
ers with anti-PID features.

## Página 39

39
EXAMPLES (page1) PVFS 1-10vs.02
Examples
1-2

Strings with PID -s, detected with IR thermography [Könt-
ges14].
Dark IR thermography at Isc for a module
affected by PID-s [Köntges14].
Severity
Examples
3-4

Strings with PID-s, detected with EL imaging [Köntges14]. Electroluminescence image made at Isc
for a module affected by PID -s [Könt-
ges14].
Severity
Examples
5-6

PID-s affected module with power loss of 89%, left: EL at
1.5 x I sc, right: I -V curve of the same module at 1000 and
200 W/m2 [Herrmann21].
PID-s affected module with power loss of
14%. top: EL at 1.5 x Isc. bottom: EL of the
same module at 0.2 x Isc [Herrmann21].
Severity

65
55
36
22

## Página 40

40
EXAMPLES (page2) PVFS 1-10vs.02
Examples
7-8

PID-s affected Al BSF module EL imaged at I sc and
0.1 Isc shows chessboard pattern degradation, more
visible at the lower bias current. STC IV curve shows
decreased shunt resistance, FF and V oc
[Mahmood2024].
PID-s affected PERC p-type bifacial module EL im-
aged at I sc and 0.1 I sc shows degradation near
frame, more visible at the lower bias current. STC
IV curves of front and rear show decreased FF
[Mahmood2024].
Severity

Isc
bias
0.1Isc
Front
Rear

## Página 41

41
EXAMPLES (page3) PVFS 1-10vs.02
Examples
9-10

PID-p affected p-type PERC bifacial module EL im-
aged at I sc and 0.1 I sc shows a decrease in minority
carrier lifetime and luminescence. Rear side STC IV
shows significant decrease of I sc, and moderate de-
crease of V oc. No noticeable decrease in shunt re-
sistance [Mahmood2024].
PID-p affected n-type TOPCON bifacial module EL
imaged at Isc and 0.1 Isc, shows a uniform and sig-
nificant decrease (~18 times less) in luminescence
relative to a non-degraded module, and no notice-
able current dependency of the EL image. Front
side STC IV shows a significant decrease in Isc and
Voc and no noticeable decrease in shunt resistance
[Mahmood2024].
Severity

Isc bias
0.1Isc
Rear Front

## Página 42

42
Component
Defect
Module
Metallisation discolouration/corrosion PVFS 1-11vs.01
Appearance The discolouration and/or corrosion of the cell metallisation and the interconnections is getting
visible as a light yellow to dark brown to black discolouration of the electrical parts. Depending
on the material combinations corrosion is furthermore noticeable by the presence of galvanic
products that may appear powdery, white, light gray, and/or have a yellow, blue, or green
tinge. The defect occurs typically at the solder bonds, on the cell gridlines/fingers or the
cell/string interconnect ribbons. It is very often observ ed together with other failures like de-
lamination and discolouration of the encapsulant and sometimes with burn marks.  Under
certain circumstances corrosion is more visible near cell edges. Dark areas at the cell borders
of the EL images can here highlight the diffusion of moisture through the rear side of the mod-
ule and the gaps between the cells and the subsequent front side cell corrosion starting from
the edges.
Detection VI, (EL, IV)
Origin The corrosion/oxidation of the metallisation is caused by the presence of moisture and acidity
in the encapsulant, as e.g. acetic acid, a degradation product of the mostly used encapsulant
EVA or remaining crosslinker (peroxides). Acetic acid has a corrosive effect on the cell metal-
lisation and the cell interconnect. The ingress of moisture caused by an ongoing delamination
process leads together with the oxygen to a further acceleration of the corrosion. Corrosion
can be caused by a poor manufacturing proc ess (e.g residual crosslinker due to a too short
lamination process; imperfections in cell soldering) or the choice of poor materials (low corro-
sion resistance of tin-based coating of copper ribbons, high water permeability of back sheet
and/or encapsulant materials). Environmental factors can accelerate the corrosion (e.g am-
monia, salt, humidity, temperature).  For these reasons, corrosion is more frequent and severe
under hot and humid climates or in agriculture or maritime environments. Discolouration ca n
be also related to non -corrosive processes like a discolouration due to light -sensitive solder
flux residues on the ribbon.
Production  Installation Operation
Impact The metallisation, and/or interconnect, corrosion leads to an increased series resistance and
therefore losses in module performance. The power loss is less pronounced for modules with
metallisation discolouration without corrosion. The defect does not automatically pose a safety
issue. Locally increased series resistance leads to current mismatch. If the mismatch is getting
significant, it can trigger the bypass diode and cause further power loss of the PV module.
Safety:   Performance:
Mitigation Corrective action Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules.
Check validity of IEC 61215
certification and BOM.

Regular system inspections.

## Página 43

43
EXAMPLES (page1) PVFS 1-11vs.01
Examples
1-3

Discolouration due to corrosion
or to light -sensitive flux residues
on the ribbon.
Discolouration due to corrosion
on the ribbon [By the courtesy of
SUPSI PVLab].
String interconnect corrosion.
[Köntges17]
Severity
Examples
4-6

Cell interconnect c orrosion
[Köntges17].
Modules with light Ag finger oxi-
dation after 5 years in the field
[Yang19].
Severe oxidation/corrosion and
burn marks on the Ag fingers,
busbars, and interconnects of
modules after 25 years [Yang19].
Severity
Examples
7-9

Corrosion seen as red, green
and black discolouration in the
string interconnect [Yang19].
Busbar corrosion and delamina-
tion at the edge [By the courtesy
of SUPSI PVLab].
Glass/glass module showing de-
lamination and subsequent cor-
rosion [Köntges17].
Severity

## Página 44

44
Component
Defect
Module
Glass corrosion or abrasion PVFS 1-12vs.01
Appearance The degradation of the glass front layer is getting visible as a homogenous or heterogeneous
change in colour and transparency of the glass. The affected glass surface can appear hazy or
milky and in some cases also rougher compared to the non -degraded module/module area.
Increased susceptibility to soling could be observed.
Detection VI, (IV)
Origin To optimise the efficiency and appearance of a PV module most manufacturers apply some
anti-reflective coatings (ARC), anti -soiling coatings (ASC) or multilayer coatings on the front
of their modules. 1-3% more power can be obtained by these techniques res pect to module
with uncoated glass. Corrosion or abrasion of these layers can however, reduce or vanish the
effectiveness of these coatings. Glass corrosion is caused by atmospheric humidity in combi-
nation with gases or particles present in the atmosphere (e.g. pollutants, salt, ammonia) and
the glass. It happens for example when water (dew) dissolves some of the sodium ions from
the top of the soda lime glass, leading to the production of an alkali base that can then corrode
the glass silicate. Glass abras ion or corrosion can be also caused by inappropriate cleaning
techniques (mechanical removal techniques, inappropriate cleaning agents) which damage or
removes the coatings. Abrasion occurs mostly in the desert, due to the combination of wind,
sand and dust which causes abrasion and frosting of the glass surface.
UV or voltage induced degradation effects can further accelerate the degradation of the coat-
ings.
Production  Installation Operation
Impact Corrosion or abrasion of the glass front layer lowers the transmission of the glass, leading to
a power loss. The power loss is generally limited to a few percent and is saturating over time
except in the case where the soiling susceptibility is significantly increased and larger losses
can be observed. Operating and Maintenance (O&M) costs can be affected by this.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Depends on the
level of performance loss. For
extreme environments (e.g.
near to mines, cement facto-
ries), evaluate cost -effective-
ness of replacing modules
with lost yield.
Check validity of IEC 61215
certification and BOM, appro-
priate component selection in
function of intended applica-
tion.
Regular system inspections.

## Página 45

45
EXAMPLES (page1) PVFS 1-12vs.01
Examples
1-3

Zoom of module with hazy glass
(homogenous discoloration) due
to surface corrosion [India13].
Zoom of module with hazy glass
(heterogenous discoloration) due
to surface corrosion [Petter11].
Hazy glass due to glass corro -
sion close to frame [India18].
Severity
Examples
4-5

Glass corrosion on the front of a mono-Si back-contact module after
damp heat 90/90 testing [Walsh20].
Glass corrosion [Köntges16].
Severity

## Página 46

46
Component
Defect
Module
Defect or detached junction box PVFS 1-13vs.01
Appearance The junction box housing and lid appears either defect (weathered, brittle, cracked, warped,
melted or burned) and/or detached (open or loose lid, shifted or detached junction box from
backsheet). The sealant/adhesive material with which the junction box is attached to the back-
sheet can be weathered or appear as yellowed.  The sealing components/material around the
wire entrance or the lid can be damaged (squeezed, broken, brittle) or completely missing.
Detection VI
Origin Junction box detachment results from poor fixing of the junction box to the backsheet or use
of low quality adhesive. Acrylic or PE Foam tapes were used as junction box attachment ma-
terial in early years, but they frequently loss stickiness at low temperat ure and result in de-
tachment.  Use of inadequate IP rating junction box may cause water intrusion and subsequent
failure.  Opened or badly closed j -boxes may due to poor manufacturing process or air pres-
sure caused by high temperature for boxes with no exhaust path. Delamination near a junction
box can cause it to become loose. Improper handling or mounting of the modules can be also
the cause of damages the j -box, like pulling modules up on the cables before mounting, or
missing cable fixing or usage of too short cabling to interconnect modules to a string, causing
frequent or permanent mechanical stress on the j-boxes.
Production  Installation Operation
Impact A defect or detached junction box is causing humidity ingress with corrosion of the intercon-
nections, leading to performance losses and increasing risk of electrical arcing and subse-
quent initiation of fire. Furthermore, a loose junction box is putting mechanical stress on the
contacts within the junction box, with the risk of breaking them and exposing persons to active
electrical components.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced or repaired.
Regular inspections should
be done to monitor the status
of the not replaced modules.
Check validity of IEC 61215
certification and BOM.
Ground fault detection by in-
verter or other devices at all
time.
Regular system inspections.
Installation of arc detection
tool.

## Página 47

47
EXAMPLES (page1) PVFS 1-13vs.01
Examples
1-3

Poorly bonded junction box on
the backsheet [Köntges14].
Open junction box in the field
[Yang19].
Detached junction box from
backsheet [ By the courtesy of
SUPSI PVLab].
Severity
Examples
4-5

Left: Missing junction box lid sealing with corrosion of contacts.
Right: Good junction box sealing [India13].
Missing seal or strain relive of
module cables, improper cable
inlet [Sinclair17].
Severity
Examples
6-7

Melted junction box [By the cour-
tesy of TUV Rheinland].

Burned junction box caused by
corroded contact s within the
junction box [By the courtesy of
TUV Rheinland].

Severity

## Página 48

48
Component
Defect
Module
Junction box interconnection failure PVFS 1-14vs.02
Appearance Not connected, broken, burned, corroded or short circuited parts within the junction box. It can
involve solder joints, wires, bypass diodes or tabbing ribbons. The interconnection failure itself
could be hidden by the potting material in the junction box and be visible only by removing the
potting material. The material can appear as degraded (yellowed, browned, burned or bub-
bled) due to the heat or arcing occurring in the junction box.
Detection BYT, (IRT, EL, VI, IV, VOC)
Origin Bad contacts  in the junction box  can be caused by cold solder joints, thermo -mechanical
caused changes in contacts, wrong assembly or moisture ingress. Contacts are either sol-
dered, screwed or inserted (mechanical spring clamping). Bad soldering contacts are caused
by low soldering temperature (cold solder joint) or chemical residuals of the previous produc-
tion process on the solder joints. Bad mechanical contacts are caused by loose clamping or
screws. Mechanical contacts can get loose due to the thermal cycling of day and night and
seasonal changes. Moisture in gress in bad or damaged junction boxes (e.g. adhesion loss,
brittle, cracked, missing seal at wire entrance or junction box housing) leads to corrosion of
the contacts. Delamination near the junction box can cause it to become loose, putting me-
chanical stress on the contacts within the junction box and breaking them.
Production  Installation Operation
Impact Depending on the position of the bad contact and its character (resistive, open circuit, short
circuit or arcing) the impact on safety and performance can be very different. Resistive heating
can moreover result in discolouration and burn marks in the encpasulant/backsheet behind
and around the junction box and to glass breakage. In the worst-case interconnection failures
cause a short circuit or internal arcing within the j-box. The heat can be detected with a n IR
camera (hot spot). Furthermore, connection failure could lead to equal impacts to the PV
module as a diode failure if the connection to a bypass diode is lost ( missing/insufficient
bypass diode protection). In addition to the visual defects, interconnect failures can also lead
to significant power losses or loss of shade resilience, which can both be detected by BYT of
modules or strings. The measurement can be affected by changing mechanical or thermal
stress conditions. Interconnect failures are particularly dangerous because the arcing can ini-
tiate fire.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced, especially if the
modules are installed on
buildings. Regular inspections
should be done to monitor the
status of the not replaced
modules.
Request a proof of IEC
61730-2:2023 Annex A5 a) or
b) bypass diode  functionality
test in production . Commis-
sioning of system with IRT or
BYT. Compare VOC of paral-
lel strings.
Testing the module bypass di-
odes with a mobile test centre
prior to  installation. Regular
IRT inspections. Installation of
arc detection tool.

## Página 49

49
EXAMPLES (page1) PVFS 1-14vs.01
Examples
1-3

Junction box with poor wiring
[Köntges14].
Detached tabbing ribbon due to
bad soldering [Köntges14].
Corrosion failure due to water
soaking of the IP65 rated Jbox
[Yang19].
Severity
Examples
4-6

Jbox failure due to poor electric
connection [Yang19].
Evidence of loose screw connec-
tion inside Jbox with browning of
pottant [Yang19].
Cold soldering of module bus -
sing ribbon to the Jbox connec -
tion terminal pad w ith minor
browning of pottant [Yang19].
Severity
Examples
7-9

Overheating due to the poor Jbox
interconnect leading to light dis-
coloration and burn mark on front
and back side [Yang19].
Overheating due to the poor Jbox
interconnect leading to burn
mark and glass breakage
[Yang19].
IR imaging of a hotspot Jbox due
to loose electric connection in-
side [Yang19].
Severity

## Página 50

50
EXAMPLES (page2) PVFS 1-14vs.02
Example
10

A cold solder joint after the diode in any junction box (either outer or inner) [Köntges25] can
result in a safety failure that is undetectable by IRT. The not connected bypass diode is visible
with night EL inspection while applying string wise reverse voltage with 3%-5% of rated Isc [by
courtesy of Ternus & Diehl GbR].
Severity
Example
11

A cold solder joint before the diode in the outer junction box cause s a 1/3 power loss and is
detectable by IRT. However, if the inner junction box is affected, it does not cause the module
sub-string to operate in open circuit [Köntges25].
Severity
Example
12

Cold solder joints before and after the diode of an outer junction box results in full string loss,
which is detectable by IR T. The module location remains unidentifiable.  If the inner junction
box is impacted, the module continues to behave as intact [Köntges25].
Severity

## Página 51

51
Component
Defect
Module
Missing or insufficient bypass diode protection PVFS 1-15vs.02
Appearance Missing, disconnected, inverted, damaged, open circuited or short circuited bypass diode.
Detection BYT, (IV, IRT, EL, VI, VOC)
Origin Bypass diodes fail either because they are undersized or because they are exposed to high
voltages due to lightning strikes or other high voltage events. In addition to these two reasons,
the diodes have a certain ppm of failure rate, that is the nature of the component. For diodes
working constantly at high temperatures this failure rate increases. This can be the case, if
partial shading is frequently present. Typically, Schottky diodes are used as bypass diodes in
PV modules, but they are very susceptibl e to static high voltage discharges and mechanical
stress. Two main failure modes are observed with bypass diodes: open circuit or short circuit.
Short circuit condition occurs when the bypass diode is physical ly shortened in the junction
box, it is mounted the wrong way around or when it has been exposed to high voltages like
lightning strikes or static electricity. Open circuit condition occurs when a diode is simply miss-
ing, it is not properly connected, a strong current damaged the diode, or it is undersized and
not resisting to a continuous current flow. Short circuit failures are reported to be more frequent
than open circuit failures. However, open circuit failures are normally not detected.
Production  Installation Operation
Impact Bypass diodes are used to avoid the reverse biasing of single solar cells higher than the al-
lowed cell reverse bias voltage of the solar cells and to reduce the power loss caused by partial
shading on the PV module. In the case of an open circuited diode no current is flowing through
the bypass diode and a cell can be reversed with a higher voltage than it is designed for the
cell and may evolve hotspots that may cause browning, burn marks or, in the worst case,
fire. This failure is difficult to be detected until the module is exposed to these risks. A short
circuited bypass diode will continuously lower the voltage and thereby the power production
of the module.  A short -circuited module leads to inhomogeneous heating of individual cells
during operation. Also it causes mismatch losses in the case of parallel strings. Bypass diode
failures sometimes cause the junction box to deform  or even burnt due to heat dissipated in
the junction box.  When the junction box or backsheet are burnt through, the safety issues like
leakage current may follow.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced, especially if
the modules are installed
on buildings.  Regular in-
spections should be done to
monitor the status of the not
replaced modules.
Request a proof of IEC
61730-2:2023 Annex A5 a) or
b) bypass diode  functionality
test in production . Commis-
sioning of system with IRT or
BYT. Compare VOC of paral-
lel strings.
Testing the module bypass di-
odes with a mobile test centre
prior to  installation. Regular
IRT inspections. Installation of
arc detection tool.

## Página 52

52
EXAMPLES (page1) PVFS 1-15vs.02
Example 1

A short circuited bypass diode causeS a 1/3 power loss and is detectable by IRT [Köntges25].
Severity
Example 2

An open circuited bypass diode causes a safety failure that is undetectable by IRT [Köntges25].
Severity

## Página 53

53
Component
Defect
Module
Not conform power rating  PVFS 1-16vs.01
Appearance The STC output power of a brand new module is below a specified tolerance limit or the min-
imum nameplate output power is not clearly specified by the manufacturer.
Detection IV, (MON)
Origin Deviations of the measured power of a single module respect to the name plate power de-
pends on the product variability, manufacturing quality, the labelling policy and the measure-
ment uncertainty.  The quality of cells (e.g. LID susceptibility) together with the binning method
applied in production for the reduction of mismatch losses, has a significant impact on the
product variability. The deviations in the measurement in the factory comes from several
sources of uncertainty, for example the environment temperature, measured module temper-
ature, calibration of the solar simulation, maintenance of the reference module, measurement
equipment, connectors and cables. According to the international standards, the power rating
has to take into account any technology related initial degradation effects (for c -Si see FS 1-
17). This means that after a first exposure to light the output power of a new module has still
to be within the rated power tolerance. The measurement uncertainty of the test laboratory
performing the STC performance test has therefore to be taken into account. The modules
have to be stabilised according the procedure described in IEC 61215 -2:2021. Technology
specific test requirements are described in IEC 61215 -1-1:2021 to IEC 61215-1-4:2021. De-
pending on the technology, a maximum allowable measurement uncertainty is defined for the
verification of power ratings. For c-Si modules it is specified as 3%. A PV module is considered
to be conform to the IEC61215 standard, when following criterion (gate 1) is fulfilled:

Pmax(Lab) ∙ (1 +
1.65
2 |m1|[%]
100 ) ≥ Pmax(NP) ∙ (1 −
|t1|[%]
100 )
Pmax (Lab):  measured maximum STC power of each module in stabilized condition
Pmax (NP):    minimum rated nameplate power of each module without rated production tolerances
 m1:    measurement uncertainty in % of laboratory for Pmax (expanded combined uncertainty (k = 2)
   t1 :   manufacturer's rated lower production tolerance in % for Pmax
The minimum nameplate power rating, Pmax(NP) and tolerance t1 has to be derived from the
nameplate or data sheet values. If the Pmax(NP) derived from the datasheet is different from
the nameplate value, the module can be considered to be not conform. If the tolerance is not
stated on the nameplate or the datasheet, then t1 = 0. If the tolerance is not reduced to a single
value on the nameplate or data sheet (for example, if multiple tolerances or measurement
uncertainty components are specified) the smallest number shall be utilized.
Production  Installation Operation
Impact A non-conform STC power rating is not a real module failure, as it causes no degradation or
safety issue, but it has a negative impact on the lifetime energy yield and financial return. An
incorrect estimation of the installed STC power has a direct impact on the energy yield predic-
tions and investor expectations.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Confirm underperformance
through an accredited PV test
laboratory.  Claim for missing
power.
Verify power warranties and
data sheet conformity, pur-
chase modules from trusted
manufacturers.
Independent third party test-
ing of samples at factory gate
and/or arrival on site. Signa-
ture of a contractual agree-
ments.

## Página 54

54
EXAMPLES (page1) PVFS 1-16vs.01
Examples
1
a)

b)
c)
d)
Example of a hypothetical conform (a-c) name plate and datasheet values with on the right the accord.
IEC 61215-1:2021 derived rated values and tolerances in comparison to a hypothetical example of a
not conform STC rating (d) [IEC 61215-1:2021].
Severity  NA

## Página 55

55
EXAMPLES (page2) PVFS 1-16vs.01
Examples
2

Statistical analysis done by Eternalsun on around 6500 new modules with 96 different PV module types
from 29 different manufacturers . [Herrmann21] Considering the measurement uncertainty of +/ -2% a
total of 4.6% of the modules are below the gate 1 limit defined by the IEC 61215 standard [IEC 61215 -
1:2021].
Note: In case of a measurement uncertainty of +/-5% none of the PV modules would fail, but it would be not conform
to the IEC 61215 standard prescribing a maximum measurement uncertainty for c-Si modules of +/-3%.
Severity

## Página 56

56
Component
Defect
Module
Light induced degradation in c-Si modules (LID/LeTID) PVFS 1-17vs.02
Appearance Light induced degradation in crystalline silicon modules is recognisable mainly as a drop in
STC output power, but also short circuit current and open circuit voltage, within the initial life-
time of a PV system. It isn’t correlated with any visual defect or other failure modes. Increasing
non-uniformity of electroluminescence images (patchwork pattern) can in some cases high-
light an ongoing degradation process.
Detection IV, (EL, IRT)
Origin Two different light induced degradation effects are known: LID (light induced degradation) and
LeTID (light and elevated temperature induced degradation). Both degradation modes occur
at cell level, but the physical mechanism staying behind them are different. The first is related
to the concentration of boron and oxygen in the cells, whereas the second one is probably
correlated to the concentration of hydrogen in the cell, but the mechanisms are still not fully
understood.  Mainly p -type boron-doped multi and mono crystalline silicon modules are af-
fected. Gallium-doped and high-efficiency cell technologies that use n-type wafers, such as n-
type PERC, HJT, or n-PERT seem to be much less or not at all concerned by these two deg-
radation effects. LID occurs only within the first days of exposure to the sun and is limited to
1-3%, whereas LeTID is in a more severe and long-term light induced degradation mechanism.
LeTID was observed for the first time with the introduction of PERC modules on the market.
The degradation can reach up to 10% and sum-up with the LID loss. It occurs only at elevated
temperatures above 50°C. The speed with which the degradation occurs depends on the av-
erage module temperature and is therefore strongly site dependent. The time frame in which
it occurs is in the order of magnitude of years. Once the full de gradation is reached the mod-
ules can regenerate, recovering the lost power. This process is however very slow and also
climate-dependent. The lost power may even not recover over the typically expected 25-year
lifetime of a module. There exist approaches of accelerated regeneration of LeTID -sensitive
modules in the field, but they are typically costly and not very user-friendly. Over the last years
most manufacturers adapted their cell production process to stabilise the cells in-line.
Production  Installation Operation
Impact LID or LETID causes no safety problems, but it has a negative impact on the lifetime energy
yield and financial return. An under-estimation of the initial degradation has a direct impact on
the energy yield predictions and investor expectations. LID is les s critical for the investors,
because it is generally less severe and it is taken into account by the manufacturers when
labelling the modules and defining the first year warranty, whereas a high LeTID degradation
rate and the difficulty to predict the tre nd over time is much more critical for manufacturers’
warranties and system owners. The sensitivity of PV modules to LeTID can be tested in the
laboratory.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Confirm underperformance
through an accredited PV test
laboratory.  Claim for missing
power.
Verify power warranties. Ver-
ify the use of LeTID  stable
cells by module manufacturer.
Request test reports with %
power loss for realistic estima-
tions. Stipulate a contractual
agreement on tolerated loss.
Test individual modules. Ver-
ify BOM (cell type).

## Página 57

57
Component
Defect
Module
Insulation failure PVFS 1-18vs.01
Appearance A module with bad insulation between its current carrying parts and the frame (or the outside
world) are not directly visible by eye. An unequivocally detection is only possible through a
measurement of the insulation resistance of the module under dry (≥4 0 Mohm/m2) or better
humid/wet conditions. It can be sometimes deduced by the presence of visual defects which
can potentially lead to insulation problems.  Under certain circumstances like after a rain fall
or in the early morning when the PV modules are covered by dew, this kind of defect is de-
tected by the inverter (low insulation fault) or the inverter is switching off when the resistance
value falls below a certain limit.
Detection INS, (MON)
Origin Insulation failures can have different causes. It can occur in the design/production phase of a
module, due to solar cells too closely positioned to the frame or to material weaknesses like
the use of inadequate encapsulation or backsheet materials or a poor lamination process.  In
the installation phase it can be caused by mechanical damages of the module, whereas in the
operational phase it is generally caused by catastrophic events or due to a delamination pro-
cess close to the edge of the module or water  ingress or condensation in the junction box.
Modules with failed or skipped insulation test in production due to an insufficient quality as-
surance could be also the origin of the problem.  Various module failures are at the origin of
an insulation failure: backsheet and encapsulant delamination, backsheet damages, burn
marks, glass breakage.
Production  Installation Operation
Impact A low insulation resistance at module level itself does not lead to a performance loss, until an
inverter failure occurs. The presence of an electrical leakage current to the frame can become
a safety hazard exposing persons to a potential electric shock hazard. Touching non-insulated
parts of the string or frame can cause severe injury, without the use of safety gear and safe
measuring instruments.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed modules. In case of in-
dividual module testing all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.
Check validity of IEC 61215
certification and BOM, com-
missioning of system with
IRT,  ground fault detection by
inverter or other devices at all
time.
Regular system inspections,
Insulation testing of modules
with mobile test centre before
installation.

## Página 58

58
Component
Defect
Module
Hot spot (thermal patterns)
PVFS 1-19vs.02
Appearance A hot spot is a thermal abnormality such as a local overheating or a thermal pattern which
deviates from the normal behaviour of a module. It can be detected only by imaging techniques
such as e.g. infrared thermography (IRT). Hot spots are not visible by the naked eye until they
lead to irreversible hot  spot damages like e.g. local yellowing, burn marks, glass or cell
breakage. The position, size, intensity and pattern of the hot spot/s depends on the origin and
progress of the failure, but also under which conditions the module is operating (shading, load
and irradiance level).
Detection IRT, (VI)
Origin A hot spot can be triggered by various factors, including (i) previous failures, like damaged
cells (see PVFS 1 -01), glass breakage (see PVFS 1 -08), poor electrical connections ( see
PVFS 1-09 and 1-14), insufficient bypass diode protection  (see PVFS 1 -15) and p otential-
induced degradation (PID) (see PVFS 1-10), (ii) production-related issues, like severe cell
mismatch, low-quality solar cells, or poor module manufacturing processes, or (iii) non-ideal
operating conditions like shading or soiling (see PVFS 1-20). When shading condition oc-
curs, the affected cell or group of cells is forced into reverse bias, causing it to dissipate power,
which can lead to overheating. If the power dissipation is high or localised, the reverse biased
cell(s) can overheat, potentially resulting in melting of solder joints, deterioration of the encap-
sulant and/or backsheet, and even glass breakage. To reduce the effects of hot spots, bypass
diodes are connected in parallel with cells. Properly designed and functioning bypass diodes
help in reducing hot spot damages from occurring.
Production  Installation Operation
Impact Hot spot formation does not always result in significant power loss. Due to normal tolerances
in cell sorting and PV module production, thermal abnormalities under 10% of the inspected
modules usually do not indicate quality issue s. Most modules with a single hot cell have an
insignificant power loss. Power reduction becomes significant when a bypass diode is perma-
nently activated and consequently the cell string is cut off from power production of the PV
module. The impact on system performance is only noticeable in its energy yield when multiple
PV modules are affected. Severe losses can occur if PID is the origin of the abnormal cell
heating. Module safety can be compromised when overheating leads to critical module dam-
ages or to a fire. Temperature differences of 10 K to 20 K (at approximately 800 W/m2) should
be further controlled to prevent temperature increases during PV system operation, as they
may indicate damaged bypass diodes or junction box failures, posing direct safety risks (see
PVFS 1-14 and 1-15). Differences over 20 K (at approximately 800 W/m2) are critical, risking
accelerated degradation of polymer materials and loss of insulation properties. If affected mod-
ules aren’t replaced, temperature differences may rise further.  Lack of regular cleaning and
maintenance can also lead to high temperatures due to bird droppings or power mismatches,
resulting in module damage. In such cases, it may be challenging to identify whether the cause
was a quality issue or insufficient maintenance.
Safety:  N/A Performance: N/A
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Modules with a direct safety
risk or a severity of 5 should
be replaced or repaired. If
more than 10% modules show
thermal abnormalities, the
reason for that behaviour
should be evaluated and cor-
rective actions implemented.
Commissioning of system
with IRT or BYT.
Regular system inspections
(i.e. IRT).

## Página 59

59
EXAMPLES (page1) PVFS 1-19vs.02
Pattern Description Origin Performance Remarks Safety
Example 1

One module
warmer than others
Module could be
open circuited - not
connected to the
system
Module normally
fully functional,
Check wiring

Example 2

One sub-string of
serially connected
cells is warmer than
others in the mod-
ule
Open circuited sub-
string
- Disconnection in
junction box or sub-
string
Sub-string
power lost,
reduction of Voc
May have burned
spot at the module.
Replace PV mod-
ule.

Example 3

One substring over-
heated with irregu-
lar pattern
Short circuited by-
pass diode or short-
circuited substring
Sub-string
power lost,
reduction of Voc
Replace module
Example 4

A single cell ap-
pears warmer,
while there are mul-
tiple warmer cells
with an irregular
pattern in the paral-
lel-connected sub-
string.
Shaded or defected
cell (bypass diode
activation)

Power decrease not
necessarily perma-
nent, e.g. shadow-
ing leaf or lichen
Visual inspection
needed, cleaning
(cell mismatch).

Example 5

Single cells are
warmer, not any
pattern (patchwork
pattern) is recog-
nized
Whole module is
short circuited
- All bypass diodes
short circuited
- Array wiring failure
Module power dras-
tically reduced (al-
most zero), strong
reduction of Voc
Check wiring
(see PVFS 1-15)

Example 6

Single cells are
warmer, lower parts
and close to frame
hotter than upper
and middle parts.
Massive shunts
caused by potential
induced degrada-
tion (PID) and/or
polarization
Module power and
FF redu-
ced. Low light per-
formance more af-
fected than at STC
Change array
grounding condi-
tions. Recovery by
reverse voltage
(see PVFS 1-10)

Example 7

One cell clearly
warmer than the
others
- Low Isc perfor-
mance of cell
- Shaded or de-
fected cell
Power decrease not
necessarily perma-
nent, e.g. shadow-
ing leaf or lichen
Visual inspection
needed, cleaning
(cell mismatch)
(see also PVFS 1-
1, 1-3, 3-3)

Example 8

Part of a cell is
warmer
- Low Isc perfor-
mance of cell
- Shaded or de-
fected cell
- Disconnected
string interconnect
Power decrease not
necessarily perma-
nent, e.g. shadow-
ing leaf or lichen,
FF reduction
Visual inspection
needed, cleaning
(cell mismatch). Re-
place PV module
(see also PVFS 1-
1, 1-7, 1-9)

## Página 60

60
EXAMPLES (page2) PVFS 1-19vs.02
Pattern Description Origin Performance Remarks Safety
Example 9

Point heating - Formation of mi-
cro-arc in the inter-
connection circuit
- Junction break-
down at cell caused
by shading
Power reduction

Crack detection af-
ter detailed visual
inspection of the
cell possible.
Replace PV module
(see also PVFS 1-
1, 1-7, 1-9)

Example 10

Sub-string part re-
markably hotter
than others when
equally shaded
Sub-string with
missing or open-cir-
cuit bypass diode
Massive Isc and
power reduction
when part of this
sub-string is
shaded
May cause severe
fire hazard when
hot spot is in this
sub-string
(see also PVFS 1-
15, 3-3)

Reviewed typical IR image patterns observed in outdoor measurements [Köntges14].

## Página 61

61
Component
Defect
Module
Soiling PVFS 1-20vs.01
Appearance Soiling is visible as a deposition of dust, dirt or other contaminants on the surface of a PV
module. The deposition can be uniform or non-uniform and vary in thickness. Due to the pres-
ence of hot-spots caused by non-uniform soiling, it can be also seen through IRT imaging.
Detection VI, (IRT, MON)
Origin Soiling of PV modules can have various origins such as dust accumulation, air pollution, bird
droppings or growth of moss, lichens or algae. It can be due to natural sources, as sand in
desert areas, seasonal pollen or volcanic emissions, or due to human activities, as near min-
ing, industry, high ways, railways, urban or agricultural surroundings. The soiling level and its
persistence over time depends on the exposure time, the chemical composition and particle
size as well as the local climate conditions. Whereas rainfalls and wind can lead to a natural
cleaning of modules, humidity can have a contrary effect by increasing adhesion and cemen-
tation of dust on the module. The module design (e.g glass coating, frame, distance of cells
from the edge), the orientation (e.g tilt angle, azimuth, landscape/portrait) and mounting con-
ditions (e.g clamps, height above ground, stringing) of the modules plays an important role.
Typically soiling increases as tilt angles decreases. The direction of the wind or obstacles can
influence the soiling process, leading to non-uniform patterns on system and module level.
Production  Installation Operation
Impact The deposited soiling layer causes optical losses, reducing the amount of light that reaches
the solar cells, with a consequential performance drop. Soiling is not a real module failure, as
it is reversible when the module is cleaned, but it has a negative impact on the lifetime energy
yield and financial return. Soiling is a site -specific issue. In arid re gions with seasonal dry
periods and dust, extreme soiling losses of up to 25%/a are reported, if modules are not
cleaned. In temperate regions with year-round rain, the annual soiling losses typically ranges
between 0% to 4%. In case of specific soiling sources (e.g. railway, farming, etc.) and/or con-
straints of the natural cleaning effect due to unfavourable mounting conditions (e.g low tilt
angle) much higher losses can be observed. Non -uniform soiling leads to current mismatch
losses which further increa ses the power loss and to hot -spots which in extreme cases can
permanently damage a PV module. In modules affected by potential induced degradation
(PID), soiling can further accelerate the ongoing degradation effect. Soiling can be mitigated
by cleaning t he modules or preventing excessive soiling. The cleaning approach has to be
appropriate to the type of soiling and site specific conditions (e.g. accessibility and water avail-
ability).  The cleaning schedule should take into account that natural agents, such as rain-falls,
wind or dew can have a natural cleaning effect at no cost. Anti-soiling coatings (ASC) can help
in reducing soiling and stretch the cleaning frequency, but only if the coating is adequate for
the type of soiling present on the system and if adequate cleaning processes are followed,
which do not damage the coating. Moreover, it has to be considered that some ASC can also
increase transmission losses by themselves.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Cleaning by qualified persons is
recommended when the reve-
nue lost because of the missed
energy production is higher than
the cleaning cost. A best time to
clean should be defined.
Preliminary site inspections
for the assessment of the
soiling risk. Cost estimation
for the implementation of
mitigation measures. Regu-
lar visual inspections to con-
trol the soiling level.
Estimation or measurement of
soiling losses prior to installa-
tion. Installation of soiling sen-
sors to determine the most
profitable time to clean.

## Página 62

62
EXAMPLES (page1) PVFS 1-20vs.01
Examples
1-3

Uniform light soiling, which in
ideal conditions is self -cleaning
when raining [By the courtesy of
SUPSI PVLab].
Uniform heavy soiling caused by
rail way station [ By the courtesy
of SUPSI PVLab].
Non-uniform soiling caused by
low inclination and close mount-
ing to roof [ By the courtesy of
SUPSI PVLab].
Severity
Examples
4-6

Moss growing on the edge of a
module combined with edge soil-
ing [Köntges17].
Soiling pattern on a system in the
Atacama desert [By the courtesy
of ISE FhG].
Soiling pattern demonstrating
dominant wind direction on a test
site in Atacama desert [ By the
courtesy of ISE FhG].
Severity
Examples
7

Heavy biofilm soiling [Könt-
ges16].

Severity

## Página 63

63
Component
Defect
Cables and Interconnectors
DC connector mismatch PVFS 2-1vs.01
Appearance Combination of male and female DC-connectors of two different manufacturers or types
(cross-mating) between modules, strings, arrays or to the inverter.
Detection VI, (IRT)
Origin There is yet no standard for PV connectors prescribing dimensions and tolerances. Therefore,
it is possible to find very similar-looking and even apparently fitting connectors on the market,
advertised as ‘compatible’.  Slight differences in the design of the connector can lead to re-
duced water and vapour tightness. Problems may also occur due to incompatibilities of mate-
rials (chemical incompatibility or different thermal expansion parameters) of the metal contact,
gaskets or sealings. Most of the time the  mismatch of connectors occurs at the string end
where extension cables are used or when connecting an inverter or a string combiner box,
which has been delivered with incompatible connectors.
Production  Installation Operation
Impact The interconnection of connectors from different manufacturers may significantly increase the
risk of loss of performance and defects which cause hazards for human and environment [IEC
TR 63225:2019]. The consequences are e.g. contact corrosion, burnt connectors, electrical
arcing and in the worth case a fire. One of the most common failures is that no current will
flow through the connection at all. The problems do not manifest themselves right away, but
only over time with increasing contact resistance and/or degradation of the connector/s. At
humid weather conditions mismatching connectors can also lead to a par tial failure of the in-
verter or a ground fault. The fire risk is further increased when the connectors are not properly
positioned and are close to flammable material such as wooden roof beams or heat-insulation
materials. Often connectors are at least par tly installed at position where they cannot be in-
spected during normal visual inspections (e.g. within profiles, underneath roof parallel modules
or even in BIPV). In combination with the unclear compatibility issue, the interconnection of
different brand or type of connectors may result in high risks.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
All not matching connect-
ors should be replaced.
Ask supplier or check mod-
ule/inverter spec sheets for
the type/manufacturer of con-
nector, only connectors from
the same manufacturer and
certified as compatible should
be mated together.
Verify that both modules and
inverters are delivered with
the same connectors. Provi-
sion of spare connectors and
string cables with connectors
of the same type as the mod-
ule connectors.

## Página 64

64
EXAMPLES (page1) PVFS 2-1vs.01
Examples
1-2

Connectors (male of female) are
of different brand or type and ob-
viously do not match [Moser17].
Connectors (male of female) are
of different brand or type and ob-
viously do not match [Moser17]

Severity
Examples
3-5

Corroded connector due to cross-
mating [ By the courtesy of
Stäubli].
Melted connector due to cross-
mating [ By the courtesy of
Stäubli].
Burned connector due to cross-
mating [ By the courtesy of
Stäubli].
Severity
Examples
6-7

Different types of connectors recognisable by dif-
ferent body mouldings and cable gland nuts [ESV
guide].
Different types of connectors recognisable by dif-
ferent ‘O’ rings or logos [ESV guide].
Severity

## Página 65

65
Component
Defect
Cables and Interconnectors
Defect DC connector/cable PVFS 2-2vs.01
Appearance A damaged connector or cable appear as melted, burned, brittle, broken, cracked or whitened.
Opened connectors can demonstrate corrosion.  Affected connectors show very often over-
heating or hot spots in an early state if a thermography check is performed.
Detection VI, (IRT)
Origin One of the major causes of damaged connectors are the combination of incompatible compo-
nents (DC connector mismatch), a low quality connector or a bad installation. In the last case
the connectors are either not installed according the instructions (e.g. bad crimping or connec-
tion, exposure to rain or polluted before installation, installation of damaged connectors) or the
connectors are not fixed correctly exposing them over longer times to humidity or dirt without
allowing the connector to dry completely. In case of damaged cables the major causes are the
use of low quality material in production (e.g. insulation material or cupper w ires), an inade-
quate selection of components within the design phase (e.g. undersized cables, too large ca-
ble glands, inadequate IP classification or UV protection)  or an improper handling or fixing of
the cables in the installation phase (e.g. cable routing over sharp or abrading edges, hanging
cables close to connections, overly tight bending, missing or not correctly installed cable
glands or exposure to direct UV radiation).
Production  Installation Operation
Impact Damaged connectors or cables constitute a high safety risk and may lead to the power loss of
the whole string. The continuity of the circuit isn’t any more guaranteed and inverter failures
can occur (low insulation faults or inverter switch off), leading t o partial or complete power
losses. In the worst case damaged cables or not well-connected connectors may cause elec-
tric arcs. In many cases, the connectors and cables are much closer to flammable material
such as wooden roof beams or heat -insulation materials than the PV module laminate, in-
creasing the risk of fire.
Safety:   Performance:
Mitigation Corrective actions Preventive actions (recom-
mended)
Preventive actions              (op-
tional)
Components constituting a
direct safety risk should be
replaced. Regular inspec-
tions should be done to moni-
tor the status of the not re-
placed components.
Protection of connectors and
cables from humidity during
installation. Use of adequate
crimping tools. Installation
should be done by trained
personal.
Signature of a contractual
agreement for maintenance of
the warranty when connectors
are substituted by the in-
staller, perform regular sys-
tem inspections.

## Página 66

66
EXAMPLES (page1) PVFS 2-2vs.01
Examples
1-3

Weathered connector [Könt-
ges17].
Cracked connector [Köntges17]. Corroded connector [Könt-
ges17].
Severity
Examples
4-6

Not fully inserted or interlocked
connecter [Yang19].
Melted connector [Köntges17]. Cracked/disintegrated cable in-
sulation [Köntges17].
Severity
Examples
7

Incorrect crimping (right) versus correct crimping (left) [PVSurvey19].
Severity

## Página 67

67
EXAMPLES (page2) PVFS 2-2vs.01
Examples
8-10

Burned connector [Köntges17]. Corroded Cable [Köntges17]. Animal bite on cable [Könt-
ges17].
Severity

## Página 68

68
Component
Defect
Cables and Interconnectors
Insulation failure PVFS 2-3vs.01
Appearance A bad isolation of cables is not always visible by eye. An unequivocally detection is only pos-
sible through the measurement of the insulation resistance under dry or humid/wet conditions.
It can be sometimes deduced by the presence of degraded or damaged cables and/or con-
nectors. Under certain c ircumstances like after a rain fall or in the early morning when the
cables or connectors are exposed to humidity, this kind of defect can lead to inverter failures
(low insulation fault or inverter switch off).
Detection VI, (INS, MON)
Origin Isolation failures occurs as a result of a short-circuit. It is usually the result of a combination of
humidity and damaged or degraded DC cables or connectors.
Production  Installation Operation
Impact A low insulation resistance due to the cables or a connector does not lead to a performance
loss itself, until an inverter failure occurs. An isolation fault can however cause potentially fatal
voltages in the conducting parts of the system potentially exposing persons to an electric shock
hazard. Touching of non -insulated parts may cause severe injury, without the use of safety
gear and safe measuring instruments. In the worst case damaged cables or connectors may
cause electric arcs and initiate a fire.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Cables or connectors con-
stituting a direct safety risk
should be replaced. Regular
inspections should be done to
monitor the status of the not
replaced components.
Ground fault detection by in-
verter or other devices at all
time.
Regular system inspections.

## Página 69

69
Component
Defect
Cables and Interconnectors
Thermal damage in combiner box FS 2-4vs.01
Appearance Defects appearing in the combiner box as discoloured or burned cable interconnections or
fuses. Damaged parts can be found by visual inspection or infrared thermography (IRT).
Detection VI, IRT, (MON)
Origin Thermal damages in the combiner box can be due to the selection of inadequate components
(e.g underrated fuses or fuse holders), a not proper connection of DC cables (e.g improper
wire torqueing, missing fuses) or a wrong wiring of the modules/strings in the field or on-roof.
Production  Installation Operation
Impact This damage is caused by the excess heat generated in fuse holder and defect DC connect-
ors/cables. The partial or complete thermal damage of the combiner box leads to performance
losses, electrical shock hazards and risk of fire. Actions must be taken immediately by qualified
personnel to prevent further damage.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Replace the components with
defect or abnormal tempera-
ture.
Use IRT to check the compo-
nents and connection to find
poor connection or defect
components.

## Página 70

70
EXAMPLES (page1) FS 2-4vs.01
Examples
1-3

Burned terminal block of the
combiner box [TUV Rheinland].
Improper wire torqueing causes
a fire [Köntges16].
Connection show signs of corro-
sion [TUV Rheinland].
Severity
Examples
4

Connecting terminals show signs
of bur ning, have melted or
charred [TUV Rheinland].

Severity

## Página 71

71
Component
Defect
Mounting
Bad module clamping PVFS 3-1vs.01
Appearance Inadequate fastening or damage of the module or frame by the clamp.
Detection VI
Origin The installation instructions of the module and mounting structure from the manufacturer are
not followed. Typical errors at the planning and installation stage are: (a) use of inadequate
clamps for the selected module and/or mounting structure, e.g. sharp  edges damaging
glass/glass modules, wrong combination of clamps and modules or mounting structure (b) too
short and too narrow clamps or (c) the positions, kind or number of the clamps on the module
not being chosen in accordance with the manufacturer’s manual. Other errors are too exces-
sively or insufficiently tightened screws during the mounting phase.
Production  Installation Operation
Impact An improperly installed clamp compromises the integrity of the mounting system and the ability
of the module to stay in place under high wind or load conditions. The detachment of modules
can happen as series effect because the modules share the clamps with the module next to
it. Once one module is detached, the clamp immediately loses fixing force on the next module
and result in series detachment. The detachment of the module/s from the mounting structure
is posing a serious hazard to persons and the risk of damaging the rest of the system and/or
the property in the vicinity of the installation site. Problems such as frame damage, glass
breakage or cell cracks can occur compromising on the long term the performance and the
electrical safety.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Modules with a safety risk
or a severity of 5 should be
replaced.
Use only compatible clamps
(mounting structure/ modules/
clamps) and follow manufac-
turer mounting instructions.
Check local wind and snow
loads.
Testing of non -standard
mounting configurations by an
accredited test laboratory (eg.
facade mounting), perform
regular system inspections

## Página 72

72
EXAMPLES (page1) PVFS 3-1vs.01
Examples
1-3

Improper installation of clamp [By
courtesy of SUPSI PVLab].
Wrong combination of clamps
and modules [Moser17].
Glass breakage caused by too
tight screws [Herrmann21]. (see
also PVFS 1-8)
Severity
Examples
4

Glass breakage caused by poor
clamp design [Moser17]. (see
also PVFS 1-8)

Severity

## Página 73

73
Component
Defect
Mounting
Inappropriate/defect mounting structure PVFS 3-2vs.01
Appearance Mechanical damages (e.g cracking, bending) or other visual defects (e.g. corrosion of frame
or mounting holes) observable on the mounting structure.
Detection VI
Origin Typically, this failure occurs when the mounting structure is not designed to withstand the wind
or snow loads which are typical for the site in which the system is installed (e.g. mounting
structure does not comply with static calculations, underestimation of the environmental con-
ditions), or if the anchorage of the mounting structure to the ground or roof is weak (e.g. ground
conditions are not considered sufficiently when choosing the mounting structure). The roof
strength, to withstand the added load of the PV system and include allowance for O&M activ-
ities, is not verified. Another reason for the fai lure of a mounting structure is the use of inap-
propriate materials (e.g use of corrosive materials in a corrosive environment, insufficient gal-
vanisation, poor quality material due to a bad or missing quality assurance in production),
leading to a premature degradation or mechanical failure of the mounting structure. Installation
errors (e.g. missing/non-original components, excessively or insufficiently tightened screws)
can be the origin of a failure of the mounting structure.
Production  Installation Operation
Impact An inappropriate or damaged mounting structure compromises the integrity of the modules
mounted on it and in some cases also the substructure (e.g roof insulation). In the worst case
this leads to the detachment of single modules or the whole mounting stru cture from the roof
or ground, or roof collapses, posing a serious hazard to persons and the risk of damaging the
rest of the system and/or the property in the vicinity of the installation site.  Performance losses
are to be expected, depending on the damage on module level (number of disconnected mod-
ules/strings, glass breakage, cell cracks , back sheet damages , damaged or detached
junction box) and the time and labour needed to repair the system.  Galvanic corrosion is
important for the installation with two different metals in contact, for example aluminium frame
fixed on steel structure, especially in humid or costal area. Direct contact of different metals
generates galvanic corrosion which frequently happens around the fastening screws. There-
fore insulation between two different metals is required in humid and costal area.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Mounting structures with a
direct safety risk should be
replaced or repaired.
Use only compatible mount-
ing structures (ground/mount-
ing structure/modules) and
follow manufacturer mounting
instructions. Check local load
(conditions (wind, snow,
other).
Regular system inspections.
Testing of non -standard
mounting configurations by an
accredited test laboratory
(e.g. facade mounting), per-
form regular system inspec-
tions.

## Página 74

74
EXAMPLES (page1) PVFS 3-2vs.01
Examples
1-3

Corrosion due to salt water [Könt-
ges16].
Cracks in mounting structure due
to mechanical stress [Könt-
ges16].
Screw canal bends due to me -
chanical stress [Köntges16].
Severity
Examples
4-6

Bracket fractured due to
mechanical stress [Köntges16].
Undersized mounting structure
for local snow load conditions
[Köntges16].
Undersized mounting structure
for local wind conditions [In-
dia13].
Severity

## Página 75

75
Component
Defect
Mounting
Module shading PVFS 3-3vs.01
Appearance Depending on the position of the sun (day and time), shading can be seen either by eye when
performing a visual inspection, or by comparing monitoring data of unshaded and shaded
strings or by running shading simulations. The shade can have different patte rns and
change/move over the day and season.
Detection VI, (MON, IRT)
Origin The choice of the mounting structure and the position in which the modules are mounted in-
fluences the shading conditions. Shading can be caused by different factors or obstacles e.g
trees, antennas, poles, chimneys, satellite dishes, roof or façade protrus ions, near buildings,
cables, or by self -shading (inter array or row -to-row shading) or soiling. Shading conditions
can change over the lifetime of a PV system due to growing vegetation, new constructions or
construction elements. It can be distinguished b etween different types of shades: direct
shades hindering the direct light to reach the module or diffuse shades.
Production  Installation Operation
Impact A cell or module which does not receives or receives less sunlight due to a shading obstacle,
lowers the performance of a PV system. Typically, the cumulative annual shading loss of PV
systems is between 1 -5%, but energy losses up to 20 -30% can be observed for roof top or
façade systems.  Due to series connection of cells and modules, the power loss is significantly
higher than the shaded area. The final loss depends on the on-site implementation or shading
mitigation measures like optimised string and module arrangements (landscape mounting),
use of module-level power electronics (MLPEs), inverter characteristics (MPPT search algo-
rithms, string control) or the use of shading tolerant module technologies (e.g half -cut cells,
back contact cells). Shading itself does not pose a safety issue, but the hot-spots caused by
prolonged shading can lead to follow -up failures (e.g burn marks, bypass diode failures ,
glass breakage, arcing or fire). It further can result in an acceleration of the aging process
resulting into higher degradation rates. The right time to consider the impact of shading is at
the system planning phase, later it is usually too late. The use of MLPEs such as micro-invert-
ers and DC optimizers for individual modules can potentially increase performance under
shading conditions, but the gain achieved by these devices do not always exceeds the loss
caused by the MPLE device itself (lower efficiency), and the shading still activates the bypass
diode and result in hot spot on the shaded cell, which increases the risk of reliability issues.
The choice of using them only in the area wher e shading occurs should be considered an
alternative to install them for all modules. A cost benefit analysis should be done in any case.
Safety:   Performance:
Mitigation Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Indirectly damaged mod-
ules with a safety or sever-
ity risk of 5 should be re-
placed or repaired.  Eventual
trees or vegetation responsi-
ble for the increased shading
loss should be cut.
A basic shading analysis (full
year solar/shade data) is rec-
ommended to identify areas
and periods of major shading.
Areas exposed to shading
within the central part of the
day or sunny season should
be avoided or appropri-
ate/cost-effective shading mit-
igation measure should be im-
plemented.
A detailed shading loss analy-
sis should be done which esti-
mates and compares different
system configurations and
shading mitigation measures.
Perform regular system in-
spections.

## Página 76

76
EXAMPLES (page1) PVFS 3-3vs.01
Examples
1-3

Shading by pole -and-wire (poor
design: too close to nearby shad-
ing objects) [Jahn18].
Shading due to bad planning or
coverage by afterwards build con-
struction element. [Moser17].
Shading by tree with seasonal
changes due to foliage
[Moser17].
Severity
Examples
4-6

Missing maintenance on flat
green roof [By courtesy of SUPSI
PVLab].
Vertical shading of a standard
module with 3 bypass diodes [By
courtesy of J.Lin PV Guider].
Shading by balustrade [By cour-
tesy of J.Lin PV Guider].
Severity
Examples
7

Continuous shading caused by
chimney [ By c ourtesy of SUPSI
PVLab].

Severity

## Página 77

77
Component
Defect
Inverter
Overheating PVFS 4-1vs.01
Appearance The inverter reduces its power or switches off to protect components from overheating (tem-
perature derating). Inverters do not always deliver a corresponding status message "power
reduction" or "derating". For this reason, it is recommended to check the inverter behaviour by
determining and analysing performance curves (Power vs Irradiance).
Detection MON, (IV, IRT)
Origin Temperature derating of the inverter can occur for various reasons, e.g. improper installation
of the inverter, fan failure, dust blocking heat dissipation or an incorrect programming of the
inverters.
Production  Installation Operation
Impact When the monitored components in the inverter reach the maximum operating temperature,
the inverter shifts its operating point to a lower power. During this process, power is reduced
step-by-step. In the extreme case, the inverter switches off completely. As soon as the tem-
perature of the threatened components falls below the critical value, the inverter returns to the
optimal operating point. The partial or complete failure of the inverter leads to performance
losses, which will get worse if the problem is not solved. In the worst case inverter will switch
off. Inverter overheating do not affect module safety.
Safety:   Performance:
Action Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Once identified the origin of
the temperature derating the
failure should be repaired.
The filters and in general
heat dissipation path should
be cleared of obstruction.
Follow the given installation
procedure, use of adequate
cooling technology, perform
regular inspections of the ven-
tilation units.

Monitoring of inverter temper-
ature

## Página 78

78
EXAMPLES (page1) PVFS 4-1vs.01
Examples
1-3

Dust blocking heat dissipation
[By courtesy of TUV Rheinland].
A soiled air filter causes over-
heating [By courtesy of TUV
Rheinland].
Installation not appropriate (di-
rect exposition to sun) [By cour-
tesy of TUV Rheinland].
Severity

## Página 79

79
Component
Defect
Inverter
Incorrect installation PVFS 4-2vs.01
Appearance The inverter must be installed according to the installation instruction. A common failures  is
the installation near flammable, explosive, corrosive or humid sources. Also the minimum dis-
tances to bottom, top or to the sides are not always fulfilled. If the input cables are not fixed
properly, increased temperatures can occur at the loose contac t point which lead to lower
performance or risk of fire. Inverters must always be accessible for operation and maintenance
and properly secured to an appropriate base.
Detection VI (MON)
Origin Violating instruction manual, e.g. installed nearby flammable materials as wood or in direct
sun light.
Minimum distance to adjacent components not maintained.
Production  Installation Operation
Impact Incorrect installation of the inverter can cause danger to users and hazardous conditions and
can result in overheating of the inverter. The use of the inverter in the presence of flammable
vapours or gases can lead to explosions. The inverter housing can become very hot under
operation. Follow the instruction to provide gaps from both sides and top for adequate cooling.
Direct sunlight on the inverters must be avoided. The inverter must be safely accessible to
avoid accidents during maintenance work.
Safety:   Performance:
Action Corrective actions Preventive actions
 (recommended)
Preventive actions
(optional)
Dismount the component and
follow the installation proce-
dure.
Follow the given installation
procedure, use of adequate
cooling technology, perform
regular inspections of the ven-
tilation units.
Monitoring of inverter temper-
ature.

## Página 80

80
EXAMPLES (page1) PVFS 4-2vs.01
Examples
1-3

Installation in direct sun light [By
courtesy of TUV Rheinland].
Inverters are not or difficult ac-
cessible for operation and
maintenance [ By courtesy of
TUV Rheinland].
Distance to bottom, top or to the
sides too low [ By courtesy of
TUV Rheinland].
Severity
Examples
4-5

Housing not appropriate [ By
courtesy of TUV Rheinland].
Presence of inflammable mate-
rial [ By courtesy of SUPSI
PVLab].

Severity

## Página 81

81
Component
Defect
Inverter
Not operating (complete failure) PVFS 4-3vs.01
Appearance If the inverter does not work despite good production conditions, common problems are the
lack of restart after grid faults or isolation faults. The inverter may show fault codes to help
understanding the problem. This can be observed by checking the display or the data log of
the monitoring system. Examples for hardware defects in the inverter are discoloured or
burned cable interconnections or fuses. Damaged parts can be found by visual inspection or
infrared thermography (IRT).
Detection MON, (VI, I-V, VOC)
Origin A complete failure of the inverter occurs due one or more malfunctions of single hardware or
software component of the inverter or faults due to grounding issues, e.g. high humidity inside
the inverter, or a firmware issue.
Production  Installation Operation
Impact The complete failure of the inverter leads to significant performance losses and immediate
actions must be taken. When the restart does not work or the fault occurs recurrently the origin
must be identified in most cases by a service team. Software issues can be solved by updating
the firmware for technical reasons or to update the system to new standards/grid technical
requirements. While damaged hardware components of central inverters are usually repaired,
string inverter are replaced more often for economic reasons. Damaged hardware can cause
fire and electric shock hazards and must be repaired by qualified personnel.
Safety:   Performance:
Action Corrective actions Preventive actions
(recommended)
Preventive actions
(optional)
Restart the inverter. Replace
the components with defect or
abnormal temperature. Up-
date the software.
Use IRT and VOC to check
the components and connec-
tion to find poor connection or
defect components.

## Página 82

82
EXAMPLES (page1) PVFS 4-3vs.01
Examples
1-3

Insulation failure [TUV Rhein-
land]
Not operating inverter [TUV
Rheinland].
Damaged hardware compo nent
[Sinclair17].
Severity

## Página 83

83
