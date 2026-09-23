# IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure

Fonte original: `IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf`

## Página 1

Degradation and Failure
Modes in New Photovol-
taic Cell and Module
Technologies
2025
PVPS
Task 13  Reliability and Performance of Photovoltaic Systems

Report IEA-PVPS T13-30:2025

## Página 2

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies

What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organization for Ec onomic
Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with a belief that the future of energy
security and sustainability starts with global collaboration. The programme is made up of 6.000 experts across government, ac ademia, and
industry dedicated to advancing common research and the application of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCP’s within the IEA and was established in 1993. The mission
of the programme is to ‘enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone
in the transition to sustainable energy systems ’. In order to achieve this, the Programme’s participants have undertaken a variety of joint
research projects in PV power systems applications. The overall programme is headed by an Executive Committee, comprised of one dele-
gate from each country or organisation member, which designates distinct ‘Tasks’, that may be research projects or activity areas.
The IEA PVPS participating countries are Australia, Austria, Belgium, Canada, China, Denmark, Finland, France, Germany, India, Israel,
Italy, Japan, Korea, Malaysia, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain, Sweden, Switzerland, Thai land, Turkiye,
and the United States of America. The European Commission, Solar Power Europe and the Solar Energy Research Institute of Singapore
are also members.
Visit us at: www.iea-pvps.org
What is IEA PVPS Task 13?
Within the framework of IEA PVPS, Task 13 aims to provide support to market actors working to improve the operation, the reliability and the
quality of PV components and systems. Operational data from PV systems in different climate zones compiled within t he project will help
provide the basis for estimates of the current situation regarding PV reliability and performance.
The general setting of Task 13 provides a common platform to summarize and report on technical aspects affecting the quality, performance,
reliability and lifetime of PV systems in a wide variety of environments and applications. By working together across national boundaries, we
can all take advantage of research and experience from each member country and combine and integrate this knowledge into valu able
summaries of best practices and methods for ensuring PV systems perform at their optimum and continue to provide competiti ve return on
investment.
Task 13 has so far managed to create the right framework for the calculations of various parameters that can give an indication of the quality
of PV components and systems. The framework is now there and can be used by the industry who has expressed appreciation towards the
results included in the high-quality reports.
The IEA PVPS countries participating in Task 13 are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany,
Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand,  the United States of America,  and the Solar Energy
Research Institute of Singapore.

DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and publica-
tions of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual member countries.
COVER PICTURE
Infrared image of an energised module string at night. One module has a not connected bypass diode. Thanks to photovoltaikbuero Ternus & Diehl GbR  for the
permission to use the image.
ISBN 978-3-907281-71-0: Task 13 Report: Degradation modes and Failure in New PV Cell and Module Technology

## Página 3

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies

INTERNATIONAL ENERGY AGENCY
PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

IEA PVPS Task 13
Reliability and Performance
of Photovoltaic Systems

Degradation and Failure Modes in New
Photovoltaic Cell and Module Technologies

Report IEA-PVPS T13-30:2025
February 2025

ISBN 978-3-907281-71-0

## Página 4

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
4
AUTHORS
Main Authors

Marc Köntges, ISFH, Germany
Jay Lin, PV Guider
Alessandro Virtuani, CSEM, Switzerland
Gabriele C. Eder, OFI, Austria
Junjie Zhu, IFE, Norway
Gernot Oreski, PCCL, Austria
Peter Hacke, NREL, USA
Joshua S. Stein, SNL, USA
Laura Bruckman, CWRU, USA
Paul Gebhardt, Fraunhofer ISE, Germany
Dounya Barrit, Total Energies, France
Mirra Rasmussen, CWRU, USA
Ina Martin, CWRU, USA
Kristopher O. Davis, UCF, USA
Gianluca Cattaneo, CSEM, Switzerland
Bram Hoex, UNSW Sydney, Australia
Ziv Hameiri, UNSW Sydney, Australia
Ebrar Özkalay, SUPSI, Switzerland

Contributing Author
 Sara Baumann, ISFH, Emmerthal, Germany

Editors
 Marc Köntges, ISFH, Germany
 Jay Lin, PV Guider
 Ulrike Jahn, Fraunhofer CSP, Germany

## Página 5

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
5
TABLE OF CONTENTS
Acknowledgements ................................................................................................... 6
List of abbreviations .................................................................................................. 7
Executive summary ................................................................................................... 8
 Introduction ...................................................................................................... 10
 Degradation and Failure modes in recent technologies entered the market ..... 11
2.1 Cut Si wafer-based cell cracking and multi-wire design .......................... 11
2.2 Light-induced degradation ....................................................................... 12
2.3 Potential-induced degradation ................................................................ 14
2.4 Protection of substrings in the modules................................................... 24
2.5 Encapsulation degradation and failure modes ........................................ 29
2.6 New material degradation modes specific to TOPCon and SHJ ............. 38
 Perovskite-based future technologies .............................................................. 44
3.1 Intrinsic degradation causes ................................................................... 44
3.2 Cell-device-specific degradation modes .................................................. 45
3.3 Extrinsic degradation causes .................................................................. 46
3.4 Module-device-specific degradation modes ............................................ 46
 Conclusion ....................................................................................................... 48
References ............................................................................................................. 50

## Página 6

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
6
ACKNOWLEDGEMENTS
This report received valuable contributions from several IEA  PVPS Task 13 members and
other international experts. Many thanks to:
Eckhard Fleiss from Ingenieurbüro Fleiß for giving the permission to use his drawing as tem-
plate for Figure 14 and Matthias Diehl from photovoltaikbuero Ternus & Diehl GbR for allowing
us to use the cover image.
This report is supported by the German Federal Ministry for Economic Affairs and Climate
Action (BMWK) under contract no. 03EE1120A, 03EE1120B and 03EE1120C, the Swiss Fed-
eral Office of Energy (SFOE) under the contract no. SI/ 502398-01, the Austrian Federal Min-
istry for Climate Action, Environment, Energy and Mobility (BMK), the Danish Energy Technol-
ogy Development and Demonstration Programme (EUDP), project number 134- 22016, "IEA
PVPS Task13 -  Reliability and performance of photovoltaic systems ”, and the Austrian Re-
search Agency (FFG) under contract no. FO999908094_05102023_160512119.
This work was authored in part by the National Renewable Energy Laboratory, operated by
Alliance for Sustainable Energy, LLC, for the U.S. Department of Energy (DOE) under Contract
No. DE-AC36-08GO28308 in the project 38263 “R&D to Ensure a Scientific Basis of Qualifi-
cation Tests and Standards,” funded by the U.S. Department of Energy, Office of Energy Effi-
ciency and Renewable Energy, Solar Energy Technologies Office. The views expressed in the
article do not necessarily represent the views of the DOE or the U.S. Government.
Sandia National Laboratories is a multi-mission laboratory managed and operated by National
Technology and Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honey-
well International Inc., for the U.S. Department of Energy’s National Nuclear Security Admin-
istration under contract DE-NA0003525.

## Página 7

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
7
LIST OF ABBREVIATIONS
Al-BSF Aluminium back surface field MHP Metal halide perovskite
ARC Anti-reflective coating OC Open-circuit
a-Si Hydrogenated amorphous Si PA Polyamide
BOM Bill of materials PERC Passivated emitter and rear cell
BPD Bypass diode PERT Passivated Emitter and Rear
Totally Diffused
c-Si Crystalline Si PET Polyethylene terephthalate
CTE Coefficient of thermal expansion PID Potential-induced degradation
CTL Charge transport layer PID-p PID-Polarisation
DH Damp heat PMMA Poly (methyl methacrylate) poly-
mer
EL Electroluminescence PMPP/Pmax Maximum power
EPE EVA-POE-EVA PO Polyolefin
EVA Ethylene-Vinyl-Acetate POE Polyolefin elastomer
FA Formamidine PSC Perovskite solar cell
FF Fill factor PV Photovoltaic
HF Humidity freeze PVDF Polyvinylidene fluoride
IBC Integrated-Back Contact PVF Polyvinyl fluoride
IEA International Energy Agency PVFS Photovoltaic Failure Fact Sheets
IEA
PVPS
IEA Photovoltaic Power Sys-
tems Programme
RH Relative humidity
IEC International Electrotechnical
Commission
SEM Scanning electron microscopy
IRT Infrared thermography SHJ  Silicon Hetero-Junction
ISC (JSC) Short Circuit Current (density) TC Thermal cycling
ITO Indium tin oxide TCO Transparent Conductive Oxide
ITRPV International Technology
Roadmap for Photovoltaic
TCP Technology Collaboration Pro-
gramme
IV Current-Voltage TOPCon Tunnel Oxide Passivated Con-
tact
LCOE Levelized cost of electricity UV Ultraviolet
LeTID Light and elevated temperature
-induced degradation
UVID UV induced degradation
LID Light-induced degradation VOC Open-circuit voltage

## Página 8

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
8
EXECUTIVE SUMMARY
The levelized cost of electricity (LCOE) of photovoltaic applications depends on, among other
things, the performance, price and durability of the photovoltaic (PV) module. Performance and
price can be determined with little effort. Durability is the least known of these three factors. In
this report, we evaluate the impact of degradation/failure modes of innovations in the market.
The reliability situation of Tunnel Oxide Passivated Contact ( TOPCon) and Silicon Hetero-
Junction (SHJ) is shown in Figure 1 for selected degradation and failure modes. Especially
semiconductor-related degradation modes show degradation and recovery paths : light (and
elevated temperature)-induced degradation (LeTID/LID), UV-induced degradation (UVID), and
potential-induced degradation (PID). Their impact can only be assessed if the degradation and
recovery paths are understood, and a test method is available. Common degradation modes
or failures related to embedment, glass and junction box are shown in Figure 1 on the right.
Current standard tests, especially of the IEC 61215 standard, cannot reveal these degradation
or failure modes. As these modes are safety relevant, it is important to understand the causes
and develop standardized tests to identify these reliability problems.

Figure 1: Overview of test availability and impact of currently relevant degradation
modes of TOPCon and SHJ module designs.
In the following we go through  degradation modes which changed with new innovation. We
find that the impact of cell cracking has been mostly overcome by the innovation of multi-wire
technology. Also, LID/LeTID has been well understood and solved by switching from Boron to
Gallium as a dopant for Si-wafers, by using adjusted processes in the cell production together
with the use of  thin wafers, and lowering the number of impurities in the wafer production.
Furthermore, standard test procedures are available , so that the LID/LeTID impact on long-
term performance can be tested even for innovation. The degradation mechanisms which lay
behind PID can be triggered and mitigated at cell, module and system level. These degradation
mechanisms are caused by high system voltage and may be influenced by light , in particular
UV irradiation. PID tests for modules with Passivated Emitter and Rear Totally diffused (PERT)
cells have shown that additional light during a PID test can effectively prevent degradation. It
has been shown in one case that an UV irradiance equivalent to the UV content in the standard
AM1.5 spectrum at 1000 W m-2 can reduce the PID effect for a module with TOPCon cells to
below 3%. In contrast, in this case no UV irradiation during the PID test leads to a degradation
of 28%. For PV modules with SHJ cells a new potential PID degradation mechanism is identi-
fied. However, no PID affected modules are found in the field corresponding to this mode, yet.

## Página 9

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
9
To assess the irradiation impact on real installations , the upcoming PI D standard IEC
TS 62804-1 (2025) offers a combined potential and light test procedure.
In some solar modules with TOPCon and SHJ cells, UVID is pronounced after accelerated
aging tests. It is still un clear whether the degradation can be reversed by outdoor exposure
and how the test can be transferred from laboratory to field, since many interacting mecha-
nisms influence UV degradation and recovery. It must be emphasized that the UVID is a solv-
able problem, since some modules in accelerated tests are  UV-stable. The reflection or ab-
sorption of UV radiation before it reaches the c-Si/passivation interfaces (e.g. by the encapsu-
lation material) can mitigate the UVID.
For encapsulant materials standardized PV module tests (e.g., of the IEC 61215 series or other
PV safety standards) often do not reveal relevant degradation paths as their focus is on the
electrical performance of the PV modules and not on the polymer materials stability. Therefore,
many PV modules are found in the field with damaged lamination material. Combined stresses
with e.g. temperature change, humidity and UV radiation can reveal these polymer-related
degradation paths. Especially for these degradation modes , new combined aging tests are
required as discussed in detail in the IEA PVPS TASK 13 sister report “Accelerated testing -
combined stress vs. sequential stress testing methods and inclusion of specific load situa-
tions”. As degradation of encapsulation material is not recoverable and often lead s to safety
issues, these additional tests are recommended for new encapsulant materials.
In practice, thin glass (thickness ≤ 2 mm) used in new glass/glass modules sometimes results
in unpredictable high glass breakage rates.  In documented cases 5% to 10% of the module
rear glasses broke in the first two years after installation . The mechanical load test in
IEC 61215 cannot reveal this vulnerability, as it would need parallel tests on tens of modules,
instead of only one, to assess the failure rate. Currently, only a high number of tests in the final
mounting position can reveal the stability of thin glass modules.
More frequently than before, i t happens that electrical contacts in the junction boxes are not
soldered correctly. This may mean that the bypass diodes (BPDs) are not properly contacted.
Faults in the junction box can lead to fires and power losses in entire module strings. However,
unconnected BPDs are difficult to detect in PV systems that have already been installed. It is
therefore recommended to check the function of 100% of the BPDs during production. A PV
system installation should be 100% tested if there are indications that this type of failure is
occurring in the selected modules.
This report also includes a concise summary on the reliability of metal halide perovskite (MHP)-
based PV modules according to the current scientific literature. There are many known degra-
dation paths for which remedies exist at the conceptual or laboratory level. For example, pro-
tective encapsulation against UV radiation, moisture and oxygen basical ly helps to stabilize
the perovskite solar cells (PSCs). However, besides others, two prominent challenges are the
temperature and the ion migration stability. The limited temperature stability and the high ion
mobility lead to unsolved degradation paths under  normal operation conditions like shading
and high system voltage. There are new degradation modes in tandem solar cells with MHPs.
For example, the reverse voltage states occurring in the top and bottom cells during shaded
conditions depend on the irradiation spectrum and cannot yet be reproduced by standard qual-
ification tests. New tests addressing this shading condition are important to evaluate new deg-
radation pathways that do not occur in single junction PV modules.
To produce reliable PV modules, all degradation pathways must be understood and mitigated
in one solution. There are currently no comprehensive solutions in the literature to address the
multiple reliability issues of PSCs.

## Página 10

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
10
 INTRODUCTION
The previous IEA PVPS reports on PV module failure s [1], their assessment [2] and quantifi-
cation of technical risks [3] are still relevant documents for assessing and mitigating of degra-
dations and failures in PV modules. A degradation mode is a n observable specific change
mechanism of a PV module like it is defined by Jordan et al. [4] that can (but does not have to)
lead to a failure mode. For the word “failure” we use the definition from Köntges et al. [1] where
a failure in a PV module means that the power warranty of a module is no longer fulfilled or the
safety of a PV system is affected. A failure mode is a specific type of failure. With this document
we like to target a broad audience starting from cell and module manufactures up to PV system
owners. As in the former reports , we strongly focus on Si -wafer-based solar modules  here.
However, the PV module technology has developed fast. This document aims to give an up-
date of degradation mechanisms and currently important failures in current PV cell and module
technologies.
Chapter 2 therefore presents in-depth information on degradation mechanisms and potential
mitigation strategies on production level. We start with degradation mechanisms (cell cracks,
LID, LeTID) which had been important in the former review but lost importance within current
(2023) PV module products. Thereafter, we present degradation modes which are still relevant
for PV module technologies (PID, substring protection and module embedment) and which
show specific differences to former reviews mentioned above. At the end of chapter 2 we an-
alyse degradation modes which are specifically relevant for the current cell technologies TOP-
Con and SHJ.  This breaks the strict sorting along degradation and failure modes but allows
the reader to quickly read about all special degradation modes for TOPCon and SHJ. All chap-
ters contain an explanation of the degradation mode, its impact on module/system level, how
to identify it, how to test it, and if possible, how to mitigate the degradation mode. All sections
contain numerous up-to-date references to the most relevant publications , if additional infor-
mation is needed.
Due to the rapidly growing development of MHP -based solar cells and modules, we report in
chapter 3 on their known degradation modes and existing mitigation strategies. Chapter 3 is
addressed to the scientific interested reader as all available data is extracted from scientific
publications. We have no information on degradation modes of market available MHP -based
modules.
In the previous  IEA PVPS Task 13 report by Herz et al. [3]  PV-related failures have been
collected and systematised in Photovoltaic Failure Fact Sheets  (PVFS) for the first time. For
the application related reader these PVFS have been updated with the content of this work
and can be downloaded as a separate document from the IEA PVPS website area [5]. These
fact sheets explain all needed information for the application , such as how to detect a failure
or degradation, information on safety and power production,  and how to mitigate the problem
if possible. Unfortunately, not all degradation and failure modes  have been transferred to the
PVFS, as there is not always enough material available to visualise the failure  and provide
clear recommendations for action. Especially for MHP-based solar cells and modules no PVFS
exists, yet.

## Página 11

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
11
 DEGRADATION AND FAILURE MODES IN RECENT
TECHNOLOGIES ENTERED THE MARKET
Photovoltaic module technologies and their application profile s evolve with time. As the deg-
radation modes are always related to technologies and their application profile they also
change with time. The testing sequences defined by the International Electrotechnical Com-
mission (IEC) in the IEC 61215 series standard [6]  are a good way to assess that new tech-
nologies degrade slow enough in the application. However, testing is always a compromise
between finding failures and test simplification. The test simplification may lead to false positive
or false negative results  for new technologies . One prominent example is the PID of PERT
cells which may degrade in a PID test under dark conditions, but under realistic conditions the
sunlight compensates for the PID effect, so the degradation is not relevant in the application.
In the following, we discuss if the most relevant degradation mechanisms already described in
previous PVPS TASK 13 reports [1], [2] which are changed due to new innovations. After-
wards, we discuss new technologies, the knowledge about their degradation modes, and their
relevance for the application.
2.1 Cut Si wafer-based cell cracking and multi-wire design
The cutting of Si wafer-based cells in half cells or 1/3rd cells increases the risk of cracking at
the cutting cell edge when preparing modules from the cells. Cutting of Si cells into half or even
in one third by a laser ablation process introduces small micro cracks into the groove area of
the laser ablation process. Hwang et al. shows that with increasing crack opening width in the
laser groove surface, the break force needed to break the cells in a 4- point bending test de-
creases [7]. They also show that the number of broken cells in a module increases with in-
creasing micro crack opening in the laser groove surface. Module power measurements after
a mechanical load test show that the number of cracked cells and the power loss increases
with the crack opening in the laser groove. For multi -wire solar modules, the power loss due
to cell cracks is reduced compared to former ribbon-based modules. Hwang et al. show 0.2%
power loss per dendritic-like cracked half-cell for a multi-wire Passivated Emitter and Rear Cell
(PERC) cell in the module [7]. For a relevant power loss of 5% one needs about 25 dendritic -
like cracked cells. So, cell cracks still influence the module power for multi -wire connected
halved cells, but the final impact on the module power is low. Thermal laser separation method
can be used to reduce cell cracking in cut solar cells compared to laser ablation method [8].
Figure 2 a) shows that small cracks induced at the cut edge may already exist after production.
They are ignored at this stage but frequently grow into dendritic cracks during transportation
and installation, as well as mechanical loads and temperature variations that may occur in the
field. Figure 2 b) shows the electroluminescence (EL) image of one of these glass /backsheet
modules tested on arrival at the installation site.
The same batch of modules was delivered to two different sites and an EL inspection of 50
modules was performed on arrival at each site. The defects are categorised as major defects
when dendritic cracks are found, simple branch cracks are categorised as minor defects, and
few single cracks are categorised as normal.
At one site the defect rate was 78% major, 18% minor and 4% normal, whereas  at the other
site the defect rate was 70% major, 30% minor, and no normal modules. Dendritic cracks per
cell result only in ~0.2% of power loss in the module . However, this kind of cracks can occur

## Página 12

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
12
with a high proportion of cells in the module and the total power loss could be noticeable, but
very small for PV systems.
For glass/glass modules the cell crack occurrence is typically very low. To our best knowledge,
all papers on PV module degradation caused by cell cracks are based on 2 to 4 cell intercon-
nect ribbons per cell with full cell module design. In this way, according to our present
knowledge, no field degradation data on cut cell and multi-wire designs are available.

Figure 2: a) Cracks induced at the edge of laser cutting during module production. b)
The cell cracks appeared after transportation while they were not seen in the final EL
inspection in the module production line. The current inactive cell areas are below
5% per cell.
2.2 Light-induced degradation
In recent times, light-induced degradation phenomena had been a large effect on some multi-
crystalline and PERC-based solar cell types. Therefore, through this chapter we discuss the
relevance of new developments in wafer and cell technology regarding to  the light-induced
degradation modes.
2.2.1 Boron related light-induced degradation
Light-induced degradation is the phenomenon of cell and module power degradation due to
incident light. The main degradation mechanism is based on the formation of Boron- Oxygen
complexes (B -O LID) and was particularly strong in Czochralski -grown Si mono-crystalline
cells, in part due to its high oxygen concentration [9]. The maximum degradation of LID typically
happens within the first few hours of light exposure and it may amount to several percent rel-
ative to the initial module performance. After the degradation phase, a slow recovery can
sometimes be observed upon further operation, which is often difficult to quantify in the field,
because it is superimposed by other degradation or weather effects.
In recent years, the prevalence and severity of LID in PV modules has dropped significantly
due to the usage of Ga instead of B as dopant in p-type cells. In theory this exchange removes
the possibility to form B-O complexes due to the absence of B atoms. Nevertheless, LID may
still be observed in Ga- doped p-type [10] and even in n -type cells [11] , due to B impurities
present in the wafers. Due to the generally low number of impurities (B and Fe) in today's Si
wafer the relevance of LID is low for nearly all current PV modules based on Ga p-type and n-
type doping.

## Página 13

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
13
2.2.2 Light and elevated temperature-induced degradation
Light and elevated temperature-induced degradation (LeTID) is a degradation mechanism that
mainly affects p-type PERC modules. The exact mechanism is linked to hydrogen-related de-
fects, which become active under the combined thermal and light stress  conditions, causing
minority charge carrier recombination and therewith reduced power output. Regeneration oc-
curs when the defects responsible for degradation are gradually passivated under controlled
thermal or electrical conditions. This process typically involves the redistribution and reactiva-
tion of hydrogen, leading to the recovery of cell efficiency over time. Due to its degradation -
regeneration behaviour through the first years of operation, it can lead to significant yield loss
in field operation (sometime reaching values over 10%). Similarly to LID, a regeneration phase,
that is largely influenced by weather and seasonal effects, can be observed in the years after
the maximum degradation has been reached [12], [13].
Based on a mechanistic understanding of the underlying phenomena, involving hydrogen dif-
fusion from the cell surface and defect formation in the bulk, mitigation strategies for cell pro-
duction, such as adapting temperature profiles in the firing process [14], [15]  or using thinner
wafers [16], have been developed in recent years. Furthermore, the transition from Boron-  to
Gallium doping in p-type solar cells led to a decrease in LeTID [17].
According to current experience, modules containing n -type TOPCon cells are substantially
less susceptible to LeTID than early p-doped PERC cells.
The above-explained reasonings for LID and LeTID have been demonstrated in the following
experiment, where a large selection of commercial TOPCon modules was subjected to 322
hours of LeTID tests (IEC TS 63342:2022 for 2 × 162 h at ISC – IMPP) after LID preconditioning
(IEC 61215-2:2021 gate 1), see Figure 3. The results show minor effects on the PV module
performance.

Figure 3: Performance loss (PMPP) of commercial TOPCon modules after 322 hours of
LeTID tests [18].
At PV module and PV system level we expect no detectable degradation from the LeTID effect
in current TOPCon modules based on Ga doped p-type wafers.

## Página 14

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
14
2.3 Potential-induced degradation

System voltage potential-induced degradation (PID) involves electric charge transfer through
the encapsulation of PV modules to or from the cell. Depending on the module type, the polarity
and level of the voltage potential, which develops according to voltage difference between the
cells in the module and ground, and environmental factors, a number of different PID modes
may manifest.
The known and documented PID modes are summarised by Molto et al.  [19] and listed in the
following:
PID-Corrosion involves electrochemical reactions at the cell surface, including the metalliza-
tion, the dielectric, and the Si itself. Chemical species within the cell and encapsulation disso-
ciate and drift under the applied electric field.
PID-Delamination involves electrochemical reactions at the cell surface which produce gase-
ous products leading to delamination of encapsulants. The process may also involve the pre-
cipitation of ions at interfaces that promote delamination.
PID-Penetration involves drift of Na+ or other ions that migrate to the cell circuit, penetrating
the passivating dielectric, including at pinholes, depositing on the Si surface, and leading to
degrading surface passivation which reduces photocurrent and voltage.
PID-Polarisation (PID-p) involves motion of charge into or out of the dielectric passivation
layers in such a manner that more minority carriers are attracted to the interface of the Si with
the passivating dielectric. This leads to reduced photocurrent and voltage. There may be sev-
eral mechanisms responsible for PID -p. The charged species may be a static charge, which
can be dissipated by UV irradiation due to photoconductivity in the dielectric, or, speculatively,
an elemental ion with a charge that is not dissipated by UV irradiation.
PID-Shunting involves migration of ions, particularly Na+ from the glass and encapsulant, but
also from cell production handling, drifting to the cell surface and dielectric, and then diffusing
through defects through the emitter of the cell, leading to junction recombination and shunting.
PID-Shunting has already been addressed in former PVPS TASK 13 reports and has not been
observed in current cell types. PID -Delamination occurs very rare in the field and is usually
mitigated when other PID -mechanisms are solved with higher resistivity encapsulation and
there is little information in the literature. PID-Corrosion is no new degradation mechanism and
no field-related cases for current crystalline silicon solar modules are reported in literature.
PID-Penetration is a process appearing after or together with other PID mechanism or it occurs
at harsh test conditions. Among all these PID modes, PID -p is the most relevant, emerging,
degradation mode for current cell types [19] . Therefore, we focus on this mode  in the next
chapters.
2.3.1 Potential-induced degradation by polarisation on cell rear of bifacial PERC
solar cells
The rear side of bifacial PERC solar cells, which have a structure from front to back consisting
of anti-reflective coating (ARC)/n+/p/ARC, is particularly susceptible to PID-p because there is
no diffused surface field repelling minority carrier electrons there, except at the localised cell
contacts. The rear ARC dielectric may consist of a stack including AlO x, SiOx, or SiNx. AlOx
deposited in the dielectric is preferably deposited to contain a negative charge that serves to
repel the minority carrier electrons in the p- doped cell base. However, when the cell c ircuit is
negatively biased, positively charged species can drift through the rear encapsulation towards

## Página 15

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
15
the dielectric stack. That net positive charge developing in the rear increasingly attracts minor-
ity carrier electrons in the p- type base towards the rear dielectric , resulting in an increased
effective surface recombination velocity, see Figure 4. This mechanism results in a loss of
photogenerated carriers, which reduces the photocurrent and the voltage of the cell, especially
if the power is measured by light-current-voltage (light-IV) characteristics from the rear.

Figure 4: Schematic of the PID -p process in the PERC module rear. The red arrows
indicate the motion of current (positive charge) through the encapsulation.
In recent times, there has been a migration to higher sheet resistance of the n-type emitter on
the front face of the cell. This transition has been achieved using methods such as selective
emitters or Ag grid finger metallization, which enable contact with higher sheet resistance front
emitters. While front ARC usually is based on some combination of SiO2 and SiNx layers, where
SiNx has a built -in positive charge, placing the cells in a positive bias which can lead to
transport phenomena resulting in more negative charge in the front. This process increasingly
attracts minority carrier holes in the front emitter and more front surface recombination. Fur-
ther, PID-shunting becomes more probable if the junction depth of that emitter is shallower .
Since the rear side is weakly doped and usually receives less light, it has less photoconductivity
in the SiNx layer to counteract PID-causing charge. As a result, the rear side is more sensitive
to PID-p than the front side, although the front side also has a certain sensitivity.
Several studies have demonstrated PID-p degradation under laboratory conditions. Since the
rear side of the cell has weak doping and is therefore more sensitive, it has received greater
attention in research studies. An example of the degradation magnitude of PID-p when effec-
tuated on the module rear is shown in Figure 5.  It can be seen that the degradation magnitude
of PID-p is much greater for light I-V testing from the rear than such testing with illumination
incident on the front of the module, because the photogenerated carriers are largely generated
close to the rear surface where increased recombination takes  place. As the stress testing
duration increases, a recovery in power output is observed. This is attributed to inversion at
the rear surface, where the silicon base effectively becomes n-type [20], [21].

## Página 16

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
16

Figure 5: Normalized IV curve parameter of bifacial PERC modules with Ethylene-Vi-
nyl-Acetate (EVA) encapsulant as function of test duration when biased with -1000 V
applied to the cells and the rear glass face grounded. The values are obtained by
flash testing under standard test conditions (25°C, 1000 W/m2) and under 200 W/m2
from the front and rear as indicated in the figures. Values are from the averages of 3
samples. The solid lines are visual guides. The figure is redrawn from Luo et al. [20].
Several studies point to the existence of PID-p in PERC modules under field stress conditions.
Combined-accelerated stress testing using the extremes of the natural environment  (temper-
ature cycles, irradiation and at the same time system voltage, dynamic and static load, low and
high humid conditions together with water spray) , indicated that PERC cells in glass/glass
modules with EVA encapsulation on the front and rear side exhibited PID -p [22]. Although
there was convolution with a much lesser amount of LID, with - 1200 V bias voltage applied
between the cell circuit and the module frame during periods of illumination (including about
7.5% albedo in the UV range), there was almost 10% relative degradation when flash tested
from the front and more than 50% degradation when flash tested from the rear at standard test
conditions associated with PID-p on the rear [22].
For testing PID-p in the field, commercial bifacial glass/glass PERC modules with EVA encap-
sulant were put in two different mounting configurations. One mounting is near (0.3 m) ground
with small insolation and one is an open rack (2 m) above ground with higher rear insulation

## Página 17

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
17
and with their maximum rated system voltage of - 1500 V or +1500 V bias during the day.
Modules in open racks, either close to ground or elevated in open racks with -1500 V exhibited
PID-p within several weeks whereas modules with +1500 V did not exhibit such degradation,
see Figure 6.

Figure 6: Normalized power to control sample for outdoor PID stress testing of
PERC modules on two different racks with +1500 V and -1500 V system voltage be-
tween cells and rack in Cocoa, Florida USA (Cfa climate in Köppen Geiger classifica-
tion 2006). Measured points are assembled from three samples per rack type. The
figure is redrawn from Hacke et al. [23].
PID-p may be partially mitigated by inclusion of SiO x in the rear dielectric stack (i.e.
AlOx/SiOx/SiNx) [24]. The use of a more resistive encapsulant such as a polyolefin (PO) -con-
taining encapsulant rather than EVA and/or a polymeric backsheet instead of glass are more
certain mitigations [20] . Ultimately, testing the module simultaneously with voltage bias and
light with UV content, is helpful to understand whether PID-p will be a problem in the field [25].
Testing for PID in crystalline Si  (c-Si)-based modules has been done with the two methods
described in the standard IEC 62804- 1 (2015) [26]. Stress method (a), testing in an environ-
mental chamber, employs a non-condensing humidity level to serve as a conductive pathway
to electrical ground. It frequently applies less stress toward the centre of the module face and
the PID effect is concentrated toward the module edges, as is often observed for PID in PV
systems. The testing conditions are module temperature of 60°C or, for further acceleration,
65°C and 85°C which is most commonly used and adopted in IEC 61215 series (2021) [6], the
design qualification and type approval test. Further test conditions are the chamber relative
humidity (RH) of 85%, the duration of 96 hours, the module rated system voltage, and polarity
applied during the test.
Stress method (b) consists of contacting the surfaces with a grounded conductive electrode. It
evaluates cell sensitivity and some effects of the component embedment materials such as
glass and encapsulant resistivity , but does not differentiate the effects of some construction
methods of mitigating PID, such as  the use of rear rail mounts, edge clips, and insulating
frames. Severities prescribed are test temperature of 25°C or, if further acceleration is desired,
50°C or 60°C, RH less than 60%, a dwell duration of 168 hours, module rated system voltage,
and the polarities applied during the test period.

## Página 18

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
18
For testing PID-p, illumination of the sample is recommended. In IEC 62804-1 (2025) [27], two
methods are given to provide a transparent conductive electrode for the module face with
which an electric field is applied while allowing the transmission of UV irradiation. Method (c)
uses an electrolyte gel serving as an electrode for the module f ace that is covered by a UV -
transparent polymeric film, to reduce evaporation of the gel. The alternative method (d) uses
a fine metal mesh weighed down by a UV transparent sheet on the module face to transmit
UV irradiation and serve as an electrode for the module face. The test temperature is 60°C,
the duration 20 hours, with the module rated system voltage and polarities. For testing on the
superstrate side, 3.0 W/m2 in the range of 290 nm to 400 nm irradiation level is prescribed. For
testing on the substrate side, the measured UV irradiance level incident on the module rear,
or by default if not measured, 0.3 W/m 2 in the range of 290 nm to 400 nm is prescribed. The
UV light irradiation spectrum is defined in IEC 61215-2 MQT 10 [28], in the UV preconditioning
test.
As a diagnostic measure of extent of possible PID -p recoverability under a standard level of
irradiance, an additional test is included in IEC TS 62804-1 (2025) [27] with a level of irradiance
for front surfaces of modules of 100 W/m 2 in the range of 290 nm to 400 nm with irradiance
source specified in IEC 61215-2 MQT 10 [28] and a module temperature of 60°C.
The test procedures described here may be used for the cell types described below, but the
relationships between the PID test and field behaviour for SHJ-based modules have not been
explored.
2.3.2 Potential-induced degradation by polarisation on PERT and TOPCon front
and rear side
PERT and TOPCon solar cells are grouped together based on their common structure of p+/n
cell doping on the cell front, see Figure 7. Due to the relatively lower solubilities of the boron
forming the p+ emitter region of the cell and the relatively reduced front surface field provided
by that doping compared to the n+/p fronts of PERC and Al-back surface field cells, the sensi-
tivity to the polarisation is elevated. When the cells experience negative voltage potential, pos-
itive charge drifts through the encapsulation to the front cell dielectric. In turn, minority carrier
electrons in the front p+ emitter tend to recombine more actively at the front surface, attracted
by that developing positive charge in  the front dielectric. Rear sides of PERT and TOPCon
have significant phosphorus n+ doping, also in polysilicon the case of TOPCon, so the rear of
these devices is correspondingly found to be less sensitive to polarisation [25], [29], although
it is important to check as each module type shows different PID behaviour.
These cell types have significantly evolved over time. For example, the PERT type which came
on the market earlier in time, tended to have SiNx/SiO2 front passivation stacks. Later module
types added AlOx films to the stack, which have a built-in negative charge. This charge repels
minority carrier electrons in the emitter, reducing sensitivity to PID-p [30].

## Página 19

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
19

Figure 7: Schematic of the PID-p process in one manifestation of the PERT module
front (the front ARC stack may differ, including with the use of AlOx). The red arrows
indicate the motion of current (positive charge) through the encapsulation. The
mechanism is the same for the TOPCon front (which has an SiOx/n-type polysili-
con/SiNx rear side instead of what is shown here for a PERT module).

For PERT cell modules, there are several studies where extremely rapid degradation has been
measured; for example, in the dark [31], and while varying the level of full spectrum illumination
and encapsulant resistivity [32].  Figure 8 shows the relative degradation in cell parameters as
PID-p occurs. PID-p in the case of a single cell consists of the loss in open-circuit voltage (VOC)
and short circuit current (ISC), but a negligible change in fill factor (FF). Overall, this results in
the loss of maximum power (Pmpp).

## Página 20

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
20

Figure 8: Change of JSC/JSC,0, VOC/VOC,0, FF/FF0, and Pmpp/Pmpp,0 of n-type c-Si PERT
single cell modules as function of the duration of PID stress. The voltage bias and
temperature in the PID tests are set to −1000 V and 85°C, respectively. The data
points represent the mean values of three identical single cell modules and the solid
lines are visual guides. The figure is redrawn from Yamaguchi et al. [31].

High resistivity encapsulants and the generally high level of front side radiation reduce PID -p
effects for PERT and TOPCon solar modules. Figure 9 shows how increased levels of the
encapsulant resistivity and illumination with the module surface maintained wet lead to a re-
duction of PID-p. In these modules the degradation occurs regardless of the irradiation  using
this low resistivity EVA encapsulant. Conversely, even the most resistant encapsulations will
exhibit PID-p if they are kept under voltage stress in the dark for long enough.

## Página 21

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
21

Figure 9: Normalised VOC of PERT single cell mini modules, measured via flash
testing (triangles) and in situ (circles) during PID testing. Different coloured circles
mark in situ measurements that were taken on each of three samples running at the
respective illumination level. Thereby, 60°C and -1000 V were applied to the cells
and the front glass face grounded. Resistivity in Ω·cm for the encapsulant Polyole-
fin elastomer (POE) A 1.2x1016, POE B 3.8x1014, POE C 8.5x1013, and EVA 1.1x1013
[32].

For PERT modules tested outdoors, it has been reported that degradation occurs during peri-
ods of wet weather, when the module surface becomes conductive and facilitates coulombic
charge transfer across the glass between the cell circuit and the ground, while there is a lack
of full sunlight. However, after periods of sunny weather, the power of the modules is at least
partially restored, see Figure 10.

## Página 22

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
22

Figure 10:  Normalized STC power to initial values of PERT PV modules as a func-
tion of the indoor (red) and outdoor (blue/orange) PID test duration at a voltage of
−115 V. At the 10 h point indoor testing the slope slidely changes indicating a shift
from PID-p mode to PID-shunting mode. The open blue and filled orange square data
points indicate the results for the outdoor PID test in or just after rainy and sunny
days, respectively. The figure is redrawn from Ohdaira et al. [33].
TOPCon modules with EVA encapsulation show a maximum of ~3% PID p -front degradation
with -1000 V applied to the solar cells and the glass rear face with the front glass face grounded
in a test setup for the polarisation of the p+/n front structure over 96 hours in humid and cloudy
(~0.1 sun) weather. However, under 0.1 -sun-equivalent level with UVA illumination corre-
sponding to 0.051 W·m−2 nm−1 at 340 nm, they show progressively less degradation, see Fig-
ure 11. The cell rear side did not show any PID effect in that study [25].

## Página 23

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
23

Figure 11: Normalized STC power PSTC relative to initial STC power PSTC,0, ob-
served with −1000 V applied at 60°C over a period of 96 h versus simultaneously ap-
plied UVA irradiance level at 340 nm. For reference, Air Mass 1.5 global spectrum ac-
cording to ASTM G173-03 contains 0.502 W·m-2·nm-1 at 340 nm. Two repetitions were
performed per irradiance level shown with markers (●). The figure is redrawn from
Hacke et al. [25].
In the case of the TOPCon module tested, the PID -p rapidly and repeatedly recovers under
sunlight when the voltage potential across the front glass is removed. Such properties suggest
that PID-p will rapidly recover in the field and that it may not even occur to any significant extent
because solar irradiation is accompanied by the development of system voltage stress in the
module string. However, the relative sensitivity to PID -p under the factors of system voltage
and solar irradiation must be checked for each module type.

## Página 24

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
24
2.4 Protection of substrings in the modules
The protection of the module’s substrings against acting as a power load is one of the most
important safety features of a solar module. A module can act as a power load if it is partially
shaded or if there is high resistive interruption due to a failure in the electric current path (sub-
string). There are two widely used options to protect a module’s substring against high power
dissipation during shading. The cheapest and most commonly used option is to protect a sub-
string against overheating by a bypass diode (BPD). The second option is to avoid overheating
during shading is by using solar cells with a low, not localised breakthrough, voltage which acts
similar as a cell-wise BPD. Even in the second case,  an additional BPD per string, is used to
reduce the power loss during excessive shading, and to achieve an additional safety feature
in the event of a high resistive interruption in the module’s substring. With current module types
(1500 V and 600 Wp) 10 kW and more can be generated in a single module string. The higher
the string power, the more harmful a failure of the substring protection can be.
2.4.1 Hot cells
Cell cracking or shading of PV modules can cause current mismatch and reverse bias voltages
in underperforming solar cells, causing the cells to dissipate power and generate heat. The
difference between the well-known hot spot and the hot cell effect is that the hot spot is mainly
associated with multicrystalline silicon solar cells and causes localised heat generation (local
junction breakdown), whereas the hot cell is associated with monocrystalline silicon solar cells
and causes a homogeneous temperature  rise throughout the cell  area [34]–[36], see Figure
12. The most important junction breakdown mechanism in monocrystalline silicon solar cells
is avalanche breakdown, which occurs at reverse bias voltages below - 20 V for PERC cells
[37] and even more negative for TOPCon, SHJ , and possibly for MHP/Si tandem [36]. A hot
cell can cause heating above the typical module operating temperature of 50°C - 70°C, reach-
ing temperatures above the highest module’s lamination temperature of 150°C.

Figure 12: Temperature distribution of a partially shaded cell during the IEC 61215-
2 MQT 09 Hot-spot endurance test [28], [35]. The shadow mask is shading the cell
with a 4 cm wide cover strip.
The occurrence of a hot cell may lead to the generation of other failure modes, including dis-
colouration, interconnection failures, cell cracks, delamination, loss of electrical insulation, and
a permanent change in the reverse bias characteristics of a shaded cell [38]–[40]. The standard

## Página 25

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
25
hot-spot endurance test (IEC 61215-2:2021 MQT 09 [28]) assesses the ability of the solar cell
and module materials to withstand localised point heating at a module temperature of 55°C ±
15°C under worst-case partial shading.
PV manufacturers are taking measures to minimise the impact of hot cells on the reliability and
durability of PV modules. These measures include sorting cells into bins based on the cell
current rating and the screening of individual cells for low shunt resistance [41], [42] . In addi-
tion, manufacturers insert BPDs into PV modules to minimise the formation of hot cells and
mitigate their harmful consequences. The incorporation of the BPDs ensures that the power
dissipated by the shaded cell is at most the power generated by the rest of the cells in the
same sub-string. This way, although BPDs can reduce the power losses caused by shadows,
they do not eliminate the negative effects of hot cells, which can still lead to significant perfor-
mance losses and safety risks [43] . The market now offers a variety of shade -resistant PV
modules, such as half -cell modules, shingled modules, and modules with built -in diodes for
each cell [44] –[46]. However, the term "shade resistance" is poorly defined, and there is no
reliable way to compare different PV products. Researchers are working to standardise this,
focusing primarily on minimising yield loss, but often neglecting improved reliability [47] . In
addition, decreasing the number of solar cells per BPD lowers  the hot cell temperature, as it
operates at less negative reverse voltages [35], [36], [48].
In Interdigitated Back Contact (IBC) solar cells, the p+ and n+ regions can be designed to be in
direct contact with each other, resulting in the formation of a Zener diode that functions as a
built-in BPD and significantly lowers the breakdown voltage (> -5 V) of the cell [49], [50]. As
shown in [48], during the indoor hot-spot test, the hot cell temperature of the IBC module was
at most 25°C higher than the module temperature. Moreover, it was significantly lower than
the temperature of the PERC and SHJ module technologies under the same conditions, see
Figure 13.

Figure 13: Module and hot cell temperatures of PERC - half-cell  365 Wp, IBC - half-
cell 400 Wp and SHJ - half-cell 375 Wp modules from indoor hot spot tests per-
formed at 55°C module temperature by following IEC 61215-2:2021 [28], [48].
High temperatures above 150°C can have significant implications for polymeric materials (i.e.
discolouration, delamination, embrittlement [38], [51] ), which are designed to operate below
this temperature. Furthermore, temperatures above 170°C can lead to bubbles and defor-
mation of the backsheet material , and in extreme cases, the junction box may even detach
[51]. It is also crucial to ensure that the temperature of the hot cell does not exceed the solder
melting temperature, which leads to solder joint failures [52] . The liquidus temperature of
Sn63Pb37 solder is 183°C and for lead- free solders around 220°C [35] . In addition, high cell

## Página 26

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
26
temperatures can also put the glass at risk of breaking. IEC 61730-2 MST 21 temperature test
exposes the module to 1000 W/m2 sunlight until the temperature stabilized and the pass criteria
of the standard is that no measured temperature exceeds the limits of the surface materials.
This limit is given in the standard as “TI/RTE/RTI”, which is the maximum service temperature
at which the critical properties of a material will remain within acceptable limits over a long
period of time. The duration spent at these high temperatures is as important as the tempera-
ture itself, as degradation mechanisms require time to occur. Thermoplastic materials require
a certain exposure duration to undergo material changes due to elevated temperatures.
Nowadays there is a clear trend towards bifacial modules, but their ability to receive light from
both sides can cause non- uniform illumination patterns at the rear side  [53]. In the event of
current mismatch, the higher current produced by bifacial modules can result in higher hot cell
temperatures compared to monofacial modules [54] . Another current trend is the adoption of
half-cells, which are advantageous in terms of heat dissipation due to the larger perimeter -to-
area ratio. However, larger Si wafer dimensions decrease this ratio, resulting in higher hot cell
temperatures for modules using larger wafer formats [35]. Up to now, the hot cell effect occurs
in the standard hot spot test , but not as severely in the field . Nevertheless, increasing the
substring length and increasing cell efficiency raises the risk of encountering modules with
laminate defects caused by regular shading in the field.
2.4.2 Unreliable connection in junction box
A reliable connection between the inner parts of a PV module and the BPD is mandatory. A
working BPD and a reliable connection of the inner cell strings is responsible to avoid high
power dissipation on shaded cells in a PV module. A defect in the BPD or in the connection
process can often lead to arcs in the module laminate, which may cause a fire. This can result
in the loss of both the mechanical and electrical integrity of the module. In addition,  power
losses can occur in the entire string, either while the module is shaded or after the disintegra-
tion of the affected module. Therefore, this kind of failure type is one of the worst possible.
The half-cell module type, introduced around 2020 as a mainstream module layout, is accom-
panied by changes in the interconnection of inner parts and the diode box. Compared to former
full-cell modules, t he substring interconnects of half -cell modules are very short at the point
where they lead into the junction box. This may cause an unwanted surface contamination
onto the ends of the short substring interconnect from the lamination material during the lami-
nation process. Furthermore, it is more difficult to reach the interconnect ends by factory work-
ers/robots as they are now in the middle of the module and not near the frame. Additionally,
the diode boxes are quite small. In the past, most connections were made by reliable clamping
in the junction box. Now adays soldering is used as the space in the boxes is to o small for
clamping. Furthermore, since then the diode boxes are filled with a filler material as a standard.
With all these modifications lamination material contamination  on the interconnection wires
can cause a bad electric contact in the junction box, the difficult handling could cause a poor
quality/bad visual quality control of the soldering process, and the filler material can cause the
loosening of a weak connection in the diode box by shrinkage or by chemical changes.
If there are unreliable connections in the junction box, modules show connection failures in the
junction box within one and two years of installation in the field. The experience is that the rate
of new failures per year drops down fast in the second year for one installation. Figure 14
shows an overview which failure modes (A, B, C) are possible, how to detect them, and what
consequences the failure mode provokes for the safety risk and the power loss. In Figure 14,
the consequences are given for the extreme case that the cold solder joints are fully discon-
nected. All shown failure modes can happen in all thinkable combinations. Failing BPD [55]
cannot be differentiated from failure mode A without a destructive analysis of the junction box.

## Página 27

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
27
However, having a mixture of failure modes A and B in a fleet of modules indicates that a cold
solder joint is the cause of the defect.

Figure 14: Failure modes of unreliable connections in separated junction boxes.
Open-circuit (OC) substrings or module strings appear 5-10 K hotter in IRT inspec-
tion compared to active strings.
However, as long as the likelihood of a cold solder joint is low, a combination of different fail-
ures in the same module is very unlikely. Failure mode A can occur at four different solder
joints. Two of four solder joints are in the middle substring. Failure mode B can occur at two
possible joints, whereas failure mode C needs two joints failing in parallel. Therefore, failure
mode A occurs at least double as likely as failure mode B. Failure mode A cannot be detected
by infrared thermography (IRT) inspection, but failure mode B and C can. This means that if
failure mode B or even C is present, failure mode A is very likely to occur at a rate at least
twice as high as that of failure mode B. However, without shade on the modules failure mode
A will stay without notice. A shaded module with failure mode A can heat up very quickly (within
seconds) and may char or even burn. The danger rises if the module is shaded at high irradi-
ation level or if the shade is applied for many seconds. Figure 15 shows a high power TOPCon
module with failure mode A after being shaded in a long module string. To find mode A failure
or open BPD, a string wise BPD test at night is useful. Measure the reverse bias voltage
achieved in the string when 3% to 5% of rated ISC is applied. If a string with extraordinarily high
reverse voltage is found, search for some Kelvin warmed up substring with night infra inspec-
tion to locate PV modules with mode A failure or open BPD, see Figure 16.

## Página 28

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
28

Figure 15: Rear side of TOPCon PV mod-
ule with failure mode A being shaded by
natural obstacles. Module has already
been dismantled from the mounting rack.
Figure 16: Not connected BPDs found by
night IRT inspection while applying
string wise reverse voltage with 3%-5%
of rated ISC. Image: photovoltaikbuero
Ternus & Diehl GbR.

All failure modes can occur also with arbitrary contact resistance at the cold solder joint. This
means that a junction box which is hotter than the other boxes can be an indication for a cold
solder joint. However, resistive heating at a cold solder joint for failure mode A can only be
observed during shading or with greater safety for the inspecting person within the BPD test.
A cold solder joint usually appears in a certain percentage of modules in the production be-
cause the problem is typically the same for the whole batch of modules. Figure 17 shows the
IRT image of multiple modules with failure mode B , with OC substrings resulting from cold
solder joints in the outer junction box. It is frequently observed that this unstable connection
appears for a small percentage of modules from the same production batch.

Figure 17: IRT of OC substrings resulting
from an unstable connection of the outer
junction box. Failure mode B can happen
only in the outer junction boxes. Current
flows through diode of outer junction box.
Figure 18: Module with burnt junction
box resulting from unstable connection
in the junction box.

## Página 29

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
29
Even if the inspection at the end of the production was inconspicuous, unstable connections
could be found in one batch of modules during pre-shipment inspection. The voltage and power
of the defective modules are only 2/3 of the normal value, while they had normal power during
the measurement at the end of production.  It is a typical unstable connection where the per-
formance is sometimes OK  and sometimes not. The modules from  the same batch showed
more open substrings in the IRT inspection. Figure 18 shows a module with burnt junction box
probably resulting from failure mode C with some contact resistance still present.
To avoid this failure type during production,  we recommend a reverse voltage sweep in the
dark in series with the flash, EL , or high potential test of the PV module , as specified in IEC
61730-2:2023 Annex A5 a) or b) but not c) . A reverse voltage sweep in the dark would show
unconnected diodes (no current flowing through them) and would also reveal high contact re-
sistances within the junction box (define max. allowed resistance in the BPD IV  curve). How-
ever, some not fully operational contacts may be overseen, as these contacts are low resistive
at this stage. To detect these cases, an automated visual inspection test is recommended after
soldering the leads into the junction box. At system level , a reverse voltage sweep should be
done for each module string to detect non-connected or high resistive BPDs in failure mode A,
and a thermal inspection is recommended to detect failure mode B and C. In case of a single
failure, all modules should be tested due to the high risk of fire.
2.5 Encapsulation degradation and failure modes
The basic module design of standard PV  modules has changed dramatically in the last few
years. The entry of bifacial solar cells into the market triggered a transition from the prevailing
standard glass/backsheet module architecture to increased use of glass or transparent back-
sheets as the back side layer of the PV modules. EVA has been the most commonly used
polymer encapsulating material, and polyvinyl fluoride (PVF) films in combination with polyeth-
ylene terephthalate (PET) core (PVF-PET-PVF known as Tedlar) have been commonly used
for backsheets in PV modules for more than 30 years [56]. Although their technical, environ-
mental and economic characteristics were satisfactory, there was still room for improvement.
Around 2010 p olyvinylidene fluoride (PVDF)-PET-PVDF and polyamide (PA) -based back-
sheets entered the market; followed by pure PET- backsheets [56]–[58]. More recently, new
encapsulation and backsheet films based on PO were developed, and after intensive testing,
some of them were also commercially launched within the last years [59]–[63]. Furthermore,
silicone-based encapsulants are also promoted and tested [64] .
Looking at the distribution of reported PV module failures [38], [65], [66], defects of the back-
sheet such as discoloration, delamination and backsheet cracking represent a significant group
[67], [68]. Jordan et al. developed a rating system to classify the severity of failure/degradation
modes by ranking them from 1 to 10, where 1 indicates that the observed degradation mode
has no effect on performance, meanwhile 10 indicates both, a major effect on power and safety
[38]. Degradation related to the backsheet layer was divided into two categories:
(i) backsheet insulation compromise (e.g. adhesion issues and cracking) has a significant ef-
fect on power and/or yield and also represents a safety hazard = severity 10,
(ii) backsheet other (e.g. bubbles, discoloration, and chalking) do not affect module perfor-
mance immediately = severity 1.
There have been reports of an increased occurrence of failures of PV modules with cracked
PA back films [69], [70], especially since 2016. In addition, cracks and insulation problems in
PVDF-PET-PVDF and PET-based backsheets [68], [71], [72] have been increasingly reported
in recent years. Based on extensive field measurements, Buerhop et al. report yiel d losses if

## Página 30

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
30
the inverters fail to  start in the morning because dewy, torn backsheets cause an insulation
fault [71]–[73].
In the following, the major chemical and physical degradation mechanisms for these failure
modes will be compiled.
As backsheet cracks are typically reveal ed after several years of field ageing, and they  have
never been observed in previous qualification and reliability tests according to standard IEC
61215-2:2021 [28], the probable origin is suggested to be the result of a combination of multiple
stresses and might also include unexpected material interactions as drivers. Similar PA back-
sheet cracks could be reproduced by a newly designed indoor accelerated ageing test , by
utilising simultaneous combined or sequential stresses (UV, humidity, temperature and
thermo-mechanical load) [22], [56], [68], [74], [75]. These newly developed ageing tests can
now be used to test the crack susceptibility of new backsheets during the product development
phase. If cracks occur in the backsheet of a PV system, a repair coating or tape/foil can be
applied to restore the insulation resistance as shown in chapter 2.2 of the PVPS Task 13 report
“Performance and Reliability of Second Life PV” [76].
Various types of backsheet cracking can be distinguished [69], [77], [78] and are described in
sections 2.5.1.- 2.5.3.

Figure 19: Backsheet crack types. a) cracked backsheet beneath a hot cell/tempera-
ture induced crack. b) squared cracks beneath cell interspaces; thermo-mechanical
induced crack combined with photo-oxidative degradation. c) longitudinal cracks lo-
cated beneath busbars; thermo-mechanical stress induced crack [69].
In addition, when new materials were introduced, incompatibilities between the encapsulating
and backsheet films were observed in some cases. These were partly caused by undesirable
additive migration within the polymer laminate and led to adhesion problems/delamination
and/or discoloration [56], [70], see chapter 2.5.4. Furthermore, specific failure modes were also
observed with new PO-based encapsulant films, see chapter 2.5.5, and innovative polymeric
front sheets [79], [80], [81].
Such material incompatibilities can be mitigated by selecting appropriate materials and thor-
oughly testing their compatibility by applying tests suggested in chapter 4.1 of the PVPS
Task 13 report “Accelerated testing -  combined stress vs. sequential stress testing methods
and inclusion of specific load situations” [79].
The different backsheet failure modes are described in the following. Finally, chapter 2.5.8. will
deal with the frequent breakage problem which has emerged in new large- format thin glass
modules.

## Página 31

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
31
2.5.1 Backsheet cracking type I: micro-cracking and chalking
UV photons can open chemical bonds at a surface and the open bond s subsequently react
with oxygen leading to degradation and discoloration of the material. This process is called
photo-oxidative degradation. Surface weathering can lead to photo-oxidative degradation of
the outer backsheet layer , resulting in decomposition of the polymer and release of the inor-
ganic filler (=chalking), see Figure 20 b). The root cause for cracking type I is insufficient weath-
ering stability of the individual outer layer of the backsheet , e.g. missing or lack of UV-stabili-
sation, which can happen with different types of backsheets which have polymeric outer layers
prone to photo-oxidative degradation, e.g. PA or PO. Chalking of the backsheet has no direct
impact on module reliability or the performance of the PV system. However, in some cases,
chalking can be an initial indication of later microcracking which in the long term could evolve
on deep cracking, see Figure 20 a) and b).

Figure 20: Light microscopic images of (a) longitudinal cracks (whole backsheet is
disrupted) and (b) surface near microcracks [69].
Chalking is the result of photo- oxidative degradation of the polymer in the outer backsheet
layer which leads to the release of filler. A simple wipe test can be carried out to check this
phenomenon in the PV system. Preventatively, the backsheet can be subjected to accelerated
weathering tests, and then these wipe tests can be applied. Chalking is a superficial phenom-
enon and not directly related to the insulation resistance of the backsheet. Unfortunately, there
is no possibility to predict if chalking is  a precursor for future cracking or potential changes in
other backsheet properties like electrical insulation, as there are no systematic studies on the
topic and its effect on long-term stability of the backsheet and the module. For example, crack-
ing was observed with and without chalking for PA backsheets [69]. Another example is crack-
ing of PVDF-based backsheets, where chalking is usually is not observed [82].
2.5.2 Backsheet cracking II: temperature-induced
Hot cells or hot spots lead to local overheating (200°C or higher) of the backsheet and the
encapsulant layers, resulting in strong chemical degradation , followed by locally  cracking of
the backsheet. This reaction is often accompanied with browning phenomenon or even gas
formation within the encapsulant and backsheet, like shown in Figure 19 a). The main reason
for cracking II is the extreme thermo-oxidative stress impact from the overheated cell or inter-
connection, caused by heat generating electrical defects like isolated cell parts caused by cell
cracking, insufficient solder contacts on cells or other wiring parts , or excessive local shading
of cells in a module. This failure mode can occur with all the different types of backsheets and
typically occurs with only some individual PV modules in a PV plant. Thus, low impact on the
performance of the PV plant is expected, but the defective modules should be replaced.

## Página 32

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
32
2.5.3 Backsheet cracking III: thermo-mechanical stress induced
The phenomenon of backsheet cracking type III occurs with increasing operational time and
seems to depend on the local weathering conditions. If backsheet cracking type III occurs
mostly all modules of a PV plant with identical module design in terms of bill of materials (BOM)
are affected [69]. Backsheet cracking III can have two appearances , see Figure 19 b) for
squared cracks and Figure 19 c) for longitudinal cracks. Drivers for these cracking modes are:
i) mechanical stress within the backsheet at the positions of the busbars , which is originated
already from the lamination process;
ii) unbalanced thermo-mechanical properties of the backsheet  e.g. caused by mismatches in
the coefficients of thermal expansion (CTE).
With co-extruded backsheet types, e.g. a 3-layer PA backsheet, a high direction dependence
of the mechanical properties has been measured [58], [69]. Physical cracking starts at the
outer surface of the backsheet and propagates towards the core and the inner layer. No chem-
ical degradation is observed in the case of longitudinal cracks [69] . However, since the back-
sheet film is damaged across the entire cross-section, the insulation requirements for the back-
sheet are no longer met and the insulation resistance collapses especially under wet condi-
tions, leading to a significant safety risk [38]. Since all modules with the same backsheet type
are usually affected, either the entire system must be repowered, or the modules must be
repaired using a suitable coating or film.

Figure 21: PV module with squared cracks from the front (left) and rear side (right).
In the case of squared cracks, on the contrary, an additional driver is the insufficient UV-stabi-
lisation of the encapsulant. In a first step photo-chemical degradation in between the cell gaps
creates acetic acid with a high local concentration at the interface EVA encapsulant/inner layer
of the backsheet. A chemical degradation between acetic acid and the backsheet weakens the
mechanical strengths of the backsheet, followed by a physical cracking of the backsheet from
the encapsulant side to the air  side [69], see Figure 21. Serious safety problems [38] are the
consequence of this type of degradation, which can only be remedied by replacing all modules
of this BOM. A repair is not possible in this case.
Similarly, as for PA, two distinct types of PVDF backsheet cracking have been observed in the
field. The PVDF cracking type III i) involves cracks along the busbars that penetrate the entire
thickness of the backsheet, while the PVDF cracking type III ii) involves randomly distributed
longitudinal cracks that only affect the outer PVDF layer. The outer layer of the PVDF- based
backsheet can have a mono or multi -layer structure, and the PVDF is often mixed with a

## Página 33

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
33
poly(methyl methacrylate)polymer (PMMA) and TiO 2 [74], [83], [84]. Apart from cracking, the
PVDF layer undergoes physical ageing processes, leading to changes in crystallinity, crystal-
line phase, and shrinkage when it is exposed to elevated temperature [85], [86]  as well as
depletion of PMMA under exposure to sunlight [85], [86] . Due to the often undisclosed varia-
tions in the composition of the PVDF layer in the backsheet, no clear correlation between the
structural parameters of the PVDF layer and backsheet cracking has been established yet.
2.5.4 New backsheet types: degradation modes
With the increasing use of bifacial solar cells, the need for transparent backsheets is increas-
ing. The trend is strongly towards glass -glass modules, but transparent polymer backsheet
films are also used if double-glass modules represent a too high weight load. However, poly-
mer films without fillers are more difficult to stabilise, thus, the emergence of new failure modes
related to  transparent backsheets are to be expected. Compared to traditional filled back-
sheets, transparent backsheets can be more susceptible to UV-degradation, as light transmits
through the transparent outer layer into the backsheet core and the inner layers [87]. A change
in the type of backsheet may also require a change in the encapsulation material. One option
is to use different encapsulations sheets on the front and back side. In this scenario the danger
of material incompatibilities described above come back into play. Thus, in the product devel-
opment phase accelerated ageing tests as described in chapter 2.5 of the Task 13 report “Ac-
celerated testing - combined stress vs. sequential stress testing methods and inclusion of spe-
cific load situations ” [79] have to be performed to prove the material compatibility between
backsheet and encapsulant.
Conductive backsheets are used for interconnection of back contacted cells. These back-
sheets typically have a thin metal inner layer (Cu or Al) laminated onto the PET core layer [88].
Potential new backsheet degradation modes include delamination or corrosion of the metallic
layer. In this case accelerated ageing tests of the conductive backsheets in a laminate with the
encapsulant to be used along with the cells and connectors must  be applied as well. Test
procedures as described in the IEC 61215- 2 should be used, especially MQT 11 thermal cy-
cling (TC), MQT 12 humidity freeze (HF) and MQT 13 damp heat (DH) [28].
Currently, due to lack of long-term field experience with these types of backsheets, no critical
failures after field exposure have been reported so far. Therefore, at the current state (as of
September 2024), no statements can be made about relevance and potential mitigation
measures.
2.5.5 Encapsulant-backsheet incompatibility
If new polymer films are going to be developed or used to encapsulate the active solar cells
and connections, it is strongly recommended to test the compatibility of the materials with the
adjacent layers during the product development phase. For example, it must be verified
whether undesirable reactions or additive migration occur at the polymer interface between the
encapsulation material and the backsheet under stress, such as increased temperature.  Fur-
thermore, the adhesion of the encapsulant to the glass panes and/or backsheet has to be
evaluated after stress impact, such as high irradiation, temperature, or humidity in accelerated
ageing tests.
PO encapsulants can be incompatible with PO-based backsheets, because additive-migration
upon DH testing  can lead to strong discoloration [89] . The yellowing effect results from an
undesired interaction of oxidised additives of the encapsulants with additives of the PO -back-
sheet. These chromophoric compounds, with conjugated double bonds, formed under the in-
fluence of temperature and humidity and decomposed upon irradiation (photo -bleaching).

## Página 34

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
34
Since PV modules are always simultaneously exposed to sunlight, temperature, and humidity
under operating conditions, this yellowing effect does not occur in real life. Furthermore, en-
capsulant discolouration has only a minor  impact in the order of several percent  on the PV
module’s electrical performance [56].
Also, PV modules with PO encapsulants and Tedlar backsheets may show adhesion problems,
since the adhesion of the encapsulant to the glass may deteriorate under accelerated aging,
especially in areas without cells underneath (e.g., edge areas and cell gaps) . Furthermore,
light microscopy images show deposition of substances at the glass/polymer interface, see
Figure 22. Na+-ions were detected at the depositions on the detached surface of the encap-
sulant by X-ray diffraction (XRD) and carboxylic groups were found by Infrared-spectroscopy.
Thus, migration of an unwanted carbon acid or ester from the backsheet to the encapsul-
ant/glass interface took place, weakening the adhesion.

Figure 22: Detached surface of the PO encapsulant from the glass in the original state
0 hours and after two types of accelerated ageing tests. Test1: constant Xe-irradiation
at 1000 W/m2 at elevated temperature (chamber 65°C, PV module 96°C) and humid-
ity (80%r.H.). Test2: sequential (i) 500 hours DH, (ii) 50 temperature cycles and (iii)
200 hours Xe-irradiation at 1000 W/m2, 3 sequences.
2.5.6 New polyolefin-encapsulants with EVA: degradation modes
The development of new materials, based on ethylene copolymers in particular, has driven the
replacement of EVA. Various types of next -generation encapsulation films have been intro-
duced in the last year s under the label “polyolefin encapsulants” that could attract significant
market share in the future [59], [63], [90]–[95].
However, there is no comprehensive knowledge on outdoor behaviour of PV modules using
these materials available. The new materials caught the attention of the academic and indus-
trial sectors, but additional studies are necessary, especially long- term indoor and outdoor
exposure investigations, to discover new degradation modes that might appear [96]. Addition-
ally, the effects of the long- term interaction between the new encapsulant materials and the
other module components are still an open question.
These material innovations tend to be classified as cross-linked POE and TPO encapsulants.
The new materials do not contain vinyl acetate moieties,  and consequently, do not produce
acetic acid upon degradation. Therefore, PV degradation mechanisms mainly associated with
acetic acid [59] does not take place. Hence, the following positive effects of the use of alterna-
tive PO encapsulants have been reported:
● Reduced corrosion (no acetic acid, lower vapour transmission rate (WVTR)) [59], [61],
[97], [98]
● Reduced PID [32]
● Reduced yellowing [98].

## Página 35

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
35
Unfortunately, the terms POE or TPO are used in a manner that implies that all POE or TPO
encapsulants are the same. Additionally, the term “polyolefin” or PO is understood differently
in the PV industry. Elsewhere, a PO is any class of polymers produced from a simple olefin
(i.e., an alkene with the general formula C nH2n) as a monomer. That includes TPOs  like poly-
ethylene and polypropylene, but also POEs such as polyisobutylene or ethylene propylene
rubbers. The PV industry uses the term PO for all non- EVA encapsulants based on polyeth-
ylene or polyethylene copolymers, which also contain other functional groups such as acrylates
or acrylic acids [99].
The most recent developments resulted in the market introduction of so -called EPE films,
which are co-extruded films combining the benefits of EVA (E) and POE (P). The outer EVA
layers provide better adhesion to glass and the solar cells, whereas the POE c ore layer pro-
vides lower WVTR values. However, as of September 2024,  only one publication about the
properties of modules using EPE films [100] and no publications on long-term outdoor behav-
iour are available. Yang et al. reported excellent stability of the EPE film after exposure to
different accelerated test conditions [100].

Figure 23: Influencing factors for encapsulant film properties [99].
Apart from the base polymers, it has to be emphasised that encapsulant additive formulation
has a greater influence on durability than the type  of polymer resin [56], [59], [83], [99], see
Figure 23.
For PO encapsulants, the following new degradation modes have been reported:
● Reduced optical transmittance due to physical ageing: Exposure to elevated tempera-
ture leads to an increase of crystallinity of the polyethylene chain sections and conse-
quently higher scattering of incident light [83]
● Interdiffusion of additives at front-encapsulant (UV transparent) - back-encapsulant (UV
blocking) interface leads to ring patterns visible in UV fluorescence imaging [101]
With growing diversification in encapsulant and backsheet materials, material incompatibilities
could also become a relevant issue [66], [102], e.g. encapsulant -  backsheet delamination.
Therefore, the materials must be tested both individually  and in combination in the complete
PV laminate in specific accelerated ageing tests (irradiation, temperature and humidity impact,
isolated and combined). However, we are still lacking long- term outdoor experience with

## Página 36

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
36
polyolefin-based encapsulants. Most degradation and reliability studies including PE encap-
sulants were done based on accelerated ageing tests. As  of September 2024, no cases of
damage or failure of EPE-based PV modules following outdoor exposure have been reported.
2.5.7 Coloured components: degradation modes
For coloured PV  modules white or black rear  encapsulation or special backsheet films are
required to achieve the requested colour effect. Furthermore, the ribbons might be blackened
with ink or black tapes. Similarly to other additives, c olourants and/or pigments can migrate
within the polymer stack caus ing unwanted colour changes [103]. Although aesthetically un-
wanted, these effects have no impact on the electrical output. In a comparative study of white
EVA back encapsulants, it was shown that there are stable and non-stable white EVA grades,
depending on the type of white pigment [104].
To ensure that the materials used in the modules are stable and compatible with the adjacent
layers, the manufacturer must carry out certain accelerated ageing tests. With tests suggested
in chapter 4.1 of  Task 13 report “Accelerated testing - combined stress vs. sequential stress
testing methods and inclusion of specific load situations” [79], the decomposition and migration
of pigmented lamination materials can be assessed.  Although aesthetically unwanted, these
effects have no impact on the electrical output.
2.5.8 Breakage of thin glass
In the year 2023, mainstream bifacial glass/glass PV modules have a glass thickness of 2 mm
to 1.6 mm (thin glass). Up to 10% breakage rates are reported for recently built PV power
plants with 2 mm glass/glass modules [105]. In a published case bifacial modules with
2 mm/2 mm glasses have been mounted on a rack and on a tracker mount system [106]. For
50% of the modules, the glass broke within 9 months of exposure. About 32% of the modules
cracked on the rack and 57% on the tracker. This indicates that the mounting system has a
clear influence, but it is not the only cause behind the glass breakage phenomenon. The mod-
ules cracked at a practically constant rate within the tested 9 months  period. No special
weather event or module internal failure (hot spots) could be identified as the root cause. In
59% of all cracked modules the rear -side glass broke. The front side cracked in 28% of all
cases and in 13% both front and rear glass w ere broken. There are many confidential cases
in the field involving 2 mm/2 mm bifacial modules with a similar characteristic and an unknown
root cause. In many cases, the manufacturers have certified the sub construction for the use
together with the modules. It is important to emphasise that by far most PV systems in the field
with thin glass/glass modules are without conspicuous glass breakage.
The glass resistance against stress, impact and scratches depend s on the preparation of the
cutting edges and on the prestress of the glass surface. A high compressive stress at the glass
surface protects the glass against opening of microcracks in the surface. The maximum com-
pressive stress induced to thin glass surfac e with current glass tempering techniques is well
below the producible compressive stress of 3 mm thick glass. Furthermore, there is no existing
standardised technique to measure the compressive stress for thin glass (≤ 2 mm). Moreover,
standardised breakage tests are not applicable for thin glass [107]. At the time of writing, there
is no standardised way to check the delivered glass quality for thin glass for PV module appli-
cations. The lack of quality control may be the reason that glass breakage occurs more fre-
quently in certain cases. Another reason may be the continuous increase of module size and
gradual decrease in frame height, which both increase the stress in the glass [108].
Broken PV module glass is a catastrophic failure because it violates the mechanical and elec-
trical safety of a PV module. Typically, the module power is not affected immediately after glass

## Página 37

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
37
breakage occurs. Isolation failure may be a first fault signal at the PV inverter. Very often the
cracking of thin glass starts on the rear glass, so a visual inspection of the modules’ rear side
is required to detect the failure. Theoretically, internal arcing and fire may be a secondary
failure after some time of outdoor exposure.
As the root cause of the glass cracking is not known yet, new measurement/testing techniques
for characterising the compressive stress of the glass surface  are needed. One attempt to
measure this characteristic is to use a SCALP -05 [109]. This device couples a laser into the
glass, where the present stress causes a rotation of the polarization plane. This, in turn, re-
duces the scattering intensity orthogonal to the initial polarization plane, which can be detected
perpendicularly to the ini tial beam. As a result, the surface stress of the glass in the module
compound can be measured. Figure 24 shows results of PV modules with different glass thick-
nesses, where significantly different glass surface stress levels are detected.

Figure 24: Results of SCALP measurements on the front glass of PV modules, reveal-
ing the surface stress [110]. The grey shaded areas characterise the typical compres-
sive stress level for production methods of Heat Strengthened Glass (HSG) and Ther-
mally Toughened safety Glass (TTG).
Since glass follows a Weibull distribution in its cracking behaviour, no specific threshold for its
breaking resistance can be defined. As the cracking resistance for thin glass is typically much
lower than 3 mm glass, the Weibull distribution moves to lower stresses. Therefore, the stress
resistance of thinner glass must be known even more precisely , to withstand typical stress in
PV applications.
Even though hail impact is not the cause of the cases discussed here , hail impacts show the
challenge we face if thin glass is used in a PV module. The hail impact test on PV modules
with 2 mm glass/glass and 3 mm glass/backsheet shows the mechanical resistance difference
between these two module types. Kedir et al. measured the Weibull distribution of that two
module types for a wide variety of hail kinetic energy [111]. They showed that, compared to a
3 mm glass/backsheet structure, modules with a 2 mm glass/glass structure experience  50%
less kinetic impact energy from the ice balls at a 50% glass breakage probability. However,
both structures perfectly survive hail impacts at the kinetic energy level required for IEC 61215-
2:2021 MQT 17 hail test with 25 mm ice ball diameter [28].

## Página 38

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
38
As mentioned earlier, thin glass cannot be fully tempered like 3 mm thick glass. Therefore, the
surface resistance against stress, impacts and scratches is much less than for fully tempered
glass. The current mechanical load test MQT16 in IEC  61215 [28] focuses on frame defor-
mation, cell breakage, and all other non-glass related features. Testing the breakage of brittle
materials, such as glass, which is characterised by a probability of breakage, requires a larger
number of samples. As we know from the field, the rear glass is most affected by the breakage.
A mechanical pressure load is therefore effective for testing this failure. One current practical
option to test the reliability of a thin glass -based module is to test about 20 modules of one
type in the final mounting position to roughly estimate breakage rates down to 5%.
2.6 New material degradation modes specific to TOPCon and SHJ
According to industry experts and the 2024  International Technology Roadmap for Photovol-
taics (ITRPV), in the next decade TOPCon on n-type wafers will grow from 29% to 53% market
share, and n-type SHJs will grow from 5% to 19% [112]. TOPCon is expected to be the domi-
nating cell technology after 2025 [112]. Cell design is evolving rapidly, driven by manufacturing
needs such as reducing silver consumption, in addition to the need for higher device efficiency
and lower LCOE. TOPCon and SHJ cell architectures are evolving rapidly with new cell de-
signs being implemented and deployed in commercial PV modules in ~6-month time frames.
Therefore, the small amount of field data from TOPCon and SHJ cells may not be necessarily
representative for the modules currently or in the future being produced.
These advanced c-Si cell architectures mitigate the energy conversion losses present in tradi-
tional architectures. Both achieve higher VOC by minimising contact recombination, without re-
ducing the FF [113]. The introduction of new materials and processes introduces the potential
for new failure modes. Furthermore, there are broad parameter spaces available for materials
and designs that can affect both performance and long -term durability (e.g., the composition
of the paste used in metallization for TOPCon and SHJ, the a-Si:H layer and transparent con-
ductive oxid (TCO) in SHJs, the number and composition of passivation layers). Thus, there is
significant variability within a device technology, both as the composition of the layers evolve
towards improved efficiencies and as different manufacturers follow different paths towards
optimization. While field studies of degradation are the gold standard for understanding lon-
gevity, the findings become less transferable when critical materials change practically  every
six months.
2.6.1 Degradation of the front metal contacts of TOPCon
Metal pastes featuring glass frit are used across cell architectures to contact the front side of
PV cells, typically where the homojunction (i.e., emitter) is located. The glass frit enables the
metal paste to etch through the dielectric passivation and the antireflection coating on the front
side when fired at high temperatures. This approach is used for aluminium back surface field
(Al-BSF), PERC, nPERT, and now for TOPCon cells. When these cells are encapsulated with
EVA in the presence of moisture, the front metallization and cell-to-cell interconnects become
susceptible to corrosion at the interface between the metal and the Si [114], [115] , caused by
acetic acid, a decomposition product of EVA [116] . This has been observed in modules in-
stalled in the field [117] –[119], encapsulated modules exposed to accelerated DH testing
[120]–[123], and bare cells directly exposed to acetic acid [124], [125].
Recent reports have shown that TOPCon cells and modules can be even more susceptible to
this type of metal corrosion than Al-BSF and PERC [125]–[128]. Evidence of this corrosion in
the metal oxide glass frit has been observed in cross -sectional scanning electron microscopy
(SEM) images of TOPCon cells exposed directly to acetic acid, as shown in Figure 25 [125].

## Página 39

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
39
In this study, TOPCon cells experienced a significantly higher increase in the contact resistivity
over two hours of acetic acid exposure compared to the PERC and SHJ groups. DH testing on
unencapsulated PERC, SHJ, and TOPCon cells exposed to sodium chloride resulted in TOP-
Con exhibiting the highest level of power loss [126] . A similar study featuring TOPCon cells
with different pastes and a laser-assisted firing process used on some cells showed the corro-
sion sensitivity is likely related to a high aluminium content in the front paste [129]. Accelerated
damp-heat testing on encapsulated TOPCon has also shown substantial power loss. Sen et al.
evaluated seven combinations of encapsulation material and backsheet with TOPCon cells,
as well as three combinations with PERC cells. After 1000 hours of DH test, they found that
the maximum power loss in TOPCon modules varied significantly, ranging from 4%rel to 65%rel,
depending strongly on the encapsulation material. In contrast, PERC modules showed only a
1%rel to 2%rel power loss [128]. Sommeling and Kroon showed that the use of TPOs can miti-
gate power loss in 1000 h DH [127]. Unfortunately, there are limited reports on this form of
degradation in field exposed TOPCon modules, because it has only recently been adopted in
high-volume production.
Figure 25: a) SEM cross-sectional images and b) quantification of the energy-disper-
sive X-ray spectroscopy for the front side of the control and acetic acid treated bifacial
TOPCon metal paste contact interface to poly-Si emitter [125].
2.6.2 SHJ: ITO and a-Si:H degradation modes
The SHJ cell architecture limits contact recombination by decoupling the absorber from the
metal contact, by including a passivating, carrier selective contact layer stack. This stack com-
prises an intrinsic a-Si:H layer to passivate dangling bonds at the n-type c-Si wafer surface, a
doped a -Si:H layer provides carrier selectivity , and an appropriate TCO provides lateral
transport and ensures good contact quality with the metal. Typically, ITO is used as TCO. It
serves as an ARC and assists in light trapping at the cell’s rear.
SHJ cells are sensitive to stressors such as moisture, heat, and irradiance, and the resulting
degradation varies from manufacturer to manufacturer. A recent literature review [130] found
average performance loss rates for SHJ modules of 0.83%/year. These values fall between
the loss rates of c-Si and thin-film modules reported in 2016 [131].
A possible route of performance change specific to SHJ is the increase of ITO resistance or
deterioration of the a-Si:H/ITO or ITO/contact interfaces. Jordan et al. found that increased ITO
resistance has not been observed in fielded SHJ cells as compared to cells of a control module
kept indoors [132]. In degradation studies of non-encapsulated SHJ solar cells, X-ray photoe-
lectron spectroscopy (XPS) data of DH -exposed samples showed signatures of surface deg-
radation of the ITO and the surface gridlines. However, there was no corresponding change in
the device performance [133].

## Página 40

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
40
Another degradation mode related only to SHJ is studied by Arruti et al. [134]. Arruti et al. have
shown that bifacial rear-emitter SHJ solar cells encapsulated in EVA in glass/glass laminates
degraded in damp heat (DH) tests. However, DH tests with negative bias applied show a
slightly accelerated degradation compared to no voltage applied, see Figure 26. The degrada-
tion of the cell under negative bias is shown in the EL images in Figure 27. Modules in positive
bias voltage or positive bias voltage  with periods of illumination [22]  consistently exhibit no
degradation during the DH test. The prerequisite for degradation is explained by molecular
NaOH from the glass either diffusing through the EVA, which has absorbed moisture, or by
Na+ ions drifting due to the electric field when a negative bias is applied to the cell circuit.
Furthermore, with positive bias applied to the cell circuit, apparently Na+ ions are driven away
from the cell and therefore no degradation is  observed. In the study by Aruti et al., the sensi-
tivity to migrating Na+ seemed to be greater on cell fronts than on the rear side [134].

Figure 26: Normalised STC power to initial power of the front-side of SHJ 1-cell
glass/glass laminates with EVA, after 800 h of PID testing at 85°C/85% RH for the
bias conditions -1 kV, 0 V, and +1 kV. Figure is redrawn from Arruti et al. [134].

Figure 27: EL images of SHJ glass/glass mini-modules with EVA subjected to PID
testing at 85°C, 85% RH and -1 kV bias for up to 800 h. EL images show that degra-
dation starts at the edges of the cell, gradually expanding inward, associated with
moisture ingress facilitating Na+ transport [134].

## Página 41

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
41
The mechanisms of moisture damage are multifaceted, and have recently been explained by
a corrosion mechanism, see Figure 28 [135]. The adoption of encapsulants with a relatively
high water-uptake, such as EVA, favours a corrosion reaction of the glass cover(s) releasing
Na+ ions that, in combination with water, form molecular NaOH. Na + ions can diffuse through
the grain boundaries of the indium tin oxide (ITO), reaching either the front or rear hydrogen-
ated amorphous silicon (a-Si:H)/c-Si interface creating recombination centres for charge carri-
ers, see Figure 29.

Figure 28: Left: physical model explaining the
sensitivity of SHJ to water. The observed deg-
radation mechanism is specific to the SHJ
technology [135]. Right: Photoluminescence
image of one SHJ cell glass/glass laminate
taken at 0 h, 500 h and 1000 h of DH testing.

Figure 29: Schematic of the mi-
croscopic model proposed to ex-
plain the sensitivity to water of
SHJ cells encapsulated in a
glass/glass structure with EVA
encapsulant. Na+ and OH- ions
cross the ITO and degrade the
passivation layer at the
a-Si:H/bulk Si interface. Adapted
from [135].
However, to our knowledge,  there are no studies in which  SHJ modules installed  outdoors
exhibit PID. The humidity levels of the 85°C/85% RH condition leads to an unnaturally high
level of humidity in the module, entering from the module edges, as can be seen in Figure 27
and Figure 28. This accelerates Na+ migration considerably.
In the past, EVA alternatives such as thermoplastic polyolefin (TPO), ionomer [31]  and back-
sheets containing Al foil [136], which do not allow moisture to pass through as easily as EVA,
have been used for SHJ modules manufactured by Sanyo  [137]. Efforts are being made  to
reduce the costs by use of EVA and other module encapsulant s [137]. These authors found

## Página 42

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
42
dual issues of degradation by Na + diffusing from the glass due to water content in 85°C and
85% RH DH and damage from acetic acid formation of the EVA. They found good success in
glass/glass modules using POE in the front and rear of the cells and with POE on the front and
EVA on the rear of the cells with glass/backsheet constructions. Presumably in the later con-
figuration, the primary sensitivity to Na + is on the front side with these cells and the PID is
mitigated by use of the lower moisture transmission of the POE and use of backsheet allows
any acetic acid to diffuse out, thus mitigating acetic acid-based damage.
More recently, humidity induced degradation in SHJ was observed related to soldering flux and
contamination introduced onto the cell prior to module fabrication  [126], [138], [135]. These
contaminations must be avoided during production.
The water-sensitivity and PID in SHJ modules can be mitigated at module level by using a
high-volume resistivity encapsulant with a low WVTR and low water uptake (i.e., POE lamina-
tion material), appropriate edge sealants, proper rear and front covers, and/or the use of barrier
layers (glass/glass, glass/aluminium foil) [139].
2.6.3 UV degradation of current c-Si cell structures
Modern TOPCon, HJT, PERT, and PERC solar cells frequently show high degradation rates
in accelerated UV degradation tests [140], [18], [141].
Gebhardt et al. examined 14 different TOPCon types in UV test s showing severe power loss
ranging from 0.5% to 8% with a median of 3% after 60 kWh/m2 UV dose [18]. Shina conducted
similar tests with 28 TOPCon and 2 SHJ module types and found a degradation range from
0% to 10% and for SHJ from 1% to 2.5%  after applying also 60 kWh/m2 UV dose [140] . De-
pending on the location, 60 kWh/m2 UV dose corresponds to 1 to 2 years of outdoor exposure.
Both authors applied short-circuit conditions to the PV modules during the UV test.
Gebhardt et al. demonstrated that the power degradation of TOPCon modules in accelerated
UV tests and outdoor exposure is roughly halved when switching from short -circuit to open-
circuit conditions. This was observed for a small number of indoor tested samples and for a
single outdoor tested sample [18] . Sinha et a l. found similar results for UV tests with short -
circuit and open-circuit conditions of bare SHJ, n-PERT and p-PERC cells [142].
Dark storage strongly  accelerates the degradation of TOPCon modules after  UVID testing
[18],[143]. Heat storage conditions (85°C) can partly or completely reverse the dark storage
effect [18], [143].
The fundamental origin of the UVID are  UV triggered changes in the passivation efficiency of
the passivation stack/silicon interface [144], [142] or possibly a defect rich silicon surface for
the PERC cell front side [143] . The deposition methods and the process parameters of the
passivation layers have a great impact on the UV stability of the solar cell s [141],[145]. Pas-
sivation layers which prevent the silicon wafer surface from UV radiation below 360 nm , like
the rear passivation of TOPCon cells, by a UV blocking polysilicon layer, can be very UV stable.
No detailed outdoor studies on UVID are available for TOPCon modules . SHJ specific UV
degradation shows a reduction of V OC over time. It is  attributed to a partial loss of the front
passivating layers properties by UV irradiation. This problem was historically solved by moving
from front to rear -emitter SHJ solar cells. Jordan et al. compared the degradation of fielded
SHJ and PERC modules. While the observed degradation rates of the SHJ modules (-0.51%/a)
[144] are on par with conventional Si cell -technologies (-0.69% to -0.91%), the loss mecha-
nisms differ [146], [147]. PERC and Al-BSF cells primarily show performance losses due to a
reduction of ISC, whereas SHJ devices also experienced reductions in FF, but the degradation
was dominated by voltage loss. The loss was correlated with an increase in midgap trap

## Página 43

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
43
densities near the c -Si/a-Si:H interface due to weathering- related defects. This results in an
increased recombination current towards the interface between the bulk Si wafer and the junc-
tion-forming a-Si:H passivation layers. Sinha et al. compared the effect of UV exposure on the
performance of different non-encapsulated silicon architectures. Overall, they found that deg-
radation was more pronounced in emerging cell technologies, including SHJ devices, com-
pared to classic Al-BSF devices [142]. The authors concluded that the damage to the SHJ cells
originates from hydrogen effusion near the surface, followed by its migration into the bulk Si,
leading to increased recombination current loss. Furthermore, Bertoni’s work [148], [149] with
surface recombination velocity measurements of c -Si/a-Si:H stacks supports the degradation
of the surface passivation layer as a root cause of the observed loss performance over time.
Even if the root causes differ for all cell types and passivation stacks, the main UVID acceler-
ating factor is the amount of UV photons reaching the passivation layer/silicon interface. Any
means of reducing this amount, like UV reflecting ARC, UV-absorbing glass, lamination mate-
rial, or passivation layer can mitigate the UVID impact [142].
As the operating point in a PV generator is the maximum power point and not the short-circuit
conditions as used in the UV tests, the field degradation rate may be lower than the UV dose
in the accelerated aging test suggests. Light soaking may recover UVID for HJT modules [150].
The strong dark storage degradation reported after UVID tests of TOPCon modules may ac-
celerate the field degradation during nighttime. However, the reported UVID test s also show
that there are some UV stable TOPCon and HJT modules on the market. We can expect man-
ufacturers to mitigate the high UVID rates found in standard UV tests.
UVID testing can induce LeTID/LID effects in addition to  chemical changes at the irradiated
semiconductor layers and interfaces of a solar cell. To separate both effects, it is important to
keep the cell and module temperature below 60°C during UV degradation tests  [151]. Addi-
tionally, a light soaking procedure IEC 61215 MQT 01 and a LeTID test IEC  61215 MQT 23
should be done before UVID testing. So far, we recommend an extended UV degradation test
for PV modules with 60 kWh/m2 UV irradiation dose under short-circuit conditions to assess
the module quality between different module products.

## Página 44

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
44
 PEROVSKITE-BASED FUTURE TECHNOLOGIES
Metal halide perovskite PV cells have attracted considerable research and development inter-
est as an alternative to c -Si PV absorber material and as an addition to c -Si in tandem struc-
tures. This excitement is due to their meteoric rise in record cell efficienc ies [152] since their
discovery in 2009 [153], their potential for very low production costs, and their bandgap tuna-
bility [154]. While record efficiencies have reached parity with c -Si, the ability of perovskite
solar cells (PSCs) and in particular larger area modules to survive outdoor operating conditions
is still uncertain with a wide variability in reported lifetimes for laboratory samples. This chapter
provides a summary of degradation mechanisms of MHP -based PV cells and modules and
their mitigation based on the work of Baumann et al. [155].
There are several known degradation modes for MHP PV cells and modules. These include
intrinsic (pertaining to material properties), cell-device-specific (pertaining to device design
and manufacturing), extrinsic  (pertaining to environmental stressors), and module- device-
specific (pertaining to the interconnection of cells into modules and embedment). In the fol-
lowing sections, we introduce degradation models for each type and highlight mitigation strat-
egies that are under investigation.
3.1 Intrinsic degradation causes
Phase instability and impurity – The perovskite structure of typical MHP PV has a cubic unit
cell with a molecular formula of ABX 3, where A is either an organic molecule (e.g., Forma-
midinium (FA)), or an inorganic element (e.g., Cs) or a mixture of both; B is a metal (Pb or Sn),
and X is a halide (Cl, Br, or I). If any of the A, B, or X components has an effective ionic radius
that is too large or too small  compared to the other constituents, the cubic structure cannot
form, due to physical space constraints, leading to the formation of undesired phases. In addi-
tion, the stability of the structure can change with temperature leading to phase instability dur-
ing operation. For example, both FAPbI3 and CsPbI3 are not stable in the cubic phase at typical
operating temperatures (-45°C to 85°C). However, a common practice to mitigate phase insta-
bility is to alloy these two constituents to create a stable cubic formulation over  a range of
operating temperatures. Phase instability can also be caused by leftover MHP precursor and
phase impurities. MHP layers are typically deposited as liquid inks and then annealed to create
solid thin films. A common instability occurs when the mixing and solubility of the MHP ink is
not optimal or the ink has degraded. PbI 2 can photolyze under illumination where it absorbs
light, i.e. blue or UV light, breaking down into I2 and metallic Pb among other by-products [156]–
[159]. This can lead to phase segregation and degradation at nucleation sites. Mitigation op-
tions include optimization of composition, stoichiometry [158], [160] , and processing to , for
example, minimise PbI2 residues or, if possible, to avoid them completely. P ost-treatments to
remove unwanted phases may also be possible.
Phase segregation (cation/halide) – Mixed cation/mixed halide MHP compositions are fa-
voured for high efficiency and a band gap ideally suited for MHP/Si tandem cells. Such alloyed
compositions may be energetically prone to de-mixing, leading to the formation of non -cubic
phases or even the coexistence of different phases simultaneously. To test if a given compo-
sition will phase-segregate under operating conditions, crystallographic studies as a function
of time under realistic conditions are needed. Using a spatial/structural analysis technique,
such as nano-XRD or time-of-flight secondary ion mass spectroscopy (ToF-SIMS), can detect
the scale, morphology, and composition of segregated phases [161]. To prevent phase segre-
gation energetic calculations should be carried out on a given composition to determine which
are more or less likely to de- mix. Segregation can be suppressed by keeping Br <20% in the

## Página 45

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
45
case of halide segregation, reducing defect densities, growing single crystal MHPs [162], [163],
and adding Cs+, Rb+, or K+ in the case of cation segregation [164].
Ion Migration - MHP materials are mixed electronic/ionic conductors with a low activation
energy for the formation of mobile ions [165], [166] . Mobile ion concentrations in MHP are
several orders of magnitude higher than in conventional semiconductors (Si, CdTe, III -V) and
this can lead to IV hysteresis [167], [168], photoinduced low-frequency capacitance [169], pho-
toluminescent quantum yield changes, halide segregation, and various other irreversible deg-
radation modes [170], [171].  When exposed to light, a PV device generates an electric field
that can move (drift) ions. At night, these ions can move according to concentration gradients.
To mitigate ion migration, researchers are investigating a variety of solutions [172] , including
compositional engineering (e.g., adding large A site cations [173], [174]), 2D and 1D MHPs
[175], [176], increasing grain size and modifying grain boundaries [177], [178], additives (e.g.,
ionic fluids [179], polymers [180], potassium salts [181], [182]), passivation, and blocking layers
(e.g., diethylammonium formate (DMAFo), thermotropic liquid crystals like 3,4,5 - trifluoro-4’-
(trans-4-propylcyclohexyl)biphenyl, CsPbI1.85Br1.15 quantum dots, tri-s-triazine-based graphitic
carbon nitride).
Thermal Degradation - When exposed to high temperatures, MHP PV absorbers decompose
into gaseous carbon and nitrogen compounds and solid PbI 2, depending on composition and
temperature. In order for MHP PV modules to be commercialised, they must be able withstand
temperatures at least up to ~ 85°C, over a complete diurnal (light/dark) cycle [6]. Mitigation
strategies include reducing ion migration with blocking layers, thermotropic liquid crystals [183]
or quantum dots [184], adding thermally conductive materials to remove heat, and/or avoiding
extreme climates.
Mechanical Degradation - MHP PV materials are very weak/soft, resulting in possible dam-
age during fabrication (soldering, finger screen printing, lamination) and operation. 2D MHPs
are even weaker than 3D [185]. Mitigation strategies include material selection and, in the case
of 2D MHPs, engineering to increase the strength of the MHP layer, increasing the number of
inorganic layers, and adding a strong insulating layer between the electrode and the intercon-
nector [186].
3.2 Cell-device-specific degradation modes
Charge transport and passivation layer reactions - Charge transport layers (CTLs) should
remain connected to the MHP layer and be stable under operational conditions. Instability can
be caused by both chemical and mechanical processes and has proven  to be a particularly
significant challenge for MHP devices. Most of the materials used for CTLs have stability is-
sues when exposed to light and UV radiation [187]–[190]. Mitigation options include choosing
an intrinsically stable inorganic material such as metal oxides [191] or sulphides [192], mini-
mising CTL reactivity with MHP by choosing a CTL that is neither acidic nor basic, and also
screening for light + heat sensitivity in the final device.
Electrode-induced degradation – Strong chemical gradients across the interfaces of elec-
trode, CTL and MHP materials drive reactions and ion migration that negatively impact perfor-
mance and stability [193]. Most metals chosen as electrodes for PSCs react with the MHP
[157], [170], [194]. To mitigate these reactions, electrode interlayers made of Ti [195] or metal
oxides (e.g., ZnO [196], Cr-Cr2O3 [197], g-C3N4 [198], MoOx [199], [200]) are proposed. Despite
advances, electrode-induced degradation remains a major challenge. One approach is to re-
place the metal with either carbon as the electrode [201] –[203] or transparent conducting ox-
ides [204], [205]. However, to date, devices with non-metallic electrodes exhibit high resistive
losses and lower efficiencies.

## Página 46

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
46
Degradation related to scribe processing – Scribing is used to separate and interconnect
individual cells into modules. Ultrafast pulse width laser scribing is favoured , as it does not
transfer high heat loads to the material [206], [207], which can cause melting. However, faster
picosecond lasers remove material via a mechanical stress-assisted lift-off mechanism result-
ing in steep edges and less residue, but may lead to microcracks and delamination [208] –
[210]. Studies have shown that the edges of laser scribes decompose to PbI2, forming a type-
I heterojunction with surrounding MHP [211] –[213]. Using carbon -based electrodes [214]  or
TCOs [215], [216] may be a mitigation method. Alternatively, adding a diffusion barrier inside
laser scribe line P2 (e.g., Al 2O3, nanoparticles, polydimethylsiloxane (PDMS), carbon nitride
[198], or CTL [217]) to separate the MHP and electrode is being considered.
Strain induced by differences in CTE – The variety of materials used in MHP cells and mod-
ules have a range of different CTEs and therefore, when the MHP layer is annealed at ~100°C
and then cooled, the film is in a state of elevated stress. Encapsulation can also introduce
stress in the cooled modules. Mitigations include replacing thermal annealing with longer pro-
cessing steps at lower temperatures [218], but adding processing time may not be feasible in
commercial production lines. Other authors have suggested additives to reduce tensile stress
including octylammonium iodide (OAI) and phenethylammonium iodide (PEAI) [219].
3.3 Extrinsic degradation causes
Reactions with water vapour and oxygen – MHP layers are generally hydrophilic and de-
grade in the presence of water as the organic cations oxidise [220] . The degradation mecha-
nisms related to oxygen are not fully understood but are enhanced by exposure to light, espe-
cially organic components in the MHP and CTL layers [221]–[224]. Mitigation strategies include
encapsulation and the embedding of glass-glass modules to prevent water and O2 from coming
into contact with the device. The addition of lower dimensional MHP layers between the ab-
sorber and ETL [225], and other additives (e.g., TFPCBP [226]) can help reduce the effect of
moisture. Some of the solutions for intrinsic degradation modes related to ion mobility are likely
to help with the effects of water and O2 reactivity.
Reverse voltage – MHPs are very sensitive to and can degrade by even low levels of reverse
voltage (< -5 V), which causes band bending and ion crowding near the MHP -CTL interfaces
[227], [228] and possibly leading to the oxidation of iodide [228]. Local shunts can form, espe-
cially when metal electrodes are used [227], [229], which can lead to local heating and further
damage to the cell [230], [231] . Options for mitigating the bias sensitivity and degradation in-
clude using non-metal electrodes [231], blocking layers [232], TCO between HTL and metal
electrodes [233], polymer HTLs [234]. Despite showing some improvements, none of the po-
tential solutions have been shown to prevent damage to the cell from reverse bias conditions,
yet.
3.4 Module-device-specific degradation modes
Module layout and embedment – MHP modules perform best if water and O2 are not allowed
to react with the layers of the device stack. In addition to glass -glass module designs, PO -
based encapsulants are recommended rather than EVA, which requires higher lamination tem-
peratures [235] and can produce acetic acid [236]–[238]. POEs also have lower WVTRs.
Potential-induced degradation – In string-connected modules, high PV system voltages (up
to ± 1500 V, can build up between grounded module frames and solar cells under operation
[239]. Several PID tests are performed on PSCs and MHP/Si tandem solar cells/minimodules,
showing no degradation at positive voltages but much  more pronounced degradation at

## Página 47

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
47
negative voltages and also at higher temperatures due to movement of Na+ ions from the glass
into the MHP layer, causing recombination centres [240]–[242]. Other ion movements are ob-
served such as Pb+, Cs+, Br- and I- towards the encapsulant materials and Ag + ions from the
back contact leading to the formation of AgI. The PID degradation can be mitigated by optimis-
ing the fabrication and deposition of MHP layers , resulting in low defect densities (i.e. I -rich
synthesis conditions), using MHP compositions with high defect tolerance [243] and adding
either additional barrier layer (e.g. PCBM between SnO2 (HTL) and MHP) [244] or inert mate-
rials that occupy interstitials in the MHP structure to inhibit Na + penetration [240]. Other miti-
gation strategies could be used such as inducing recovery of MHP by applying positive bias
during the night to drive Na+ ions out of the active layer [245] or using suitable encapsulation
material [241].
Testing and qualification - Accelerated indoor tests reproduce the standard 20 years of out-
door functioning in much shorter times , enabling reliable predictive analysis. The IEC 61215
series 2021 standards [6], [246]–[248] are developed to assess the reliability of PV modules .
They contain accelerated ageing protocols, including climatic (e.g. DH, TC, HF, ...), mechani-
cal (e.g. mechanical loads and hail impact), and electrical (e.g. PID, wet and dry insulation)
tests in addition to electrical and mechanical safety requirements as addressed in the IEC
61730:2023 [249]. Other tests can be tailored to cope with some technology specificities such
as the International Summit on Organic PV stability  protocols, as in the case of MHPs. Com-
pliance with  these standards is generally considered a minimum quality requirement and
should be considered a prerequisite for MHP module commercialization.

## Página 48

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
48
 CONCLUSION
It is recommended to review published reports on PV failures observed for the type of cell/mod-
ule technologies being used in a PV project. In order to reduce the number of failures in large
PV systems, the impact of the corresponding degradation modes should be verified by accel-
erated testing prior to their installation. For 2024, the main cell related degradation modes are
PID, UVID, and humidity related corrosion for SHJ and TOPCon modules.
From the perspective of the module design glass breakage failure for bifacial glass/glass mod-
ules with thin glass got a high relevance in the field. The more power is achieved per module
and in the module string , the more important the safety measures become, as the conse-
quences of an imperfectly connected BPD can lead to a fire much more easily than before.
All these degradation/failure causes are known from former failure reports. However, due to
new methods for passivation layer, metallization and thin glass , the reliability of the modules
has to be reoptimized for these new manufacturing processes. Some of the reported degrada-
tion issues may already been solved from PV module manufacturers by the time this report is
published. The most important standard IEC 61215 [6] does not cover the UVID, because the
UV test included in the standard is too short and may not take recovery effects into account.
Similarly, for PID effects in SHJ PV module types, it is still not clear how the PID test represents
relevant conditions in the field, as the influence of recovery conditions in the application has
not yet been tested. More research is needed to adapt the UVID and PID tests. For the humidity
related corrosion of TOPCon and SHJ the main root cause (TOPCon: degradation of the front
metal contacts, SHJ: Na related degradation of the a -Si-layer) is known . By optimizing the
high-volume resistivity encapsulant with a low WVTR and low water uptake , the degradation
speed can be mitigated . However, the relevance in the field is unknown and needs more re-
search.  Furthermore, glass breakage rates cannot be detected within the IEC 61215 mechan-
ical load test, because for a brittle glass material much more than one test sample is needed
to detect a failure rate of 10% and below.  In particular when optimising the glass thickness
closer to the appli cation load, the according test must be much more precise.  Therefore, we
need extended standard tests for these types of failures for the current PV technologies, which
is ongoing work.
Process instabilities that lead to unreliable cold solder joints in junction boxes must be moni-
tored as an integral part of production control.  As the correct function of the BPDs is very
important for safety, we recommend checking the BPD function during the module production
and performing a module string wise diode test during the construction phase of the PV system.
If there are indications of probable cold solder joints in some of the junction boxes , the whole
PV system should be checked for cold solder joints in the junction b oxes. The risk of  a fire
within the service life of the PV system is high in this scenario.
On a positive note LeTID and cell crack degradation are still a possible degradation mode but
their relevance practically vanished in the new PV module types based on TOPCon  and SHJ
cells, as well as multi-wire connection technology. As LeTID is reduced using thinner and thin-
ner wafers, the effect may vanish even further as the wafer thickness continues to decrease
with new technology steps. Glass/glass encapsulation is becoming increasingly popular. This
trend can support humidity sensitive cell technologies like TOPCon which are less affected by
humidity than in glass/backsheet BOMs. Thus, the shift to glass/glass modules protects cell
technologies which are less moisture resistive. Furthermore, the chemical interaction and ma-
terial variety are also reduced in glass/glass module designs compared to glass/backsheet
modules.

## Página 49

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
49
For future PV technologies based on MHP -containing cells and modules , we relied only on
published literature data to support our findings. Reliability data from commercial products
were not available to the authors of this report. In the literature, nearly all types of degradation
mechanisms, and therefore all kinds of tests are highly relevant. Ion migration is a dominant
characteristic involved in many published degradation modes , such as chemical interface re-
actions, phase changes, reverse voltage instab ility, PID,  and metastability of the electrical
characteristic, such as IV curve hysteresis. In this way, mitigating ion migration in MHP con-
taining solar cells might be a way to solve many degradation pathways at once.
Today’s silicon-based module designs must withstand h igh absorber temperatures above
150°C and more during partial shading. Many researchers wrongly assume that MHP absorb-
ers/solar cells only need to be stable up to 85°C . In fact,  the number of cells per BPD, the
reverse voltage characteristic of the cells and the cell efficiency determine the maximum cell
temperature in the application profile. We would need new (and expensive) module designs
allowing this low application temperature of 85°C in reality. Some types of degradation mech-
anisms for MHP solar cells, such as PID and hot spot tests, have not yet been tested for real-
istic scenarios in the literature. We recommend not losing focus on the corresponding tests for
MHP-containing solar cells and modules. For commercial products , all known degradation
pathways must be mitigated simultaneously, as all degradation pathways have a major impact
on MHP-based PV modules.

## Página 50

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
50
REFERENCES
[1] M. Köntges et al., “Review of Failures of Photovoltaic Modules,” Report IEA-PVPS T13-
01:2014, 2014. [Online]. Available: http://iea-pvps.org/index.php?id=275 [Accessed 18-
Sep-2014]
[2] M. Köntges et al., “Assessment of Photovoltaic Module Failures in the Field,” IEA PVPS,
2017. [Online]. Available: http://www.iea-pvps.org/index.php?id=435
[3] M. Herz, G. Friesen, U. Jahn, M. Köntges, S. Lindig, and D. Moser, Quantification of
Technical Risks in PV Power Systems 2021, IEA-PVPS T13-23:2021. IEA PVPS, 2021.
[Online]. Available: https://iea- pvps.org/wp-content/uploads/2021/11/Report-IEA–
PVPS-T13-23_2021-Quantification-of-Technical-Risks-in-PV-Power-Systems_final.pdf
[4] D. C. Jordan, T. J. Silverman, J. H. Wohlgemuth, S. R. Kurtz, and K. T. VanSant,
“Photovoltaic failure and degradation modes,” Prog. Photovoltaics Res. Appl. , vol. 25,
no. 4, pp. 318–326, Apr. 2017, doi: 10.1002/pip.2866.
[5] G. Friesen et al. , “Photovoltaic Failure Fact Sheets (PVFS),” Report IEA -PVPS T13-
30:2024, 2025. [Online]. Available: https://iea -
pvps.org/publications/?year_p=&task=67&order=DESC&keyword=&cpt=keytopics&ke
ytopic=
[6] Terrestrial photovoltaic (PV) modules -  Design qualification and type approval, IEC
61215-Series-2021. 2021.
[7] S. Hwang and Y. Kang, “Reliability study on the half -cutting PERC solar cell and
module,” Energy Reports, vol. 10, pp. 678–685, 2023, doi: 10.1016/j.egyr.2023.07.023.
[8] F. Kaule, M. Pander, M. Turek, M. Grimm, E. Hofmueller, and S. Schoenfelder,
“Mechanical damage of half -cell cutting technologies in solar cells and module
laminates,” AIP Conf. Proc. , vol. 1999, no. February 2022, 2018, doi:
10.1063/1.5049252.
[9] F. Fertig, K. Krauß, and S. Rein, “Light-induced degradation of PECVD aluminium oxide
passivated silicon solar cells,” Phys. status solidi - Rapid Res. Lett. , vol. 9, no. 1, pp.
41–46, Jan. 2015, doi: 10.1002/pssr.201409424.
[10] D. Chen et al. , “Investigating the degradation behaviours of n+- doped Poly -Si
passivation layers: An outlook on long- term stability and accelerated recovery,” Sol.
Energy Mater. Sol. Cells , vol. 236, no. May 2021, p. 111491, 2022, doi:
10.1016/j.solmat.2021.111491.
[11] D. Macdonald and L. J. Geerligs, “Recombination activity of interstitial iron and other
transition metal point defects in p- and n-type crystalline silicon,” Appl. Phys. Lett., vol.
85, no. 18, pp. 4061–4063, Nov. 2004, doi: 10.1063/1.1812833.
[12] J. Karas et al., “Results from an international interlaboratory study on light‐ and elevated
temperature‐induced degradation in solar modules,” Prog. Photovoltaics Res. Appl., vol.
30, no. 11, pp. 1255–1269, Nov. 2022, doi: 10.1002/pip.3573.
[13] D. Chen et al. , “Progress in the understanding of light ‐ and elevated temperature ‐
induced degradation in silicon solar cells: A review,” Prog. Photovoltaics Res. Appl., vol.
29, no. 11, pp. 1180–1201, Nov. 2021, doi: 10.1002/pip.3362.
[14] R. Eberle, W. Kwapil, F. Schindler, M. C. Schubert, and S. W. Glunz, “Impact of the
firing temperature profile on light induced degradation of multicrystalline silicon,” Phys.

## Página 51

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
51
status solidi –  Rapid Res. Lett. , vol. 10, no. 12, pp. 861– 865, Dec. 2016, doi:
10.1002/pssr.201600272.
[15] C. E. Chan et al. , “Rapid Stabilization of High- Performance Multicrystalline P -type
Silicon PERC Cells,” IEEE J. Photovoltaics , vol. 6, no. 6, pp. 1473– 1479, Nov. 2016,
doi: 10.1109/JPHOTOV.2016.2606704.
[16] D. Bredemeier, D. C. Walter, and J. Schmidt, “Possible Candidates for Impurities in mc‐
Si Wafers Responsible for Light‐Induced Lifetime Degradation and Regeneration,” Sol.
RRL, vol. 2, no. 1, Jan. 2018, doi: 10.1002/solr.201700159.
[17] F. T. Thome, C. Yilmaz, W. Kwapil, F. Schindler, and M. C. Schubert, “Why is gallium -
doped silicon (sometimes) stable? Kinetics of light and elevated temperature induced
degradation,” Sol. Energy Mater. Sol. Cells , vol. 275, p. 112986, Sep. 2024, doi:
10.1016/j.solmat.2024.112986.
[18] P. Gebhardt, U. Kräling, E. Fokuhl, I. Haedrich, and D. Philipp, “Reliability of Commercial
TOPCon PV Modules -  An Extensive Comparative Study,” Prog. Photovoltaics Res.
Appl., 2024, doi: 10.24406/publica-3553.
[19] C. Molto et al. , “Review of Potential ‐Induced Degradation in Bifacial Photovoltaic
Modules,” Energy Technol., vol. 11, no. 4, Apr. 2023, doi: 10.1002/ente.202200943.
[20] W. Luo et al. , “Elucidating potential ‐induced degradation in bifacial PERC silicon
photovoltaic modules,” Prog. Photovoltaics Res. Appl. , vol. 26, no. 10, pp. 859 –867,
Oct. 2018, doi: 10.1002/pip.3028.
[21] K. Sporleder, V. Naumann, J. Bauer, D. Hevisov, M. Turek, and C. Hagendorf, “Time ‐
Resolved Investigation of Transient Field Effect Passivation States during Potential ‐
Induced Degradation and Recovery of Bifacial Silicon Solar Cells,” Sol. RRL, vol. 5, no.
7, Jul. 2021, doi: 10.1002/solr.202100140.
[22] P. Hacke et al., “Evaluation of bifacial module technologies with combined-accelerated
stress testing,” Prog. Photovoltaics Res. Appl. , vol. 31, no. 12, pp. 1270 –1284, Dec.
2023, doi: 10.1002/pip.3636.
[23] P. Hacke et al. , “Polarization -Type Potential -Induced Degradation in Bifacial PERC
Modules in the Field,” in Proc. 41st EUPVSEC, in Press, Vienna, Austria: WIP, 2024.
[24] T. Pu, H. Shen, K. H. Neoh, F. Ye, and Q. Tang, “Reduced power degradation in bifacial
PERC modules by a rear silicon oxide additive layer,” Int. J. Energy Res., vol. 45, no. 6,
pp. 8659–8665, May 2021, doi: 10.1002/er.6402.
[25] P. Hacke, S. Spataru, B. Habersberger, and Y. Chen, “Field‐ representative evaluation
of PID ‐polarization in TOPCon PV modules by accelerated stress testing,” Prog.
Photovoltaics Res. Appl., vol. 32, no. 5, pp. 346–355, May 2024, doi: 10.1002/pip.3774.
[26] Photovoltaic (PV) modules - Test methods for the detection of potential -induced
degradation - Part 1: Crystalline silicon, IEC 62804-1-2015. VDE, 2015.
[27] Photovoltaic (PV) modules - Test methods for the detection of potential -induced
degradation - Part 1: Crystalline silicon, IEC 62804-1-2025. VDE, 2025.
[28] Terrestrial photovoltaic (PV) modules - Design qualification and type approval - Part 2:
Test procedures, IEC 61215-2-2021. 2021.
[29] W. Luo et al. , “Investigation of polysilicon passivated contact’s resilience to potential -
induced degradation,” Sol. Energy Mater. Sol. Cells, vol. 195, pp. 168–173, Jun. 2019,
doi: 10.1016/j.solmat.2019.02.038.

## Página 52

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
52
[30] W. Luo et al. , “Investigation of Potential -Induced Degradation in Bifacial n- PERL
Modules,” IEEE J. Photovoltaics , vol. 10, no. 4, pp. 935 –939, Jul. 2020, doi:
10.1109/JPHOTOV.2020.2981841.
[31] S. Yamaguchi, K. Nakamura, A. Masuda, and K. Ohdaira, “Rapid progression and
subsequent saturation of polarization-type potential-induced degradation of n-type front-
emitter crystalline-silicon photovoltaic modules,” Jpn. J. Appl. Phys. , vol. 57, no. 12, p.
122301, Dec. 2018, doi: 10.7567/JJAP.57.122301.
[32] B. M. Habersberger and P. Hacke, “Impact of illumination and encapsulant resistivity on
polarization‐type potential‐induced degradation on n ‐PERT cells,” Prog. Photovoltaics
Res. Appl., vol. 30, no. 5, pp. 455–463, May 2022, doi: 10.1002/pip.3505.
[33] K. Ohdaira, M. Akitomi, Y. Chiba, and A. Masuda, “Potential -induced degradation of n-
type front -emitter crystalline silicon photovoltaic modules — Comparison between
indoor and outdoor test results,” Sol. Energy Mater. Sol. Cells, vol. 249, p. 112038, Jan.
2023, doi: 10.1016/j.solmat.2022.112038.
[34] K. A. Kim and P. T. Krein, “Photovoltaic hot spot analysis for cells with various reverse-
bias characteristics through electrical and thermal simulation,” in 2013 IEEE 14th
Workshop on Control and Modeling for Power Electronics (COMPEL), IEEE, Jun. 2013,
pp. 1–8. doi: 10.1109/COMPEL.2013.6626399.
[35] R. Witteck, M. Siebert, S. Blankemeyer, H. Schulte -Huxel, and M. Köntges, “Three
Bypass Diodes Architecture at the Limit,” IEEE J. Photovoltaics, vol. 10, no. 6, pp. 1828–
1838, Nov. 2020, doi: 10.1109/jphotov.2020.3021348.
[36] C. Reichel et al. , “Design aspects in consideration of hotspot phenomena in high -
performance photovoltaic modules featuring different silicon solar cell architectures,”
Sol. Energy Mater. Sol. Cells , vol. 276, no. July, p. 113058, 2024, doi:
10.1016/j.solmat.2024.113058.
[37] Y. Jia et al., “Diagnosing breakdown mechanisms in monocrystalline silicon solar cells
via electroluminescence imaging,” Sol. Energy, vol. 225, pp. 463–470, Sep. 2021, doi:
10.1016/j.solener.2021.07.052.
[38] D. C. Jordan, T. J. Silverman, J. H. Wohlgemuth, S. R. Kurtz, and K. T. VanSant,
“Photovoltaic failure and degradation modes,” Prog. Photovoltaics Res. Appl. , vol. 25,
no. 4, pp. 318–326, Jan. 2017, doi: 10.1002/pip.2866.
[39] M. C. A. García, W. Herrmann, W. Böhmer, and B. Proisy, “Thermal and electrical
effects caused by outdoor hot -spot testing in associations of photovoltaic cells,” Prog.
Photovoltaics Res. Appl. , vol. 11, no. 5, pp. 293– 307, 2003, doi:
https://doi.org/10.1002/pip.490.
[40] K. A. Kim and P. T. Krein, “Hot spotting and second breakdown effects on reverse I -V
characteristics for mono-crystalline Si Photovoltaics,” in 2013 IEEE Energy Conversion
Congress and Exposition , IEEE, Sep. 2013, pp. 1007 –1014. doi:
10.1109/ECCE.2013.6646813.
[41] J. Appelbaum, A. Chait, and D. Thompson, “Parameter estimation and screening of
solar cells,” Prog. Photovoltaics Res. Appl. , vol. 1, no. 2, pp. 93– 106, Feb. 1993, doi:
10.1002/pip.4670010202.
[42] J. Hudson, L. Vasilyev, J. Schmidt, and G. Horner, “Economic impacts and approaches
to address hot -spot defects in photovoltaic devices,” in 2010 35th IEEE Photovoltaic
Specialists Conference, IEEE, Jun. 2010, pp. 001706– 001709. doi:
10.1109/PVSC.2010.5616102.

## Página 53

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
53
[43] R. G. Vieira, F. M. U. de Araújo, M. Dhimish, and M. I. S. Guerra, “A comprehensive
review on bypass diode application on photovoltaic modules,” Energies, vol. 13, no. 10,
p. 2472, 2020, doi: 10.3390/en13102472.
[44] H. Hanifi, J. Schneider, and J. Bagdahn, “Reduced shading effect on half -cell modules
– Measurement and simulation,” in 31st European Photovoltaic Solar Energy
Conference and Exhibition, 2015, pp. 2529–2533.
[45] D. Götz, D. Hahn, R. Gottschalg, D. Dassler, S. Schindler, and H. Hanifi, “Evaluation of
shading tolerance of PV modules with different module designs for mobile applications
by simulation, indoor and outdoor measurements,” in 36th European Photovoltaic Solar
Energy Conference and Exhibition, 2019.
[46] N. Klasen, D. Weisser, T. Rößler, D. H. Neuhaus, and A. Kraft, “Performance of shingled
solar modules under partial shading,” Prog. Photovoltaics Res. Appl., vol. 30, no. 4, pp.
325–338, Apr. 2022, doi: 10.1002/pip.3486.
[47] H. Sträter and S. Riechelmann, “An approach for a shading resistance classification of
PV modules,” in 8th World Conference on Photovoltaic Energy Conversion, Milano,
2022, pp. 492–497.
[48] E. Özkalay, F. Valoti, M. Caccivio, A. Virtuani, G. Friesen, and C. Ballif, “The effect of
partial shading on the reliability of photovoltaic modules in the built -environment,” EPJ
Photovoltaics, vol. 15, p. 7, Feb. 2024, doi: 10.1051/epjpv/2024001.
[49] H. Chu, L. J. Koduvelikulathu, V. D. Mihailetchi, G. Galbiati, A. Halm, and R. Kopecek,
“Soft Breakdown Behavior of Interdigitated- back-contact Silicon Solar Cells,” Energy
Procedia, vol. 77, pp. 29–35, Aug. 2015, doi: 10.1016/j.egypro.2015.07.006.
[50] R. Müller et al. , “Analysis of n -type IBC solar cells with diffused boron emitter locally
blocked by implanted phosphorus,” Sol. Energy Mater. Sol. Cells , vol. 142, pp. 54– 59,
Nov. 2015, doi: 10.1016/j.solmat.2015.05.046.
[51] S. Deng et al. , “Research on hot spot risk for high- efficiency solar module,” Energy
Procedia, vol. 130, pp. 77–86, Sep. 2017, doi: 10.1016/j.egypro.2017.09.399.
[52] T. Geipel, M. Moeller, J. Walter, A. Kraft, and U. Eitner, “Intermetallic compounds in
solar cell interconnections: Microstructure and growth kinetics,” Sol. Energy Mater. Sol.
Cells, vol. 159, pp. 370–388, 2017, doi: https://doi.org/10.1016/j.solmat.2016.08.039.
[53] D. Phillip, H. Manuel, E. Fokuhl, and G. Mülhöfer, “Hot -spot endurance test —
Modifications for bifacial photovoltaic modules,” in 35th European Photovoltaic Solar
Energy Conference & Exhibition, 2018.
[54] Y. Zhang, Y. Yu, F. Meng, and Z. Liu, “Experimental Investigation of the Shading and
Mismatch Effects on the Performance of Bifacial Photovoltaic Modules,” IEEE J.
Photovoltaics, vol. 10, no. 1, pp. 296– 305, 2020, doi:
10.1109/JPHOTOV.2019.2949766.
[55] C. Xiao, P. Hacke, S. Johnston, D. B. Sulas ‐Kern, C. -S. Jiang, and M. Al ‐Jassim,
“Failure analysis of field‐failed bypass diodes,” Prog. Photovoltaics Res. Appl. , vol. 28,
no. 9, pp. 909–918, Sep. 2020, doi: 10.1002/pip.3297.
[56] D. C. Jordan, N. Haegel, and T. M. Barnes, “Photovoltaics module reliability for the
terawatt age,” Prog. Energy, vol. 4, no. 2, 2022, doi: 10.1088/2516-1083/ac6111.
[57] H. E. Yang, R. H. French, and L. S. Bruckman, Durability and Reliability of Polymers
and Other Materials in Photovoltaic Modules . Elsevier, 2018. doi: 10.1016/C2016- 0-
01032-X.

## Página 54

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
54
[58] Y. Voronko, G. C. Eder, M. Knausz, G. Oreski, T. Koch, and K. A. Berger, “Correlation
of the loss in photovoltaic module performance with the ageing behaviour of the
backsheets used,” Prog. Photovoltaics Res. Appl., vol. 23, no. 11, pp. 1501–1515, Nov.
2015, doi: 10.1002/pip.2580.
[59] G. Oreski et al., “Properties and degradation behaviour of polyolefin encapsulants for
photovoltaic modules,” Prog. Photovoltaics Res. Appl., vol. 28, no. 12, pp. 1277–1288,
Dec. 2020, doi: 10.1002/pip.3323.
[60] G. Oreski et al., “Performance of PV modules using co -extruded backsheets based on
polypropylene,” Sol. Energy Mater. Sol. Cells , vol. 223, p. 110976, 2021, doi:
10.1016/j.solmat.2021.110976.
[61] B. Brune et al., “Quantifying the influence of encapsulant and backsheet composition on
PV-power and electrical degradation,” Prog. Photovoltaics Res. Appl., vol. 31, no. 7, pp.
716–728, 2023, doi: 10.1002/pip.3679.
[62] E. Bonekamp, Jeffrey and H. Zhang, “Polyolefin photovoltaic backsheet comprising a
stabilized polypropylene layer,” 2017
[63] B. Adothu et al. , “Newly developed thermoplastic polyolefin encapsulant –A potential
candidate for crystalline silicon photovoltaic modules encapsulation,” Sol. Energy, vol.
194, no. July, pp. 581–588, 2019, doi: 10.1016/j.solener.2019.11.018.
[64] G. Beaucarne et al. , “Low temperature solar cell encapsulation with novel silicone
elastomer for building integrated PV,” in 8th World Conference on Photovoltaic Energy
Conversion, 2021, pp. 893–897.
[65] M. Halwachs et al., “Statistical evaluation of PV system performance and failure data
among different climate zones,” Renew. Energy, vol. 139, pp. 1040– 1060, Aug. 2019,
doi: 10.1016/j.renene.2019.02.135.
[66] M. Aghaei et al. , “Review of degradation and failure phenomena in photovoltaic
modules,” Renew. Sustain. Energy Rev., vol. 159, no. February, p. 112160, May 2022,
doi: 10.1016/j.rser.2022.112160.
[67] “DuPont global PV reliability 2019 Field analysis.” [Online]. Available:
https://www.dupont.com/news/20190618-dupont-issues-2019-pv-reliability-study.htm
[68] “DuPont global PV reliability 2020 Field analysis.” [Online]. Available:
https://www.dupont.com/news/20200512-2020-global-pv-reliability-report.html
[69] G. C. Eder et al., “Error analysis of aged modules with cracked polyamide backsheets,”
Sol. Energy Mater. Sol. Cells , vol. 203, no. August, p. 110194, 2019, doi:
10.1016/j.solmat.2019.110194.
[70] Y. Voronko et al. , “Repair options for PV modules with cracked backsheets,” Energy
Sci. Eng., vol. 9, no. 9, pp. 1583–1595, Sep. 2021, doi: 10.1002/ese3.936.
[71] C. Buerhop -Lutz, O. Stroyuk, T. Pickel, T. Winkler, J. Hauch, and I. M. Peters, “PV
modules and their backsheets -  A case study of a Multi -MW PV power station,” Sol.
Energy Mater. Sol. Cells , vol. 231, no. May, p. 111295, 2021, doi:
10.1016/j.solmat.2021.111295.
[72] C. Buerhop Lutz, L. Lüer, O. Stroyuk, J. Hauch, and I. M. Peters, “Dynamics of
backsheet-driven insulation issues,” Sol. Energy Mater. Sol. Cells, vol. 257, no. April, p.
112398, Aug. 2023, doi: 10.1016/j.solmat.2023.112398.
[73] C. Buerhop, O. Stroyuk, J. Zöcklein, T. Pickel, J. Hauch, and I. M. Peters, “Wet leakage

## Página 55

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
55
resistance development of modules with various backsheet types,” Prog. Photovoltaics
Res. Appl., vol. 30, no. 8, pp. 938–947, Aug. 2022, doi: 10.1002/pip.3481.
[74] M. Owen‐Bellini et al., “Advancing reliability assessments of photovoltaic modules and
materials using combined ‐accelerated stress testing,” Prog. Photovoltaics Res. Appl. ,
vol. 29, no. 1, pp. 64–82, Jan. 2021, doi: 10.1002/pip.3342.
[75] M. D. Kempe, T. Lockman, and J. Morse, “Development of Testing Methods to Predict
Cracking in Photovoltaic Backsheets,” Conf. Rec. IEEE Photovolt. Spec. Conf. , pp.
2411–2416, 2019, doi: 10.1109/PVSC40753.2019.8980818.
[76] T. T. Gernot Oreski, Ioannis Tsanakas, Arvid van der Heide, Gabriele Eder,
“Performance and Reliability of Second Life PV,” 2025. [Online]. Available: https://iea-
pvps.org/publications/?year_p=&task=67&order=DESC&keyword=&cpt=keytopics&ke
ytopic=
[77] J. Markert, S. Kotterer, D. E. Mansour, D. Philipp, and P. Gebhardt, “Advanced analysis
of backsheet failures from 26 power plants,” EPJ Photovoltaics, vol. 12, no. September,
pp. 6–10, 2021, doi: 10.1051/epjpv/2021006.
[78] P. Lechner et al. , “Analysis of Fielded PV -Modules with Backsheet Issues,” in
Proceedings of the 36th European Photovoltaic Solar Energy Conference and
Exhibition, Marseille, France, 2019, pp. 930–934.
[79] K.-A. Weiß, “Accelerated testing - combined stress vs. sequential stress testing methods
and inclusion of specific load situations,” 2025. [Online]. Available: https://iea -
pvps.org/publications/?year_p=&task=67&order=DESC&keyword=&cpt=keytopics&ke
ytopic=
[80] Y. Voronko, G. C. Eder, E. Reiser, M. Babin, and G. Oreski, “Development of Novel
Frontsheets With Protective Coatings to Increase the Durability and Reliability of Glass‐
Free Lightweight PV Modules,” Prog. Photovoltaics Res. Appl. , pp. 1823– 1823, Nov.
2024, doi: 10.1002/pip.3871.
[81] H. Hu, S. Chen, O. Fu, M. Demko, and K. R. Choudhury, “Transparent Tedlar®
Frontsheet for Lightweight PV Module Designs,” in 2023 IEEE 50th Photovoltaic
Specialists Conference (PVSC) , IEEE, Jun. 2023, pp. 1– 3. doi:
10.1109/PVSC48320.2023.10359631.
[82] G. Oreski et al. , “Investigation of the crack propensity of co- extruded polypropylene
backsheet films for photovoltaic modules,” Sol. Energy Mater. Sol. Cells , vol. 259, no.
March, p. 112438, 2023, doi: 10.1016/j.solmat.2023.112438.
[83] S. Uličná, A. Sinha, D. C. Miller, B. M. Habersberger, L. T. Schelhas, and M. Owen-
Bellini, “PV encapsulant formulations and stress test conditions influence dominant
degradation mechanisms,” Sol. Energy Mater. Sol. Cells, vol. 255, no. December 2022,
p. 112319, Jun. 2023, doi: 10.1016/j.solmat.2023.112319.
[84] C. Barretta, E. Helfer, A. E. Macher, and G. Oreski, “What Are PVDF-Based Backsheets
Made Of?,” in 2022 IEEE 49th Photovoltaics Specialists Conference (PVSC), IEEE, Jun.
2022, pp. 0633–0636. doi: 10.1109/PVSC48317.2022.9938844.
[85] S. Uličná et al. , “A study of degradation mechanisms in PVDF- based photovoltaic
backsheets,” Sci. Rep., vol. 12, no. 1, pp. 1–11, 2022, doi: 10.1038/s41598-022-18477-
1.
[86] S. L. Moffitt et al., “Microstructure changes during failure of PVDF- based photovoltaic
backsheets,” Prog. Photovoltaics Res. Appl. , vol. 31, no. 1, pp. 26– 35, 2023, doi:

## Página 56

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
56
10.1002/pip.3605.
[87] S. Smith et al., “Long-term durability of transparent backsheets for bifacial photovoltaics:
An in-depth degradation analysis,” Sol. Energy Mater. Sol. Cells , vol. 256, p. 112309,
Jul. 2023, doi: 10.1016/j.solmat.2023.112309.
[88] I. Bennett, E. Bende, M. J. A. A. Goris, and W. Eerenstein, “An Overview of
Developments in Foil -Based Back -Contact Modules,” in Conference Proceedings of
29th European Photovoltaic Solar Energy Conference and Exhibition, Amsterdam,
2014. doi: 10.4229/EUPVSEC20142014-1AP.1.3.
[89] Y. Voronko, G. Eder, M. Edler, G. Oreski, and W. Muehleisen, “Analysis of the triggers
for the yellowing of PV materials during artificial ageing,” in 9th European Weathering
Symposium Natural and Artificial Ageing of Polymers, Basel, 2019.
[90] C. Barretta, G. Oreski, S. Feldbacher, K. Resch-Fauster, and R. Pantani, “Comparison
of Degradation Behavior of Newly Developed Encapsulation Materials for Photovoltaic
Applications under Different Artificial Ageing Tests,” Polymers (Basel). , vol. 13, p. 271,
2021, doi: 10.3390/polym13020271.
[91] B. Adothu, P. Bhatt, S. Zele, J. Oderkerk, F. R. Costa, and S. Mallick, “Investigation of
newly developed thermoplastic polyolefin encapsulant principle properties for the c -Si
PV module application,” Mater. Chem. Phys., vol. 243, no. January, p. 122660, 2020,
doi: 10.1016/j.matchemphys.2020.122660.
[92] B. Lin, C. Zheng, Q. Zhu, and F. Xie, “A polyolefin encapsulant material designed for
photovoltaic modules: from perspectives of peel strength and transmittance,” J. Therm.
Anal. Calorim., vol. 140, no. 5, pp. 2259 –2265, Jun. 2020, doi: 10.1007/s10973 -019-
09006-w.
[93] J. H. Park and S. -H. Hwang, “A Polyolefin Elastomer Encapsulant Modified by an
Ethylene–Propylene–Diene Terpolymer for Photovoltaic Applications,” ACS Omega ,
Jan. 2024, doi: 10.1021/acsomega.3c07969.
[94] J. H. Park and S. H. Hwang, “Construction and Characterization of Polyolefin Elastomer
Blends with Chemically Modified Hydrocarbon Resin as a Photovoltaic Module
Encapsulant,” Polymers (Basel)., vol. 14, no. 21, 2022, doi: 10.3390/polym14214620.
[95] N. T. Dintcheva, E. Morici, and C. Colletti, “Encapsulant Materials and Their Adoption in
Photovoltaic Modules: A Brief Review,” Sustainability, vol. 15, no. 12, p. 9453, Jun.
2023, doi: 10.3390/su15129453.
[96] H. Hanifi et al., “Loss analysis and optimization of PV module components and design
to achieve higher energy yield and longer service life in desert regions,” Appl. Energy ,
vol. 280, no. September, p. 116028, Dec. 2020, doi: 10.1016/j.apenergy.2020.116028.
[97] K. Hara, Y. Chiba, and Y. Shirahige, “Durable polyolefin encapsulants in aged
photovoltaic modules,” J. Photochem. Photobiol. A Chem. , vol. 431, no. February, p.
114015, 2022, doi: 10.1016/j.jphotochem.2022.114015.
[98] B. Adothu, F. R. Costa, and S. Mallick, “Damp heat resilient thermoplastic polyolefin
encapsulant for photovoltaic module encapsulation,” Sol. Energy Mater. Sol. Cells, vol.
224, no. February, p. 111024, 2021, doi: 10.1016/j.solmat.2021.111024.
[99] G. Oreski et al. , “Polyethylene copolymers as solar cell encapsulants  : A critical
overview,” in Conference Proceedings of 40th European Photovoltaic Solar Energy
Conference and Exhibition, Lisbon, 2023, p. 3AV.1.35.
[100] Z. Yang et al., “Novel EPE co -extruded encapsulating films with UV down- conversion

## Página 57

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
57
power gain effect for highly efficient solar cells,” Sol. Energy Mater. Sol. Cells, vol. 257,
no. January, p. 112373, 2023, doi: 10.1016/j.solmat.2023.112373.
[101] M. Köntges, A. Morlier, G. Eder, E. Fleis, B. Kubicek, and J. Lin, “Review: Ultraviolet
Fluorescence as Assessment Tool for Photovoltaic Modules,” IEEE J. Photovoltaics ,
vol. 10, no. 2, pp. 616–633, 2020, doi: 10.1109/JPHOTOV.2019.2961781.
[102] G. Oreski et al. , “Motivation, benefits, and challenges for new photovoltaic material
&amp; module developments,” Prog. Energy , vol. 4, no. 3, p. 032003, Jul. 2022, doi:
10.1088/2516-1083/ac6f3f.
[103] A. Borja Block et al., “Colouring solutions for building integrated photovoltaic modules:
A review,” Energy Build. , vol. 314, no. April, p. 114253, 2024, doi:
10.1016/j.enbuild.2024.114253.
[104] A. J. Curran et al. , “Field studies of PERC and Al -BSF PV module performance loss
using power and I -V timeseries,” Front. Energy Res. , vol. 11, Jul. 2023, doi:
10.3389/fenrg.2023.1127775.
[105] R. Rüther, “Make PV modules as cheap as possible, but not cheaper,” PV Magazine
International. [Online]. Available: https://www.pv -magazine.com/2024/01/03/make-pv-
modules-as-cheap-as-possible-but-not-cheaper/
[106] M. Braga, G. X. A. Pinto, A. M. Pires, A. H. Zamboni, L. R. Nascimento, and R. Rüther,
“No Title,” Universidade Federal de Santa Catarina, Florianópolis -SC, Brazil,. [Online].
Available: https://scorecard.pvel.com/mechanical-stress-sequence/
[107] F. O. Santos, C. Louter, and J. R. Correia, “Exploring thin glass strength test
methodologies,” Challenging Glas. 6 Conf. Archit. Struct. Appl. Glas. CGC 2018 - Proc.,
no. May, 2018, doi: 10.7480/cgc.6.2192.
[108] C. Sillerud, D. Zirzow, and J. Crimmins, “Past , Current , and Future Issues in PV
Reliability Testing,” in Proc. 53nd European Photovoltaic Solar Energy Conference,
Seattle, WA, 2023.
[109] K. Thiele, S. Müller -Braun, and J. Schneider, “Evaluation methods for surface
compression stress measurements with unknown principle stress directions,” Glas.
Struct. Eng., vol. 7, no. 2, pp. 121–137, Aug. 2022, doi: 10.1007/s40940-022-00184-y.
[110] J. Markert, F. Ensslen, T. Rist, E. Job, I. Hädrich, and D. Philipp, “Mechanical Stability
of PV Modules,” in PV Symp., 2024, pp. 1–12.
[111] C. Kedir, “Solar Risk Assessment,” Report: kWh analytics. [Online]. Available:
https://www.kwhanalytics.com/solar-risk-assessment
[112] VDMA, “International Technology Roadmap for Photovoltaic (ITRPV) -  15th Edition,”
2023.
[113] T. G. Allen, J. Bullock, X. Yang, A. Javey, and S. De Wolf, “Passivating contacts for
crystalline silicon solar cells,” Nat. Energy, vol. 4, no. 11, pp. 914–928, Sep. 2019, doi:
10.1038/s41560-019-0463-6.
[114] C. Peike et al., “Origin of damp-heat induced cell degradation,” Sol. Energy Mater. Sol.
Cells, vol. 116, pp. 49–54, 2013, doi: 10.1016/j.solmat.2013.03.022.
[115] A. Kraft et al. , “Investigation of Acetic Acid Corrosion Impact on Printed Solar Cell
Contacts,” IEEE J. Photovoltaics , vol. 5, no. 3, pp. 736– 743, May 2015, doi:
10.1109/JPHOTOV.2015.2395146.
[116] M. D. Kempe, G. J. Jorgensen, K. M. Terwilliger, T. J. McMahon, C. E. Kennedy, and

## Página 58

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
58
T. T. Borek, “Acetic acid production and glass transition concerns with ethylene- vinyl
acetate used in photovoltaic devices,” Sol. Energy Mater. Sol. Cells , vol. 91, no. 4, pp.
315–329, 2007, doi: 10.1016/j.solmat.2006.10.009.
[117] E. A. Gaulding et al., “Differences in Printed Contacts Lead to Susceptibility of Silicon
Cells to Series Resistance Degradation,” IEEE J. Photovoltaics, vol. 12, no. 3, pp. 690–
695, 2022, doi: 10.1109/JPHOTOV.2022.3150727.
[118] M. Liggett et al. , “Characterization of Field Exposed Photovoltaic Modules Featuring
Signs of Contact Degradation,” in 2023 IEEE 50th Photovoltaic Specialists Conference
(PVSC), IEEE, Jun. 2023, pp. 1–3. doi: 10.1109/PVSC48320.2023.10360087.
[119] O. K. Segbefia, N. Akhtar, and T. O. Sætre, “Moisture induced degradation in field-aged
multicrystalline silicon photovoltaic modules,” Sol. Energy Mater. Sol. Cells , vol. 258,
no. March, p. 112407, Aug. 2023, doi: 10.1016/j.solmat.2023.112407.
[120] T. H. Kim, N. C. Park, and D. H. Kim, “The effect of moisture on the degradation
mechanism of multi-crystalline silicon photovoltaic module,” Microelectron. Reliab., vol.
53, no. 9–11, pp. 1823–1827, 2013, doi: 10.1016/j.microrel.2013.07.047.
[121] A. J. Curran et al. , “Degradation of PERC and Al -BSF Cells with UV Cutoff and White
Variations of EVA and POE Encapsulant,” Conf. Rec. IEEE Photovolt. Spec. Conf., pp.
1510–1516, 2021, doi: 10.1109/PVSC43889.2021.9519110.
[122] N. Iqbal et al. , “Characterization of front contact degradation in monocrystalline and
multicrystalline silicon photovoltaic modules following damp heat exposure,” Sol. Energy
Mater. Sol. Cells , vol. 235, no. February 2021, p. 111468, 2022, doi:
10.1016/j.solmat.2021.111468.
[123] D. B. Sulas -Kern, H. Moutinho, T. Erion -Lorico, and S. Johnston, “Near -Busbar
Degradation of Screen -Printed Metallization in Silicon Photovoltaic Modules,” Conf.
Rec. IEEE Photovolt. Spec. Conf. , vol. 2022- June, pp. 200 –203, 2022, doi:
10.1109/PVSC48317.2022.9938799.
[124] A. M. Jeffries, T. Nietzold, L. T. Schelhas, and M. I. Bertoni, “Corrosion of novel reactive
silver ink and commercial silver-based metallizations in diluted acetic acid,” Sol. Energy
Mater. Sol. Cells , vol. 223, no. July 2020, p. 110900, 2021, doi:
10.1016/j.solmat.2020.110900.
[125] N. Iqbal et al., “Impact of acetic acid exposure on metal contact degradation of different
crystalline silicon solar cell technologies,” Sol. Energy Mater. Sol. Cells , vol. 250, no.
August 2022, p. 112089, 2023, doi: 10.1016/j.solmat.2022.112089.
[126] C. Sen et al. , “Accelerated damp -heat testing at the cell -level of bifacial silicon HJT,
PERC and TOPCon solar cells using sodium chloride,” Sol. Energy Mater. Sol. Cells ,
vol. 262, no. September, p. 112554, 2023, doi: 10.1016/j.solmat.2023.112554.
[127] P. M. Sommeling, J. Liu, and J. M. Kroon, “Corrosion effects in bifacial crystalline silicon
PV modules; interactions between metallization and encapsulation,” Sol. Energy Mater.
Sol. Cells , vol. 256, no. October 2022, p. 112321, 2023, doi:
10.1016/j.solmat.2023.112321.
[128] C. Sen et al., “Buyer aware: Three new failure modes in TOPCon modules absent from
PERC technology,” Sol. Energy Mater. Sol. Cells, vol. 272, no. March, p. 112877, 2024,
doi: 10.1016/j.solmat.2024.112877.
[129] X. Wu et al., “Enhancing the reliability of TOPCon technology by laser-enhanced contact
firing,” Sol. Energy Mater. Sol. Cells , vol. 271, no. March, p. 112846, 2024, doi:

## Página 59

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
59
10.1016/j.solmat.2024.112846.
[130] O. Arriaga Arruti, A. Virtuani, and C. Ballif, “Long‐ term performance and reliability of
silicon heterojunction solar modules,” Prog. Photovoltaics Res. Appl., vol. 31, no. 7, pp.
664–677, Jul. 2023, doi: 10.1002/pip.3688.
[131] D. C. Jordan, S. R. Kurtz, K. VanSant, and J. Newmiller, “Compendium of photovoltaic
degradation rates,” Prog. Photovoltaics Res. Appl. , vol. 24, no. 7, pp. 978 –989, Jul.
2016, doi: 10.1002/pip.2744.
[132] D. C. Jordan et al. , “Silicon heterojunction system field performance,” IEEE J.
Photovoltaics, vol. 8, no. 1, pp. 177–182, 2018, doi: 10.1109/JPHOTOV.2017.2765680.
[133] N. Iqbal et al. , “Accelerate Cycles of Learning: Unencapsulated Silicon Photovoltaic
Cells to Environmental Stressors,” in 2022 IEEE 49th Photovoltaics Specialists
Conference (PVSC) , IEEE, Jun. 2022, pp. 0668– 0674. doi:
10.1109/PVSC48317.2022.9938492.
[134] O. Arriaga Arruti, L. Gnocchi, Q. Jeangros, C. Ballif, and A. Virtuani, “Potential‐induced
degradation in bifacial silicon heterojunction solar modules: Insights and mitigation
strategies,” Prog. Photovoltaics Res. Appl., vol. 32, no. 5, pp. 304–316, May 2024, doi:
10.1002/pip.3765.
[135] L. Gnocchi, O. A. Arruti, C. Ballif, and A. Virtuani, “A comprehensive physical model for
the sensitivity of silicon heterojunction photovoltaic modules to water ingress,” Cell
Reports Phys. Sci., vol. 5, no. 1, p. 101751, Jan. 2024, doi: 10.1016/j.xcrp.2023.101751.
[136] J. H. Wohlgemuth, P. Hacke, N. Bosco, D. C. Miller, M. D. Kempe, and S. R. Kurtz,
“Assessing the causes of encapsulant delamination in PV modules,” in 2016 IEEE 43rd
Photovoltaic Specialists Conference (PVSC) , IEEE, Jun. 2016, pp. 0248 –0254. doi:
10.1109/PVSC.2016.7749589.
[137] M. Taguchi, J. Irikawa, M. Iwata, H. Kannou, Y. Murakami, and S. Okamoto,
“Approaches to the long-term stability of silicon heterojunction modules,” in Proceedings
of 4th International Workshop on Silicon Heterojunction Solar Cells, 2021.
[138] C. Sen et al., “Four failure modes in silicon heterojunction glass -backsheet modules,”
Sol. Energy Mater. Sol. Cells , vol. 257, no. December 2022, p. 112358, 2023, doi:
10.1016/j.solmat.2023.112358.
[139] X. Wu et al., “Addressing sodium ion-related degradation in SHJ cells by the application
of nano-scale barrier layers,” Sol. Energy Mater. Sol. Cells , vol. 264, no. September
2023, p. 112604, Jan. 2024, doi: 10.1016/j.solmat.2023.112604.
[140] A. Sinha, J. Jaubert, and T. Karin, “UV-Induced Degradation Susceptibility of Industrial
N-Type Silicon High -Efficiency PV Mod -ules,” in IEEE 52nd Photovoltaic Specialist
Conference on IEEE 52nd Photovoltaic Specialist Conference, Seattle, WA, USA ,
Seattle: Seattle, 2024, p. Poster E3 -#108. [Online]. Available:
https://www.kiwa.com/49edc2/globalassets/usa/pvel/resorces/pvsc-2024-poster_final-
version_sinha.pdf
[141] P. Thome, Fabian T. Meßmer, S. Mack, E. Schnabel, W. Schindler, Florian Kwapil, and
C. M. Schubert, “UV-Induced Degradation of Industrial PERC, TOPCon, and HJT Solar
Cells - The Next Big Reliability Challenge?,” Sol. RRL, Press, 2024.
[142] A. Sinha et al. , “UV -induced degradation of high- efficiency silicon PV modules with
different cell architectures,” Prog. Photovoltaics Res. Appl. , vol. 31, no. 1, pp. 36 –51,
2023, doi: 10.1002/pip.3606.

## Página 60

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
60
[143] T. Kamioka, D. Takai, T. Tachibana, T. Kojima, and Y. Ohshita, “Plasma damage effect
on ultraviolet-induced degradation of PECVD SiNx:H passivation,” in 2015 IEEE 42nd
Photovoltaic Specialist Conference (PVSC) , IEEE, Jun. 2015, pp. 1– 3. doi:
10.1109/PVSC.2015.7356326.
[144] R. Witteck et al., “UV-induced degradation of PERC solar modules with UV-transparent
encapsulation materials,” Prog. Photovoltaics Res. Appl. , vol. 25, no. 6, 2017, doi:
10.1002/pip.2861.
[145] B. Veith-Wolf, R. Witteck, A. Morlier, H. Schulte -Huxel, M. R. Vogt, and J. Schmidt,
“Spectra-dependent stability of the passivation quality of Al2O3/c-Si interfaces,” IEEE J.
Photovoltaics, vol. 8, no. 1, pp. 96–102, 2018, doi: 10.1109/JPHOTOV.2017.2775147.
[146] D. C. Jordan et al., “Photovoltaic fleet degradation insights,” Prog. Photovoltaics Res.
Appl., vol. 30, no. 10, pp. 1166–1175, 2022, doi: 10.1002/pip.3566.
[147] S. W. Johnston et al. , “Degradation -related defect level in weathered silicon
heterojunction modules characterized by deep level transient spectroscopy,” Sol.
Energy Mater. Sol. Cells , vol. 262, no. September, p. 112527, 2023, doi:
10.1016/j.solmat.2023.112527.
[148] S. Bernardini and M. I. Bertoni, “Insights into the Degradation of Amorphous Silicon
Passivation Layer for Heterojunction Solar Cells,” Phys. Status Solidi Appl. Mater. Sci.,
vol. 216, no. 4, pp. 1–6, 2019, doi: 10.1002/pssa.201800705.
[149] S. Manzoor and M. Bertoni, “Degradation of Surface Recombination Velocity at a -Si/c-
Si interface under light and temperature,” Conf. Rec. IEEE Photovolt. Spec. Conf. , pp.
1286–1288, 2021, doi: 10.1109/PVSC43889.2021.9518982.
[150] H. Ye et al. , “Short Wavelength Photons Destroying Si –H Bonds and Its Influence on
High‐Efficiency Silicon Solar Cells and Modules,” Sol. RRL, vol. 7, no. 15, Aug. 2023,
doi: 10.1002/solr.202300334.
[151] M. M. Rasmussen, “Ultraviolet -Induced Degradationof PERC and TOPCon
Architectures: Design of a Rapid Screening Process and Investigation of Degradation
Signatures,” Case Western Reserve University, 2024. doi: http://orcid.org/0000 -0001-
5895-5051.
[152] “Best Research-Cell Efficiency Chart,” National Renewable Energy Laboratory. [Online].
Available: https://www.nrel.gov/pv/cell-efficiency.html
[153] A. Kojima, K. Teshima, Y. Shirai, and T. Miyasaka, “Organometal halide perovskites as
visible-light sensitizers for photovoltaic cells,” J. Am. Chem. Soc. , vol. 131, no. 17, pp.
6050–6051, 2009, doi: 10.1021/ja809598r.
[154] G. E. Eperon, S. D. Stranks, C. Menelaou, M. B. Johnston, L. M. Herz, and H. J. Snaith,
“Formamidinium lead trihalide: A broadly tunable perovskite for efficient planar
heterojunction solar cells,” Energy Environ. Sci., vol. 7, no. 3, pp. 982– 988, 2014, doi:
10.1039/c3ee43822h.
[155] S. Baumann et al. , “Stability and reliability of perovskite containing solar cells and
modules: degradation mechanisms and mitigation strategies,” Energy Environ. Sci., vol.
17, no. 20, pp. 7566–7599, 2024, doi: 10.1039/D4EE01898B.
[156] R. I. Dawood, A. J. Forty, and M. R. Tubbs, “The photodecomposition of lead iodide,”
Proc. Roy. Soc. A, vol. 284, pp. 272–288, 1964, doi: 10.1098/rspa.1965.0063.
[157] A. Donakowski et al., “Improving Photostability of Cesium-Doped Formamidinium Lead
Triiodide Perovskite,” ACS Energy Lett. , vol. 6, no. 2, pp. 574– 580, 2021, doi:

## Página 61

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
61
10.1021/acsenergylett.0c02339.
[158] B. Roose, K. Dey, Y. H. Chiang, R. H. Friend, and S. D. Stranks, “Critical Assessment
of the Use of Excess Lead Iodide in Lead Halide Perovskite Solar Cells,” J. Phys. Chem.
Lett., vol. 11, no. 16, pp. 6505–6512, 2020, doi: 10.1021/acs.jpclett.0c01820.
[159] G. Tumen-Ulzii et al., “Detrimental Effect of Unreacted PbI2 on the Long-Term Stability
of Perovskite Solar Cells,” Adv. Mater. , vol. 32, no. 16, p. 1905035, 2020, doi:
10.1002/adma.201905035.
[160] S. Macpherson et al., “Local nanoscale phase impurities are degradation sites in halide
perovskites,” Nature, vol. 607, no. 7918, pp. 294–300, 2022, doi: 10.1038/s41586-022-
04872-1.
[161] L. T. Schelhas et al. , “Insights into operational stability and processing of halide
perovskite active layers,” Energy Environ. Sci., vol. 12, no. 4, pp. 1341–1348, 2019, doi:
10.1039/c8ee03051k.
[162] Y. Chen et al. , “Strain engineering and epitaxial stabilization of halide perovskites,”
Nature, vol. 577, p. 209, 2020, doi: 10.1038/s41586-019-1868-x.
[163] A. Y. Alsalloum et al. , “22.8%-Efficient single-crystal mixed-cation inverted perovskite
solar cells with a near-optimal bandgap,” Energy Environ. Sci, vol. 14, pp. 2263–2268,
2021, doi: 10.1039/d0ee03839c.
[164] B. Philippe et al. , “Chemical Distribution of Multiple Cation (Rb+,Cs+,MA+, and FA+)
Perovskite Materials by Photoelectron Spectroscopy,” Chem. Mater, vol. 29, pp. 3589–
3596, 2017, doi: 10.1021/acs.chemmater.7b00126.
[165] G. Y. Kim, A. Senocrate, T. Y. Yang, G. Gregori, M. Grätzel, and J. Maier, “Large tunable
photoeffect on ion conduction in halide perovskites and implications for
photodecomposition,” Nat. Mater. , vol. 17, no. 5, pp. 445– 449, 2018, doi:
10.1038/s41563-018-0038-0.
[166] W. J. Yin, T. Shi, and Y. Yan, “Unusual defect physics in CH3NH3PbI3 perovskite solar
cell absorber,” Appl. Phys. Lett. , vol. 104, no. 6, p. 063903, 2014, doi:
10.1063/1.4864778.
[167] B. Chen, M. Yang, S. Priya, and K. Zhu, “Origin of J -V Hysteresis in Perovskite Solar
Cells,” J. Phys. Chem. Lett. , vol. 7, no. 5, pp. 905 –917, 2016, doi:
10.1021/acs.jpclett.6b00215.
[168] H. Lee et al. , “Direct experimental evidence of halide ionic migration under bias in
CH3NH3PbI3-xClx-based perovskite solar cells using GD-OES analysis,” ACS Energy
Lett., vol. 2, no. 4, pp. 943–949, 2017, doi: 10.1021/acsenergylett.7b00150.
[169] D. A. Jacobs et al. , “The two faces of capacitance: New interpretations for electrical
impedance measurements of perovskite solar cells and their relation to hysteresis,” J.
Appl. Phys., vol. 124, no. 22, p. 225702, 2018, doi: 10.1063/1.5063259.
[170] C. C. Boyd, R. Cheacharoen, T. Leijtens, and M. D. McGehee, “Understanding
Degradation Mechanisms and Improving Stability of Perovskite Photovoltaics,” Chem.
Rev., vol. 119, no. 5, pp. 3418–3451, 2019, doi: 10.1021/acs.chemrev.8b00336.
[171] S. P. Dunfield et al. , “From Defects to Degradation: A Mechanistic Understanding of
Degradation in Perovskite Solar Cell Devices and Modules,” Adv. Energy Mater. , vol.
10, no. 26, pp. 1–35, 2020, doi: 10.1002/aenm.201904054.
[172] Y. Zhong et al. , “Inhibition of Ion Migration for Highly Efficient and Stable Perovskite

## Página 62

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
62
Solar Cells,” Adv. Mater., vol. 35, p. 2302552, 2023, doi: 10.1002/adma.202302552.
[173] S. Tan et al., “Steric Impediment of Ion Migration Contributes to Improved Operational
Stability of Perovskite Solar Cells,” Adv. Mater. , vol. 32, p. 1906995, 2020, doi:
10.1002/adma.201906995.
[174] A. D. Jodlowski et al. , “Large guanidinium cation mixed with methylammonium in lead
iodide perovskites for 19% efficient solar cells,” Nat. Energy, vol. 2, pp. 972–979, 2017,
doi: 10.1038/s41560-017-0054-3.
[175] P. Liu et al. , “Lattice-Matching Structurally-Stable 1D@3D Perovskites toward Highly
Efficient and Stable Solar Cells,” Adv. Energy Mater. , vol. 10, p. 1903654, 2020, doi:
10.1002/aenm.201903654.
[176] Z. Huang et al. , “Suppressed Ion Migration in Reduced -Dimensional Perovskites
Improves Operating Stability,” ACS Energy Lett. , vol. 4, p. 1521−1527, 2019, doi:
10.1021/acsenergylett.9b00892.
[177] W. Fan et al. , “Grain Boundary Perfection Enabled by Pyridinic Nitrogen Doped
Graphdiyne in Hybrid Perovskite,” Adv. Funct. Mater. , vol. 31, p. 2104633, 2021, doi:
10.1002/adfm.202104633.
[178] J. Yang et al. , “High-Performance Perovskite Solar Cells with Excellent Humidity and
Thermo-Stability via Fluorinated Perylenediimide,” Adv. Energy Mater. , vol. 9, p.
1900198, 2019, doi: 10.1002/aenm.201900198.
[179] S. Bai et al. , “Planar perovskite solar cells with long -term stability using ionic liquid
additives,” Nature, vol. 571, p. 245, 2019, doi: 10.1038/s41586-019-1357-2.
[180] Y. Ma et al., “Suppressing Ion Migration across Perovskite Grain Boundaries by Polymer
Additives,” Adv. Funct. Mater. , vol. 31, p. 2006802, 2021, doi:
10.1002/adfm.202006802.
[181] H. Wang et al., “Potassium Salt Coordination Induced Ion Migration Inhibition and Defect
Passivation for High-Efficiency Perovskite Solar Cells,” J. Phys. Chem. Lett , vol. 13, p.
8573−8579, 2022, doi: 10.1021/acs.jpclett.2c02414.
[182] J. Cao et al. , “Interstitial Occupancy by Extrinsic Alkali Cations in Perovskites and Its
Impact on Ion Migration,” Adv. Mater , vol. 30, p. 1707350, 2018, doi:
10.1002/adma.201707350.
[183] Y. Yang et al., “A thermotropic liquid crystal enables efficient and stable perovskite solar
modules,” Nat. Energy, vol. 9, pp. 316–323, 2024, doi: 10.1038/s41560-023-01444-z.
[184] F. Cheng et al. , “85 °C/85% -Stable n- i-p Perovskite Photovoltaics with NiO x Hole
Transport Layers Promoted By Perovskite Quantum Dots,” Adv. Sci., vol. 9, p. 2201573,
2022, doi: 10.1002/advs.202201573.
[185] Q. Tu et al. , “Out- of-Plane Mechanical Properties of 2D Hybrid Organic -Inorganic
Perovskites by Nanoindentation,” ACS Appl. Mater. Interfaces , vol. 10, no. 26, pp.
22167–22173, 2018, doi: 10.1021/acsami.8b05138.
[186] S. Baumann, A. Raugewitz, F. Haase, T. Wietler, R. Peibst, and M. Köntges,
“Perovskite/silicon tandem solar cells with front side metallization applied prior to top
cell fabrication enabling high curing temperatures,” in 2023 IEEE 50th Photovoltaic
Specialists Conference (PVSC), 2023. doi: 10.1109/PVSC48320.2023.10359983.
[187] T. Leijtens, G. E. Eperon, S. Pathak, A. Abate, M. M. Lee, and H. J. Snaith, “Overcoming
ultraviolet light instability of sensitized TiO2 with meso-superstructured organometal tri-

## Página 63

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
63
halide perovskite solar cells,” Nat. Commun. , vol. 4, p. 2885, 2013, doi:
10.1038/ncomms3885.
[188] B. Roose et al. , “Mesoporous SnO2 electron selective contact enables UV -stable
perovskite solar cells,” Nano Energy , vol. 30, no. October, pp. 517– 522, 2016, doi:
10.1016/j.nanoen.2016.10.055.
[189] S. Zhang et al. , “Conjugated Self -Assembled Monolayer as Stable Hole -Selective
Contact for Inverted Perovskite Solar Cells,” ACS Mater. Au , vol. 4, pp. 1976– 1983,
2022, doi: 10.1021/acsmaterialslett.2c00799.
[190] P. Jiang, L. Hu, L. Sun, Z. Li, H. Han, and Y. Zhou, “On the interface reactions and
stability of nonfullerene organic solar cells,” Chem. Sci., vol. 13, no. 17, pp. 4714–4739,
2022, doi: 10.1039/d1sc07269b.
[191] A. Das Mahapatra and J. -W. Lee, “Metal oxide charge transporting layers for stable
high-performance perovskite solar cells,” Cryst EngComm, vol. 24, p. 7229, 2022, doi:
10.1039/d2ce00825d.
[192] B. Roose, Q. Wang, and A. Abate, “The Role of Charge Selective Contacts in Perovskite
Solar Cell Stability,” Adv. Energy Mater , vol. 9, p. 1803140, 2019, doi:
10.1002/aenm.201803140.
[193] I. Gueye et al. , “Analysis of Iodide Transport on Methyl Ammonium Lead Iodide
Perovskite Solar Cell Structure Through Operando Hard X -ray Photoelectron
Spectroscopy,” Chem. Mater, vol. 35, 2023, doi: 10.1021/acs.chemmater.2c03162.
[194] N. N. Udalova et al., “New Aspects of Copper Electrode Metamorphosis in Perovskite
Solar Cells,” J. Phys. Chem. C , vol. 2020, pp. 24601 –24607, 2020, doi:
10.1021/acs.jpcc.0c06608.
[195] T. Chen et al., “Efficient Perovskite Solar Cells with Titanium Cathode Interlayer,” Sol.
RRL, vol. 2, p. 1800167, 2018, doi: 10.1002/solr.201800167.
[196] M. Liu, Z. Chen, Y. Yang, H.-L. Yip, and Y. Cao, “Reduced open-circuit voltage loss for
highly efficient low-bandgap perovskite solar cells via suppression of silver diffusion,” J.
Mater. Chem. A, vol. 7, p. 17324, 2019, doi: 10.1039/c9ta04366g.
[197] H. Lee and C. Lee, “Analysis of Ion-Diffusion-Induced Interface Degradation in Inverted
Perovskite Solar Cells via Restoration of the Ag Electrode,” Adv. Energy Mater., vol. 8,
p. 1702197, 2018, doi: 10.1002/aenm.201702197.
[198] E. Bi et al., “Efficient Perovskite Solar Cell Modules with High Stability Enabled by Iodide
Diffusion Barriers,” Joule, vol. 3, no. 11, pp. 2748– 2760, Nov. 2019, doi:
10.1016/j.joule.2019.07.030.
[199] J. A. Christians et al. , “Tailored interfaces of unencapsulated perovskite solar cells for
>1,000 hour operational stability,” Nat. Energy , vol. 3, no. 1, pp. 68 –74, 2018, doi:
10.1038/s41560-017-0067-y.
[200] E. M. Sanehira et al. , “Influence of Electrode Interfaces on the Stability of Perovskite
Solar Cells: Reduced Degradation Using MoO x /Al for Hole Collection,” ACS Energy
Lett., vol. 1, pp. 38–45, 2016, doi: 10.1021/acsenergylett.6b00013.
[201] I. Jeon et al., “Carbon nanotubes to outperform metal electrodes in perovskite solar cells
via dopant engineering and hole- selectivity enhancement,” J. Mater. Chem. A , vol. 8,
pp. 11141–11147, 2020, doi: 10.1039/d0ta03692g.
[202] B. Nath, P. C. Ramamurthy, G. Hegde, and D. Roy Mahapatra, “Role of electrodes on

## Página 64

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
64
perovskite solar cells performance: A review,” ISSS J. Micro Smart Syst., vol. 11, no. 1,
pp. 61–79, 2022, doi: 10.1007/s41683-021-00089-y.
[203] H. Zhang, K. Song, L. Zhu, and Q. Meng, “Back -interface regulation for carbon-based
perovskite solar cells,” Carbon N. Y. , vol. 168, pp. 372– 391, Oct. 2020, doi:
10.1016/J.CARBON.2020.06.065.
[204] Y. J. Noh, J. G. Kim, S. S. Kim, H. K. Kim, and S. I. Na, “Efficient semi -transparent
perovskite solar cells with a novel indium zinc tin oxide top electrode grown by linear
facing target sputtering,” J. Power Sources , vol. 437, p. 226894, Oct. 2019, doi:
10.1016/J.JPOWSOUR.2019.226894.
[205] S. Yoon et al., “Highly Efficient and Reliable Semitransparent Perovskite Solar Cells via
Top Electrode Engineering,” Adv. Funct. Mater. , vol. 32, p. 2111760, 2022, doi:
10.1002/adfm.202111760.
[206] A. Rousse et al. , “Non-thermal melting in semiconductors measured at femtosecond
resolution,” Nature, vol. 410, no. 6824, pp. 65–67, 2001, doi: 10.1038/35065045.
[207] K. Sokolowski-Tinten et al., “Transient states of matter during short pulse laser ablation,”
Phys. Rev. Lett., vol. 81, no. 1, pp. 224–227, 1998, doi: 10.1103/PhysRevLett.81.224.
[208] F. Jamaatisomarin, R. Chen, S. Hosseini -Zavareh, and S. Lei, “Laser Scribing of
Photovoltaic Solar Thin Films: A Review,” J. Manuf. Mater. Process., vol. 7, no. 3, p. 94,
2023, doi: 10.3390/jmmp7030094.
[209] L. Bayer et al., “Morphology and topography of perovskite solar cell films ablated and
scribed with short and ultrashort laser pulses,” Appl. Surf. Sci. , vol. 416, pp. 112 –117,
2017, doi: 10.1016/j.apsusc.2017.04.058.
[210] C. Schultz et al., “Ablation mechanisms of nanosecond and picosecond laser scribing
for metal halide perovskite module interconnection –  An experimental and numerical
analysis,” Sol. Energy , vol. 198, no. January, pp. 410– 418, 2020, doi:
10.1016/j.solener.2020.01.074.
[211] F. U. Kosasih, L. Rakocevic, T. Aernouts, J. Poortmans, and C. Ducati, “Electron
Microscopy Characterization of P3 Lines and Laser Scribing- Induced Perovskite
Decomposition in Perovskite Solar Modules,” ACS Appl. Mater. Interfaces , vol. 11, no.
49, pp. 45646–45655, 2019, doi: 10.1021/acsami.9b15520.
[212] J. Zhao et al. , “Nonthermal laser ablation of high -efficiency semitransparent and
aesthetic perovskite solar cells,” Nanophotonics, vol. 11, no. 5, pp. 987–993, 2022, doi:
10.1515/nanoph-2021-0683.
[213] N. N. Udalova, A. S. Tutantsev, Q. Chen, A. Kraskov, E. A. Goodilin, and A. B. Tarasov,
“New Features of Photochemical Decomposition of Hybrid Lead Halide Perovskites by
Laser Irradiation,” ACS Appl. Mater. Interfaces, vol. 12, no. 11, pp. 12755–12762, 2020,
doi: 10.1021/acsami.9b21689.
[214] Y. Hu et al., “Stable Large-Area (10 × 10 cm2) Printable Mesoscopic Perovskite Module
Exceeding 10% Efficiency,” Sol. RRL , vol. 1, no. 2, p. 1600019, 2017, doi:
10.1002/solr.201600019.
[215] B. Q. Lin, C. P. Huang, K. Y. Tian, P. H. Lee, W. F. Su, and L. Xu, “Laser Patterning
Technology Based on Nanosecond Pulsed Laser for Manufacturing Bifacial Perovskite
Solar Modules,” Int. J. Precis. Eng. Manuf. - Green Technol., vol. 10, no. 1, pp. 123–
139, 2023, doi: 10.1007/s40684-022-00421-3.
[216] B. Chen et al. , “Bifacial all- perovskite tandem solar cells,” Sci. Adv. , vol. 8, no.

## Página 65

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
65
November, pp. 1–12, 2022, doi: 10.1126/sciadv.add0377.
[217] S. Hong et al. , “A series connection architecture for large- area organic photovoltaic
modules with a 7.5% module efficiency,” Nat. Commun. , vol. 7, pp. 3 –8, 2016, doi:
10.1038/ncomms10279.
[218] M. Dailey, Y. Li, and A. D. Printz, “Residual Film Stresses in Perovskite Solar Cells:
Origins, Effects, and Mitigation Strategies,” ACS Omega, vol. 6, p. 30214−30223, 2021,
doi: 10.1021/acsomega.1c04814.
[219] H. Wang et al. , “Interfacial Residual Stress Relaxation in Perovskite Solar Cells with
Improved Stability,” Adv. Mater , vol. 31, p. 904408, 2019, doi:
10.1002/adma.201904408.
[220] L. Duan and A. Uddin, “Defects and stability of perovskite solar cells: A critical analysis,”
Mater. Chem. Front., vol. 6, no. 4, pp. 400–417, 2022, doi: 10.1039/d1qm01250a.
[221] S. Mazumdar, Y. Zhao, and X. Zhang, “Stability of Perovskite Solar Cells: Degradation
Mechanisms and Remedies,” Front. Electron. , vol. 2, p. 712785, 2021, doi:
10.3389/felec.2021.712785.
[222] F. M. Rombach, S. A. Haque, and T. J. Macdonald, “Lessons learned from spiro-
OMeTAD and PTAA in perovskite solar cells,” Energy Environ. Sci , vol. 14, pp. 5161–
5190, 2021, doi: 10.1039/d1ee02095a.
[223] C.-T. Lin et al., “Passivation against oxygen and light induced degradation by the PCBM
electron transport layer in planar perovskite solar cells,” Sustain. Energy Fuels , vol. 2,
pp. 1686–1692, 2018, doi: 10.1039/c8se00095f.
[224] J. A. Mikroyannidis, A. N. Kabanakis, S. S. Sharma, and G. D. Sharma, “A Simple and
Effective Modifi cation of PCBM for Use as an Electron Acceptor in Efficient Bulk
Heterojunction Solar Cells,” Adv. Funct. Mater. , vol. 21, pp. 746 –755, 2011, doi:
10.1002/adfm.201001807.
[225] Z. Zhu et al., “Interaction of Organic Cation with Water Molecule in Perovskite MAPbI3:
From Dynamic Orientational Disorder to Hydrogen Bonding,” Chem. Mater., vol. 28, no.
20, pp. 7385–7393, 2016, doi: 10.1021/acs.chemmater.6b02883.
[226] L. Shi et al., “Accelerated Lifetime Testing of Organic−Inorganic Perovskite Solar Cells
Encapsulated by Polyisobutylene,” ACS Appl. Mater. Interfaces, vol. 9, p. 25073−25081,
2017, doi: 10.1021/acsami.7b07625.
[227] A. R. Bowring, L. Bertoluzzi, B. C. O’Regan, and M. D. McGehee, “Reverse Bias
Behavior of Halide Perovskite Solar Cells,” Adv. Energy Mater., vol. 8, no. 8, p. 1702365,
2018, doi: 10.1002/aenm.201702365.
[228] L. Bertoluzzi et al., “Incorporating Electrochemical Halide Oxidation into Drift -Diffusion
Models to Explain Performance Losses in Perovskite Solar Cells under Prolonged
Reverse Bias,” Adv. Energy Mater. , vol. 11, no. 10, p. 2002614, Mar. 2021, doi:
10.1002/aenm.202002614.
[229] R. A. Z. Razera et al., “Instability of p- i-n perovskite solar cells under reverse bias,” J.
Mater. Chem. A, vol. 8, no. 1, pp. 242–250, 2020, doi: 10.1039/c9ta12032g.
[230] S. Johnston et al. , “Thin -Film Module Reverse -Bias Breakdown Sites Identified by
Thermal Imaging,” in 2018 IEEE 7th World Conference on Photovoltaic Energy
Conversion, WCPEC 2018 - A Joint Conference of 45th IEEE PVSC, 28th PVSEC and
34th EU PVSEC, 2018, pp. 1897–1901. doi: 10.1109/PVSC.2018.8547766.

## Página 66

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
66
[231] D. Bogachuk et al. , “Perovskite Photovoltaic Devices with Carbon- Based Electrodes
Withstanding Reverse- Bias Voltages up to –9 V and Surpassing IEC 61215:2016
International Standard,” Sol. RRL , vol. 6, no. 3, p. 2100527, Mar. 2022, doi:
10.1002/solr.202100527.
[232] Z. Ni et al., “Evolution of defects during the degradation of metal halide perovskite solar
cells under reverse bias and illumination,” Nat. Energy , vol. 7, no. 1, pp. 65– 73, Dec.
2021, doi: 10.1038/s41560-021-00949-9.
[233] C. Jiang et al. , “Double Layer Composite Electrode Strategy for Efficient Perovskite
Solar Cells with Excellent Reverse-Bias Stability,” Nano-Micro Lett., vol. 15, no. 1, p. 12,
2023, doi: 10.1007/s40820-022-00985-4.
[234] F. Jiang et al., “Architecture Optimization Dramatically Improves Reverse Bias Stability
in Perovskite Solar Cells: A Role of Polymer Hole Transport Layers,” 2023, doi:
10.48550/arXiv.2308.08084.
[235] C. Peike, C. Peike, I. Hädrich, K. Weiß, I. Dürr, and F. Ise, “Overview of PV module
encapsulation materials,” Pvi, vol. 22, no. November 2015, pp. 85–92, 2013.
[236] R. Cheacharoen et al. , “Encapsulating perovskite solar cells to withstand damp heat
and thermal cycling,” Sustain. Energy Fuels , vol. 2, no. 11, pp. 2398– 2406, 2018, doi:
10.1039/c8se00250a.
[237] Y. Wang et al. , “Encapsulation and Stability Testing of Perovskite Solar Cells for Real
Life Applications,” ACS Mater. Au , vol. 2, pp. 215– 236, 2022, doi:
10.1021/acsmaterialsau.1c00045.
[238] F. Toniolo et al., “Efficient and reliable encapsulation for perovskite/silicon tandem solar
modules,” Nanoscale, vol. 15, no. 42, pp. 16984– 16991, 2023, doi:
10.1039/d2nr06873g.
[239] A. Virtuani, E. Annigoni, and C. Ballif, “One ‐ type ‐ fits ‐ all ‐ systems : Strategies for
preventing potential ‐  induced degradation in crystalline silicon solar photovoltaic
modules,” Prog Phptovolt Res Appl , vol. 27, no. May 2018, pp. 13 –21, 2019, doi:
10.1002/pip.3066.
[240] L. Nakka, W. Luo, A. G. Aberle, and F. Lin, “Study of Potential -Induced Degradation in
Glass-Encapsulated Perovskite Solar Cells under Different Stress Conditions,” Sol.
RRL, vol. 7, p. 2300100, 2023, doi: 10.1002/solr.202300100.
[241] L. Xu et al. , “Potential-induced degradation in perovskite/silicon tandem photovoltaic
modules,” Cell Reports Phys. Sci. , vol. 3, no. 9, p. 101026, Sep. 2022, doi:
10.1016/j.xcrp.2022.101026.
[242] J. Carolus et al. , “Potential -Induced Degradation and Recovery of Perovskite Solar
Cells,” Sol. RRL, vol. 3, no. 10, p. 1900226, 2019, doi: 10.1002/solr.201900226.
[243] M. A. Islam et al. , “Potential -Induced Performance Degradation (PID) Applied on a
Perovskite Solar Cell: Exploring Its Effect on Cell Performance Through Numerical
Simulation,” J. Electron. Mater. , vol. 52, pp. 3205– 3218, May 2023, doi:
10.1007/s11664-023-10284-2.
[244] Z. Purohit et al. , “Impact of Potential -Induced Degradation on Different Architecture -
Based Perovskite Solar Cells,” Sol. RRL , vol. 5, no. 9, p. 2100349, Sep. 2021, doi:
10.1002/solr.202100349.
[245] K. Brecl, M. Jošt, M. Bokalič, J. Ekar, J. Kovač, and M. Topič, “Are Perovskite Solar Cell
Potential-Induced Degradation Proof?,” Sol. RRL, vol. 6, no. 2, p. 2100815, Feb. 2022,

## Página 67

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
67
doi: 10.1002/solr.202100815.
[246] D. Zhang, D. Li, Y. Hu, A. Mei, and H. Han, “Degradation pathways in perovskite solar
cells and how to meet international standards,” Commun. Mater. , vol. 3, p. 58, 2022,
doi: 10.1038/s43246-022-00281-z.
[247] A. Mei et al., “Stabilizing Perovskite Solar Cells to IEC61215:2016 Standards with over
9,000-h Operational Tracking,” Joule, vol. 4, no. 12, pp. 2646– 2660, 2020, doi:
10.1016/j.joule.2020.09.010.
[248] L. Duan et al. , “Stability challenges for the commercialization of perovskite –silicon
tandem solar cells,” Nat. Rev. Mater. , vol. 8, no. 4, pp. 261– 281, 2023, doi:
10.1038/s41578-022-00521-1.
[249] Photovoltaic (PV) module safety qualification, IEC 61730-Series-2023, 3.0. VDE, 2023.

## Página 68

Task 13 Reliability and Performance of Photovoltaic Systems – Degradation and Failure Modes in New Photocoltaic Cell and Module Technologies
68

Insert a QR code
linking to the re-
port. Delete the
green frame af-
ter.
