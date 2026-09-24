# IEA-PVPS-T13-35-2026-REPORT-PV-BESS-2026

Fonte original: `IEA-PVPS-T13-35-2026-REPORT-PV-BESS-2026.pdf`

## Página 1

Task 13   Reliability and Performance of Photovoltaic Systems
PVPS
Report IEA-PVPS T13-35:2026
Assessing the Reliability
of Battery Systems in
Solar Power Plants in
Operation
2026

## Página 2

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organization for Ec onomic
Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with a belief that the future of energy
security and sustainability starts with global collaboration. The programme is made up of 6.000 experts across government, ac ademia, and
industry dedicated to advancing common research and the application of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCP’s within the IEA and was established in 1993. The mission
of the programme is to “enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone
in the transition to sustainable energy systems.” In order to  achieve this, the Programme’s participants have undertaken a variety of joint
research projects in PV power systems applications. The overall programme is headed by an Executive Committee, comprised of one dele-
gate from each country or organisation member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.
The 28 IEA PVPS participating countries are Australia, Austria, Belgium, Canada, China, Denmark, Finland, France, Germany, India, Israel,
Italy, Japan, Korea, Lithuania, Malaysia, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain, Sweden, Switzerland, Thailand,
Turkiye, the United Kingdom and the United States of America. The European Commission, Solar Power Europe and the Solar Energ y
Research Institute of Singapore are also members.
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
Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand, and the United States of America, and the Solar Energy
Research Institute of Singapore.

DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and publica-
tions of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual  member countries.
COPYRIGHT STATEMENT
This content may be freely used, copied and redistributed, provided appropriate credit is given (please refer to the ‘Suggest ed Citation’). The exception is that
some licensed images may not be copied, as specified in the individual image captions.
SUGGESTED CITATION
Stensrud Marstein, E., Messner, C. (2026). Stensrud Marstein, E., Köntges, M., Jahn, U.  (Eds.), Assessing the Reliability of Battery Systems in Solar Power
Plants in Operation (Report No. T13-35:2026). IEA PVPS Task 13. DOI: 10.69766/EIRM1927
COVER PICTURE
The cover picture shows the utility-scale PV + BESS power plant in Kenhardt, South Africa  (Source: Scatec).

## Página 3

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
5

INTERNATIONAL ENERGY AGENCY
PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

Assessing the
Reliability of Battery Systems
in Solar Power Plants in Operation

IEA PVPS
Task 13
Reliability and Performance
of Photovoltaic Systems

Report IEA-PVPS T13-35:2026
July 2026

ISBN: 978-1-923734-09-8
DOI: 10.69766/EIRM1927

## Página 4

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

AUTHORS
Main Authors

Erik Stensrud Marstein, IFE, Norway
Christian Messner, AIT, Austria
Patrik Ollas, RISE, Sweden
Jonathan Fagerström, IFE, Norway
Mengjie Li, UCF, USA
Dan-Eric Archer, Checkwatt, Sweden
 Roger H. French, CWRU, USA

Editors

Erik Stensrud Marstein, IFE, Norway
Marc Köntges, ISFH, Germany
Ulrike Jahn, Fraunhofer CSP, Germany

## Página 5

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
7
TABLE OF CONTENTS
Acknowledgements ................................ ................................ ................................ ................ 8
List of abbreviations ................................ ................................ ................................ ............... 9
Executive summary ................................ ................................ ................................ .............. 11
 INTRODUCTION................................ ................................ ................................ ........... 13
1.1 Motivation for this report ................................ ................................ ....................... 13
1.2 Structure of this report ................................ ................................ .......................... 14
 SOLAR POWER AND BATTERY ENERGY STORAGE SYSTEMS ..............................  15
2.1 Introduction ................................ ................................ ................................ .......... 15
2.2 Introduction to solar power and battery energy storage systems .......................... 15
2.3 Review of commonly used battery technologies ................................ ................... 20
2.4 Photovoltaic and battery energy storage system use cases ................................ . 26
2.5 Modelling the use case-dependence of battery degradation................................ . 30
 DETERMINATION OF PERFORMANCE INDICATORS ................................ ............... 33
3.1 Introduction ................................ ................................ ................................ .......... 33
3.2 Factory and site acceptance tests ................................ ................................ ........ 34
3.3 Performance analysis using operational data ................................ ....................... 35
3.4 Performance indicators related to specific use cases ................................ ........... 40
 SOLAR POWER AND BATTERY ENERGY STORAGE  SYSTEM
PERFORMANCE ................................ ................................ ................................ .......... 42
4.1 Introduction ................................ ................................ ................................ .......... 42
4.2 The efficiency guideline and the HTW Berlin storage inspection .......................... 42
4.3 Discussion ................................ ................................ ................................ ........... 46
 CASE STUDIES ................................ ................................ ................................ ............ 47
5.1 The Florida SunSmart Schools ................................ ................................ ............ 47
5.2 The RISE PV + BESS: self-consumption and self-sufficiency ..............................  49
5.3 Grid-supporting BESS and market operations ................................ ...................... 53
 CONCLUSIONS ................................ ................................ ................................ ............ 57
References ................................ ................................ ................................ .......................... 59

## Página 6

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

ACKNOWLEDGEMENTS
This report received valuable contributions from IEA-PVPS Task 13 members and other inter-
national experts. ESM and JF acknowledge financial support from the projects KSP HY-
DROSUN (P.N. 328640) and FME SOLAR (P.N. 350244) co-funded by the Research Council
of Norway and user partners. RHF and ML acknowledge support by the U.S. Department of
Energy’s Solar Energy Technologies Office under Agreement Number DE -EE0009347. PO
acknowledges support from the Swedish Energy Agency.
This report is supported by the German Federal Ministry for Economic Affairs and Climate
Action (BMWK) under contract no. 03EE1120B and 03EE1120C.

## Página 7

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
9
LIST OF ABBREVIATIONS
AC Alternating current
AC2BAT Battery charging from the grid / AC side
a-FRR Automatic frequency restoration reserves
AIT Austrian Institute of Technology
BAT2AC Battery discharging to the grid / AC side
BESS  Battery energy storage system
BMS Battery management system
BSW German Solar Association
BTM Behind the meter
BVES German Energy Storage Association
CC-CV Constant current – constant voltage
C&I Commercial and industrial
C-rate A measure of the rate at which a battery can be charged or discharged
DC Direct current
DoD Depth of discharge
DSO Distribution systems operator
EMS Energy management system
EoL End of life
EPC Engineering, procurement and construction
FAT Factory acceptance test
FCR Frequency containment reserves
FCR-D Frequency containment reserves down-regulation
FCR-U Frequency containment reserves up-regulation
FDD Fault detection and diagnostics
FFR Fast frequency reserves
FSEC Florida Solar Energy Center
FTM In front of the meter
HTW Berlin University of Applied Sciences
IEA  International Energy Agency
IEC International Electrotechnical Committee
IFE Institute for Energy Technology
LCO Lithium cobalt oxide technology

## Página 8

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

LFP Lithium iron phosphate technology
LMO Lithium manganese oxide technology
LTO Lithium titanium oxide technology
MARI Manually Activated Reserves Initiative
m-FRR Manual frequency restoration reserves
NaS Sodium sulphur battery
NMA Lithium nickel cobalt aluminium oxide technology
NMC Lithium nickel manganese cobalt oxide technology
O&M Operations and maintenance
PI  Performance indicator
PICASSO Platform for the International Coordination of Automated Frequency Restoration
and Stable System Operation
PoC Point of connection
PPA Power purchase agreement
PV  Photovoltaic
PV2AC Direct PV feed-in to grid
PV2BAT PV battery charging
RMIPPPP Risk Mitigation Independent Power Producer Procurement Programme
SAM System advisor model
SAT Site acceptance test
SC Self-consumption
SoC  State of charge
SoH  State of health
SPI System performance index
SS Self-sufficiency
T  Temperature
ToU Time of use
TSO Transmission systems operator
UCF University of Southern Florida
VFB Vanadium flow battery
VPP  Virtual power plant

## Página 9

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
11
EXECUTIVE SUMMARY
The number of photovoltaic (PV) power plants integrated with Battery Energy Storage Systems
(BESS), is increasing rapidly. Battery Energy Storage Systems are set up to play an important
role in an energy system increasingly reliant on intermittent power production and are already
widely used to support  profitable and reliable operations . To support optimal operation of a
rapidly growing fleet of BESS facilities, access to real-time information related to the ir state,
performance and reliability during operation is crucial.
This report is intended for the scientific community and for developers, installers, and operators
of BESS. It addresses the definition and determination of performance indicators for the relia-
bility and operational performance of PV + BESS.  This increasingly important topic for the
industry also represents a rapidly evolving field of science and technology. Battery operation
is, of course, not a new field. Standards and certificates that ensure component quality, per-
formance and reliability and define required testing and documentation are well-established.
Until the early 2020s, the main battery markets were linked to electric vehicles and electrical
appliances. As of 2026, a rapidly growing proportion of PV systems of all sizes are equipped
with BESS. The large variety in scale, technology, design, use case, and deployment environ-
ment of PV + BESS affects their performance and reliability.  To support development and
subsequent cost-effective operations of PV + BESS facilities, developers and operators need
access to precise predictive models and real-time state of health information of their facilities.
Moreover, the generation of more available performance and reliability data of PV + BESS in
operation will support customers, technology developers, and vendors in their activities.
A range of battery technologies exist in the market today, and there is also great variety in the
types of batteries that are integrated in PV systems. However, Lithium-ion battery technologies
have rapidly become the preferred choice due to their combination of electrical properties,
performance and cost. The largest market share of BESS in the PV industry is now held by
Lithium Iron Phosphate (LFP) batteries. The choice of both battery chemistry and design, as
well as the overall design  and selection of components and software  affects both the perfor-
mance and reliability of the complete BESS.
For the PV industry, the use of BESS to support operations targeting a range of highly different
use cases is an important feature. Common use cases include energy management, market
operations, resilience, system services and off-grid energy systems. The selected use case—
or combination of use cases—determines the duty cycles imposed on the BESS, resulting in
substantially different electrical operating conditions.  The operating physical environment of
BESS can also vary significantly. Battery ageing is influenced by variations in both electrical
and physical conditions. It is the sum of two distinct mechanisms: environment-dependent cal-
endar ageing and duty-cycle-dependent cyclic ageing, whose relative contributions depend on
the specific operating conditions. Therefore, both the placement and use of a BESS will affect
performance and reliability, including the BESS lifetime.
To support developers, installers and operators of larger BESS, factory acceptance tests and
site acceptance tests are important to ensure that the initial product performance corresponds
to expectations. Once the BESS is in operation, time series data of important parameters be-
come available. These can be used to determine important performance indicators of opera-
tional PV + BESS, including the BESS c apacity, power tolerance, internal resistance, round -
trip efficiency, response time and standby losses. These can be used to support optimal control
strategies of the BESS. They also give important information supporting operations and man-
agement and indicate which parts of a BESS should be inspected, repaired or replaced. In this

## Página 10

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

report, we outline methods applicable for determining the above-mentioned parameters from
data obtained from normal operation, as well as methods more closely aligned with standard
laboratory measurements based on the use of dedicated test cycles for characterization.
An increasing number of studies share findings from performance and reliability tests of fleets
of BESS. One very good example is the HTW Berlin storage inspections, which has a focus
on smaller PV + BESS in operation. Th e published data from these inspections illustrate a
large variation in the performance and reliability of BESS, and includes data related to both
battery and inverter operations. Results from this work is included in this report.
To illustrate the large variation in use cases, this report  also presents three case studies of
operational systems and experiences and results from their operation. The first of these is a
fleet of PV + BESS supporting emergency shelters , data from which is now available to the
broader scientific, educational and industrial community. The second is a PV + BESS installed
in a Swedish residential building targeting increased self-consumption and self-sufficiency. In
the third case study, operational experience from a fleet of distributed BESS in Sweden per-
forming system services is shared. In this report we discuss how t he performance of the two
last systems is impacted by the local climate and seasonality.
The main takeaways of this report are:
1. The performance, reliability and lifetime of PV + BESS depend on technology,  use-
case and environment. Battery chemistry and design, system topology, control strategy
and duty cycles jointly determine calendar and cyclic ageing. Value-stacked or chang-
ing use-cases complicate predictive degradation modelling and end-of-life estimation.

2. A technically robust assessment framework is proposed based on six performance in-
dicators: capacity, power tolerance, internal resistance, round-trip efficiency, response
time and standby losses. These can be derived via factory and site acceptance tests
and from operational time -series, aligned with emerging IEC/IEEE/DIN standards to
support state-of-health estimation, fault detection and ageing-aware operation.

3. Field results from residential inspections (HTW Berlin), resilience systems (SunSmart
Schools), building-scale PV + BESS (RISE) and Nordic virtual power plant operation
demonstrate large spreads in real-world efficiency, inverter losses, state-of-charge es-
timation and cell-balancing quality, as well as strong temperature and firmware effects.
This underscores the need for harmonised monitoring, high-quality open data and val-
idated ageing models to enable reliable, cost-optimal deployment of PV + BESS.

## Página 11

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
13
 INTRODUCTION
1.1 Motivation for this report
Rapidly declining costs have resulted in a massive deployment of solar  photovoltaic (PV)
power plants. At the time of writing, the power production capacity of PV power plants
worldwide is approaching ~3 TWp. In 23 countries, the share of PV in the electricity mix
today exceeds 10%, as measured by kWh production. In five of those, it exceeds 20% [1].
With the increasing penetration of PV comes an increase in the value of energy storage.
Integration of battery energy storage systems (BESS) in PV power plants of all sizes is
becoming increasingly widespread. In 2025, 104 GW/257 GWh of new BESS capacity was
added worldwide, bringing the cumulative global capacity to 267 GW/610 GWh [2]. BESS
contribute to solving many of the challenges imposed by the increase in PV penetration,
including price cannibalization, power quality, and grid capacity.
The cost of BESS has dropped dramatically in recent years, making such systems increas-
ingly affordable. Consequently, PV + BESS power plants of all sizes are attracting increas-
ing levels of investment [2]. These systems perform various critical services for which high
lifetime performance and reliability are crucial.
This report reviews methods for determining the performance and reliability of operational
PV + BESS power plants. This is a field of science and technology in rapid development.
There is already substantial experience in the industrial and scientific community related
to BESS performance and reliability in general, much of which has been establ ished in
large markets related to automotive applications and consumer electronics. However, the
duty cycles imposed on the BESS for the PV-specific use cases exhibit a large variety and
can differ substantially from those of other well-established applications.
Battery ageing is commonly divided into two additive components. The first, calendar age-
ing, is technology-specific and depends on the age of the system, as well as temperature
and the state of charge of the battery, as main stressors. This is, in principle, equal for all
BESS irrespective of the application and only indirectly related to the imposed duty cycles.
However, the second component, cyclic ageing, depends on the actual operation of the
battery. Since the duty cycles of PV-specific use cases can differ strongly from those ap-
plied in the more studied BESS applications, this can impact cyclic ageing.
While the field addressed by the report is in extremely rapid development, with multiple
national and international initiatives, projects, and activities, the recent rapid growth in the
field of PV + BESS means that limited history, data, and experience are  available. The
performance and reliability of PV + BESS will depend on the battery technology, the envi-
ronment in which the system is deployed, and the specific use case or set of services/func-
tions it supports. Both experience and data related to the lifetime performance and degra-
dation of PV + BESS operated under these con ditions are largely lacking in the available
literature. This report reviews this exciting and important field with the aim of  identifying
research gaps and related challenges. The report reviews the most important battery tech-
nologies, use cases, and performance and reliability metrics towards PV-specific applica-
tions. To illustrate the breadth of the field, the report also includes three case studies of
fielded PV + BESS deployed to support three specific use cases.

## Página 12

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

1.2 Structure of this report
In chapter 2, we introduce PV + BESS and review the most common battery technologies
and selected technological developments in the battery industry. Furthermore, we review
the different use cases of PV + BESS. These result in very different duty cycles and
stressor environments. Therefore, we also discuss predictive battery agein g models. In
chapter 3, we review performance indicators (PI) relevant to BESS. In addition to PIs de-
scribing the technical state of the BESS itself, we also discuss using case-specific PIs. The
main focus is on methods for their determination after deployment of the PV + BESS based
on operational data or dedicated test duty cycles. In chapter 4, we present selected results
of a study of the performance and reliability of operational PV + BESS. Chapter 5 presents
the three above-mentioned case studies performing specific use cases for PV + BESS.
The case studies illustrate concrete needs, opportunities and challenges associated with
operation, performance and reliability analysis on such systems. The case studies are:

A. PV + BESS targeting resilience
B. PV + BESS targeting self-consumption and self-sufficiency
C. A fleet of BESS (Virtual Power Plants (VPPs) performing ancillary services.

## Página 13

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
15
 SOLAR POWER AND BATTERY ENERGY STORAGE SYS-
TEMS
2.1 Introduction
In this chapter, we introduce PV + BESS, including the main BESS components and topologies
and the main relevant data available from a BESS with respect to performance and reliability
analysis. Thereafter, we review commonly used battery technologies in PV applications today,
emphasising lead-acid and lithium-ion batteries. We then present common use cases for PV
+ BESS and demonstrate how the associated fluctuations in the duty cycle affect the cyclic
ageing of the batteries. Finally, we introduce models that take use case-dependent cyclic age-
ing of batteries into account to enable predictive modelling of PV + BESS ageing.

2.2 Introduction to solar power and battery energy storage systems
2.2.1 Battery terminology
The ability of batteries to store chemical energy and convert it reliably and cost-effectively into
electrical energy has made them attractive for a wide range of applications . Although they
exhibit a large variety, a BESS is generally defined by a configuration hierarchy, which  is de-
scribed below.
At the upper level of the hierarchy, a  BESS typically includes several components in addition
to the battery itself, such as an inverter and different auxiliary systems including systems for
thermal management and fire suppression and alarms. The BESS operation is often controlled
by an energy management system (EMS). Below the BESS  level, we have multiple battery
racks and/or packs. The distinction and usage of the terms “racks” and “packs” depend on the
specific application and energy storage capacity of the system and are usually not very strict.
Further down the hierarchy , we have the battery modules, which  consist of a rigid physical
frame hosting multiple battery cells. To ensure optimal operation of the battery, a battery man-
agement system (BMS) that monitors and controls voltage, current and temperature to ensure
both safety and performance on module and cell levels is included. Battery cells are made from
a wide variety of materials. As a result, they exhibit a wide range of electrical and physical
properties, as will be explained later in this chapter.  It should be noted that the components
and software integrated into the various levels of the BESS hierarchy described here may be
manufactured and controlled by between one and at least four different companies. Depending
on the openness of different companies along the hierarchy, data will be more and less avail-
able across the different levels. Moreover, the operator of a PV + BESS system often adds a
new layer of intelligence and monitoring to deploy their operations and maintenance (O&M)
and optimization procedures. The integration, assembly and construction of a BESS including
all required hardware and software are important factors impacting both performance and re-
liability.
Performance indicators (PIs) related to BESS performance and reliability can be measured
and reported on all hierarchy levels. This report examines PI relating to the performance and
reliability of the battery itself and the entire BESS, as well as performance indicators relevant
to the overall performance of the PV system in conjunction with the BESS in relation to the
intended use cases.

## Página 14

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

2.2.2 Nominal battery specifications
The technical product specifications of battery cells are described in their corresponding data
sheets, which include information about nominal electrical properties, performance character-
izations, and safety certifications. Battery modules have similar specifications as cells, but at
rack and BESS-level, additional features are included, such as system-wide aspects including
temperature management, power conversion, grid interfacing, energy management, and en-
ergy storage capacity, reflecting the complexity and scale of larger systems.  A list of typical
items included in the nominal specifications of a battery cell is given in Table 1. An important
metric in this context is the battery state of charge (SoC), which is defined as the  battery ca-
pacity expressed as percentage of maximum (Table 2).

Table 1 : List of items typically included in the nominal specifications of a battery cell.
Parameter Description Unit
Standard discharge capacity Available capacity from 100% SoC down to the cut-off voltage Ah
C-rate (charging/discharging) The rate of which a battery can be charged/discharged -
Cut-off voltage The minimum voltage allowed by the battery V
Max charge voltage The voltage the battery is charged to at full capacity V
Max continuous  and/or pulse
charge current
Recommended and maximum charge currents A
Max continuous and/or pulse dis-
charge current
Recommended and maximum discharge currents A
Weight Weight of battery Kg
Dimensions Physical dimensions of battery m3
Operating temperature Recommended temperature range for battery operation oC
Storage temperature Temperature ranges linked to calendar life oC
Cycle life The number of discharge-charge cycles before which the bat-
tery fails a specific performance criterium
#cycles
Calendar life The time before which the battery fails a specific performance
criterium, often given for different storage temperatures
h
Self-discharge-rate A battery has a certain self-discharge rate when it is discon-
nected. It is related to the specific electrochemistry of the se-
lected battery technology and environmental conditions as
temperature.
e.g.
%/month

According to IEC terminology, “capacity” for cells and batteries is defined as the electric charge
that can be delivered under specified conditions and is typically expressed in ampere -hours
(Ah) (IEC 60050). For electrical energy storage systems, however, IEC 62933 explicitly distin-
guishes this from energy storage capacity, which is expressed in watt-hours (Wh or kWh) and
shall not be confused with charge -based capacity. This reflects the shift from a cell -oriented,
electrochemical description toward a system-level, energy-based characterization.

## Página 15

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
17
The C-rate is a measure of how rapidly a battery can be charged and/or discharged.  Histori-
cally, battery operation has been characterized using the ratio of current (Ampere) to capacity
(Ampere-hour’s). This representation originates from the electrochemical description of batter-
ies, where capacity is naturally defined in ampere-hours and the C-rate provides a normalized
measure of charge and discharge intensity. With the increasing deployment of battery energy
storage systems (BESS) at system level, this perspective has shifted toward an energy-based
representation. In this context, the power-to-energy (P/E) ratio, defined as the ratio of system
power (kW) to energy storage capacity (kWh), is commonly used. While both metrics share
the same dimensionality (h −1) and are mathematically related, the C -rate remains a cell - or
battery-level parameter, whereas the P/E ratio is primarily used to describe system -level de-
sign and application requirements.
The inverse of the P/E-rate indicates the number of hours a fully charged battery needs to
discharge at full power. This is an increasingly used parameter. A battery with a capacity of 1
MWh and a P/E rate of 1 can deliver 1 MW for 1 hour and is consequently referred to as a 1h
battery. Batteries with a P/E rate of e.g. 0.5 and 0.25 are similarly referred to as a 2h and 4h
batteries. The P/E rate is a key parameter that significantly influences a battery’s suitability for
applications requiring rapid charging or discharging , such as ancillary services and load -dis-
patch control.
In addition to the details in Table 1, information on reliability is provided, including tests and
certifications covering key stress factors such as behaviour under short-circuit conditions, me-
chanical shocks and vibrations, overcharging, and thermal shocks. Details regarding battery
performance at various operating temperatures are also frequently provided. In addition, there
is data available on a battery’s operating condition, as shown in Table 2. These parameters
form an important basis for determining the battery’s specific performance, reliability metrics
and remaining service life.

Table 2: Data related to the state of a battery under operation.
Parameter Description Unit
State of charge (SoC) Present battery capacity expressed as percentage of maximum %
Depth of discharge (DoD) Discharged battery capacity expressed as percentage of maximum (1-
SoC)
%
Terminal voltage The voltage between battery terminals when subjected to load V
Open-circuit voltage The voltage between battery terminals without load V
Internal resistance The internal resistance, often different for charging and discharging mΩ
Temperature Temperature of battery (measured) oC

2.2.3 Solar power and battery energy storage system topologies
Two typical PV+BESS topologies are described below. The first example is an AC-coupled PV
+ BESS, as shown in Figure 1Figure 1: Components of an AC-coupled PV + BESS. The overall
operation of the BESS is governed by an EMS. A BMS ensures optimal battery operation, often
at the module or cell level. In addition to the components shown, the BESS includes sensors
and application-specific auxiliary components, such as temperature control, fire suppression,
and alarms (Source: IFE). The different available measurement points at which performance-

## Página 16

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

and reliability-related data can be collected are emphasized. We will return to the importance
of selecting relevant measurement points later in this report when discussing performance and
reliability analysis.

Figure 1: Components of an AC-coupled PV + BESS. The overall operation of the BESS
is governed by an EMS. A BMS ensures optimal battery operation, often at the module
or cell level. In addition to the components shown, the BESS includes sensors and ap-
plication-specific auxiliary components, such as temperature control, fire suppression,
and alarms (Source: IFE).

The system shown in Figure 1consists of a battery and PV modules connected via separate
inverters. The EMS controls the overall operation of the PV + BES S. A BMS is included to
ensure optimal operation of the battery. Thereafter, the system is either connected directly to
the grid or to a local energy system at the point of connection (PoC). The system also includes
sensors that enable remote monitoring of environmental parameters, overall production, and
the condition of key components.
As shown in Figure 1, monitoring supporting the optimal operation, performance analysis, and
fault detection and diagnostics (FDD) can be performed both on the PV system (DC and AC
side of inverter), the BESS (DC and AC side of inverter), as well as at the interface between
the PV system and the BESS.
Figure 2 shows an example of a  DC-coupled PV + BESS. In th e topology shown, two DC
converters connect the PV system and the battery to a common DC bus, which is connected
to the AC side via the inverter. DC-coupled topologies can be simplified further: in many cases,
only one inverter, often referred to as a hybrid inverter, connects the battery and PV to the AC
side, reducing the number of components in the system.

## Página 17

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
19

Figure 2: Components of DC-coupled PV + BESS. In addition to the components of an
AC-coupled PV + BESS shown in Figure 1, this specific topology uses two DC/DC
converters to connect the PV modules and the battery to a common DC bus, which is
then connected to the AC side via the inverter (Source: IFE).

2.2.4 Data time series
The typical specifications of a battery in terms of performance and reliability are determined
using standardized tests. Available data time series  are a key source of information for as-
sessing any ageing-induced changes in e.g. capacity  and performance, often referred to as
the state of health (SoH), of a battery in the field . Where and how this assessment is carried
out within the hierarchy varies. Several commercially available BMS have built-in algorithms
for calculating SoH and supply relevant higher-level information in addition to the data men-
tioned above.
To support performance analytics, the time series should include at least timestamps, meas-
ured voltages, measured currents and the S oC. In addition, temperature measurements are
often available, taken either at ambient temperatures or at various points within the BESS. The
physical parameters that are typically  available as time series from a BESS are listed in
Table 3.

## Página 18

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Table 3: Relevant physical parameters available as data time series from a BESS.
Parameter Description Unit
Measured voltage The voltage between battery terminals under operation V
Measured current The current between battery terminals under operation A
SoC Battery state of charge, given as percentage of maximum charge %
Temperature Measured ambient and/or battery temperature oC

In addition to the system-level parameters, available time series can also include measured
currents, voltages, SoCs, and temperatures of the battery pack s, individual battery modules
and cells. As mentioned before, this depends strongly on the concrete suppliers throughout
the BESS hierarchy. Cell-level measurements add cost but improve the capabilities with re-
spect to more optimized operation with respect to performance and reliability and support data-
driven FDD. As the total BESS performance depends on the battery's output and that of the
inverter, current and voltage measurements on both sides of the inverter (AC and DC sides)
are also useful for calculating performance indicators.

2.3 Review of commonly used battery technologies
In this section, we provide an overview of the current state-of-the-art battery technologies com-
monly used in PV + BESS applications. We cover their basic operating principles, key charac-
teristics, their prevalence in PV systems, and prospects for future advancements. We discuss
the technologies of lead-acid, lithium-ion and flow battery technologies. As lithium-ion technol-
ogy currently completely dominates the market for BESS applications , this technology is de-
scribed in detail.

2.3.1 Lead-acid batteries
Lead-acid batteries operate by undergoing a sequence of reversible chemical reactions involv-
ing their primary constituents: lead dioxide (PbO2) plates, sponge lead (Pb) plates, and a sul-
furic acid (H 2SO4) electrolyte solution. While being charged, the lead dioxide at the positive
plate undergoes a reaction with sulfuric acid, resulting in the formation of lead sulphate
(PbSO4) and water. Simultaneously, the sponge lead at the negative plate also generates lead
sulphate and releases electrons. In this process, sulphuric acid is converted into water, thereby
storing electrical energy as chemical energy. During discharge, the chemical reactions are
reversed. The lead sulphate on both plates is converted back into lead dioxide and spongy
lead respectively. At the same time, the water in the electrolyte decomposes, producing sul-
phuric acid and releasing electrical energy.
The key characteristics of lead-acid batteries for BESS applications are shown in Table 4.

## Página 19

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
21
Table 4: Key characteristics of lead-acid batteries [3, 4].
Characteristic Status
Maturity and reliability Proven technology also for PV applications
Cost Low
Lifespan Short
Energy density Low
Efficiency Moderate
Additional comments High self-discharge, frequent maintenance needed

Lead-acid batteries have long been the most common type of batteries in PV + BESS, partic-
ularly in off-grid and standalone applications. Their low cost and reliability have been important
drivers. Today, such batteries have largely been replaced by lithium-ion batteries and are used
in less than 5% of BESS [2]. They remain an older technology that is still relevant in certain
cost-sensitive applications.

2.3.2 Lithium-ion batteries
Lithium-ion batteries have rapidly become the dominating battery technology for a range of
applications, including BESS. In 2025, more than 90% of all BESS were based on this tech-
nology [2]. The operation of Li-ion batteries is governed by the movement of Li-ions between
a cathode and anode. During the charging process, Li ions move from the cathode to the an-
ode, where they store energy by becoming embedded within the lattice structure of the anode
material. The anode is commonly composed of graphite, which effectively accommodates the
Li ions. During discharge, the Li ions return to the cathode  where they release the stored en-
ergy. This process is facilitated by an electrolyte solution that allows ions to flow while inhibiting
the direct flow of electrons, as well as by  a separator that prevents the cathode and anode
from encountering one another and causing a short circuit. Li thium-ion batteries are efficient
and, compared to alternative battery technologies, are characterized by  high energy density
and a long service life. Lithium-ion technology is now the most widely used technology for the
majority of PV + BESS.
Lithium-ion batteries are available in various types, each distinguished by its specific cathode
material, which has a significant impact on the battery's performance, reliability and cost. The
cathode materials include lithium-iron phosphate (LiFePO4), lithium-cobalt-oxide (LiCoO2), lith-
ium-manganese oxide/spinel (LiMn2O4), lithium-nickel-manganese-cobalt oxide (LiNiMn-
CoO2), lithium-titanate (Li 2TiO3), and lithium-nickel-cobalt-aluminum oxide (LiNiCoAlO2),
known as LFP, LCO, LMO, NMC, LTO and NCA. The two cathode materials most used today
are NMC and LFP, which also serve as terms for the two corresponding lithium-ion technolo-
gies.
NMC batteries, which are known for their high energy density and performance, are a good
choice for applications where weight and space are key considerations. A prime example of
this is their use in electric vehicles. NMC batteries offer a good balance between energy stor-
age capacity , performance and lifespan. LFP batteries exhibit enhanced thermal stability.
While such batteries also exhibit  a lower energy density than NMC batteries, they are more
durable and exhibit a longer lifespan and improved tolerance to high temperatures [2]. Conse-

## Página 20

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

quently, they are well-suited for larger systems such as stationary energy storage in PV instal-
lations and industrial applications. By 2025, they dominated the BESS market with a market
share of over 85% [2]. The choice between NMC and LFP generally depends on requirements
regarding energy density, safety, durability and cost.
Lithium-ion battery cells typically come in three main shapes, known as form factors: cylindri-
cal, prismatic or pouch. Cylindrical cells are frequently used in consumer electronics and cer-
tain automotive applications due to their robustness and straightfor ward manufacturing pro-
cess. Some argue that cylindrical cells offer a safety advantage, as they generally have a lower
capacity than pouch and prismatic cells, meaning that a potentially faulty cell does not release
large amounts of energy.  Prismatic cells, housed in rigid plastic or aluminum, provide a con-
densed and efficient design, rendering them appropriate for applications where limited space
and weight are crucial. Pouch cells, featuring pliable and lightweight packaging, are used in
portable electronic devices and electric vehicles due to their versatility in accommodating dif-
ferent forms and dimensions, hence optimizing the utilization of space. LFP batteries are fre-
quently used as larger prismatic cells and pouch cells for stationary energy storage and indus-
trial applications where service life and reliability are more important than energy density. Gen-
erally, the choice of physical size and shape for both NMC and LFP batteries is determined by
the specific combination of energy density, mechanical stability, thermal management and
space constraints of the respective application.  The key characteristics of Lithium-ion batteries
for BESS applications are shown in Table 5.

Table 5: Key characteristics of Lithium-ion batteries [2,4].
Characteristic Status
Maturity and reliability Proven technology also for PV applications
Cost Increasingly low
Lifespan Long
Energy density High
Efficiency High
Additional comments Low self-discharge rate

Like the other lithium-ion technologies listed above, LCO batteries are characterised by high
energy density and are used in portable electronic devices such as smartphones and laptops.
NCA batteries are similar to NMC batteries but have a slightly higher energy density and are
used in electric vehicles.
LMO batteries exhibit excellent thermal stability and superior power output  and are therefore
commonly employed in power tools and hybrid automobiles. LTO batteries show rapid charg-
ing capability, excellent durability over multiple charge cycles and are suitable for applications
requiring quick charging.
The volume of knowledge regarding failures and safety incidents involving lithium-ion batteries
is growing. Although such batteries generally meet specifications, incidents are inevitable. Les-
sons have been learnt from past incidents, leading to improvements in the design, manufac-
ture, construction, integration and operation of lithium -ion BESS, which has resulted in a de-
cline in the number of serious incidents per unit of installed capacity in recent years [2,5]. It is

## Página 21

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
23
interesting to note that the control of the BESS, as well as the balance of system components,
are both responsible for a higher number of such incidents than the battery cells or modules
themselves [5]. Also, most of the observed incidents happen within the first two years of oper-
ation [5]. Since a BESS is often a highly complex system based on components from different
vendors, functional testing of the full BESS integrated into its operational environment is desir-
able. Serious incidents can have large consequences with respect to safety and profitability .
Consequently, continuous monitoring and real-time, data-driven performance analysis are also
desirable, as they provide a basis for operation and maintenance and enable deviations from
normal operation to be detected at an early stage. These aspects are covered in chapter 3.
The challenge associated with precise SoC determination for LFP batteries needs to be ad-
dressed. If the estimated SoC values deviate substantially from the actual SoC, this can lead
to both financial losses due to suboptimal operation and to operation of the BESS outside of
the desired SoC range, which reduces the performance and increases the likelihood of failure.
For LFP batteries, the relationship between the open circuit voltage and the SoC exhibits a flat
plateau across which exact determination of the SoC is more challenging. There is increased
risk of internal fluctuations in the SoC due to the large number of LFP battery cells that make
up the BESS. This requires what is known as cell balancing. As part of this process, the BESS
– and therefore all the battery cells it contains – is typically charged to a SoC of 100%. During
balancing, the BESS is typically removed from normal operation. Today, imperfect cell balanc-
ing routines can lead to substantial capacity reductions of up to 5 % – 10%. The need for bal-
ancing varies depending on the product, which can have significant economic implications.

2.3.3 Flow batteries
Flow batteries operate by utilizing the redox reaction between two electrolytes. These electro-
lytes are contained in separate tanks and pumped through a cell in which the reaction takes
place. A membrane is used to separate the two electrolytes, enabling the transfer of ions while
preventing their mixture. During the charging process, oxidation occurs at the positive elec-
trode, causing the release of electrons, while reduction takes place at the negative electrode,
resulting in the acceptance of electrons. During the discharge phase, the oxidation -reduction
reaction is reversed. The oxidized electrolyte is reduced at the negative electrode, whil st the
reduced electrolyte is oxidized at the positive electrode, resulting in a transfer of electrons.
There is substantial flexibility in the design of a flow battery. The transport of electrolytes within
the cell is regulated by pumps, whilst the energy storage capacity can be increased by increas-
ing the volume of electrolyte in the tanks. An increase in power output can be achieved by
altering the cell dimensions or by arranging the cells in a series connection. The key charac-
teristics of flow batteries for BESS applications are listed in Table 6 [4,6].

## Página 22

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Table 6: Key characteristics of flow batteries.
Characteristic Status
Maturity and reliability Less experience with use
Cost Increasingly low
Lifespan Long
Energy density Low
Efficiency Low

Flow batteries are becoming more common in BESS systems, particularly for long duration
storage purposes, but their market share remains below 2% [2]. Flow batteries are well suited
for this purpose since they can be easily adjusted in size, exhibit a long lifespan, and allow for
separate control of power- and energy storage capacity. Vanadium flow battery (VFB) technol-
ogies have been utilized in numerous demonstration projects at the MW and larger scales. The
successful implementation of these projects confirms the reliability and durability of VFB en-
ergy storage systems. VFB energy storage technologies are in the early stages of commer-
cialization, with emerging companies around the world building up their capacity [2,6].

2.3.4 Technology comparison
When comparing storage technologies for BESS applications, investment cost, lifetime, relia-
bility and O&M costs are important. Flexibility and performance are also important, especially
the ability to provide high performance in the relevant use cases. While single use cases facil-
itate such optimization, value stacking of different use cases adds complexity. The same BESS
can be required to supply power at low C-rates during, e.g., time-shifting operations and sim-
ultaneously have the capability for high C-rates required for ancillary services.
Table 7 summarizes the key characteristics of the battery technologies discussed above. It is
clear why lithium-ion batteries are popular : both the number of life cycles and the efficiency
are high. Moreover, systems using lithium-ion batteries are generally the most cost -effective
today. It is expected that this situation will not change in the coming years. Redox flow batteries
could have good growth prospects for long-term storage [7].

## Página 23

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
25
Table 7: A comparison of selected battery technologies adapted from [4].
 Lead-acid Lithium-ion VRFB
Cell voltage (V) 2.1 3.7 – 4 1.4 – 1.6
Specific energy (Wh/kg) 30 – 50 100 – 200 10 – 30
Specific power (W/kg) 75 – 300 250 – 340 80 – 150
Life cycle (#) 500 – 2000 >5000 >8000
Efficiency (%) 75 – 90 90 – 95 70 – 85
Temperature range (oC) -20 to +60 -30 to +40 -

2.3.5 Other battery technologies
The above-mentioned battery technologies are still being developed, improved and tailored
towards specific markets and applications. In parallel, emerging technologies are also reaching
a higher degree of commercialization.
Even though lithium-ion technology is relatively mature, there are still numerous opportunities
for technical and chemical improvements that can be exploited to enhance its performance.
Emphasis going forward is placed on the development of both cathode and anode, and elec-
trolytes [8]. One of the most significant developments is the replacement of the graphite anode
with silicon or silicon oxide to achieve a higher energy density. From a systems engineering
perspective, cost reductions can also be achieved by shortening installation times, as complete
storage systems are prefabricated at the factory.
Sodium-ion (Na-ion) batteries have made significant progress over the last decade and are
currently the subject of substantial investment. It is expected that, with further development in
terms of power density and reliability, battery cells based on sodium-ion technology will catch
up with lithium-ion cells. Similarities in the manufacturing processes of lithium-ion and sodium-
ion facilitate upscaling. Sodium-cells are also attractive due to the abundance and relative
affordability of relevant sodium feedstock materials. The drawbacks of Na -ion technologies
compared to Li -ion technologies i nclude their anticipated lower specific energy and energy
density and remaining uncertainties related to reliability and safety [2,9].
Solar redox flow batteries are being developed as a promising technology for addressing the
challenges of PV power production intermittency. Simultaneously, to attain widespread adop-
tion in industry, novel chemical compositions utilizing cost -effective and abundant elements
have been employed to enhance both longevity and energy storage capacity. Although there
has been significant progress in the state-of-the-art, the solar redox flow battery technology is
still in the early stages of research and development. Developments are currently focused on
addressing various limitations associated with limited capacity, insufficient photovoltage, and
the need for efficient and stable materials.
Sodium-sulphur (NaS) batteries could also become increasingly widespread. These batteries
offer considerable potential for applications in grid energy storage and represent a viable al-
ternative to conventional lithium-ion batteries. When it comes to sodium-ion batteries, the af-
fordability and wide availability of the materials used are key factors. Another attractive feature
is the ability to achieve excellent electrochemical performance without having to rely on ex-
pensive rare-earth elements.  Nevertheless, there are significant barriers that impede the scal-
ing of manufacturing today, including the composition of the electrolyte, the performance of the

## Página 24

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

anode, the stability of the electrode-electrolyte interface, and the ability to recycle the materials
in a sustainable manner. Considerable additional resources would be required to invest in ap-
plied research [10].

2.4 Photovoltaic and battery energy storage system use cases
2.4.1 Introduction
The following section outlines key use cases for PV + BESS. The terminology and grouping of
use cases vary depending on the perspective, source and region [11]. Here, we adopt an op-
erator-specific perspective for PV + BESS. We discuss three different categorisations:
• Behind-the-meter (BTM) and in-front-of-the-meter (FTM) applications
• Categorization of use cases based on temporal properties
• Categorization of use cases based on application.

2.4.2 Behind the meter and in front of the meter applications
Generally, the use cases for PV + BESS can be divided into two groups. The first group com-
prises so-called ‘behind-the-meter’ (BTM) services, which aim to minimise operating costs and
optimise resource utilisation by optimising energy management, using system concepts that
give consumers or prosumers control over their electr icity consumption and sales. An added
benefit is a reduction of grid impacts associated with increased electrification. In relation to the
PV + BESS topologies previously shown in Figures 1 and 2, the meter is located at the point
of connection (PoC). In addition to the components shown, other means of energy production,
conversion, charging and flexible loads can be included in BTM systems. The overall control
is performed by the EMS.
The other main group of applications comprises the so-called “in front of the meter” (FTM)
services, which aim to maximise revenue or strengthen the resilience of the energy system by,
for example, providing grid services and/or engaging in energy trading and/or participating in
energy communities and flexibility mechanisms beyond the PoC. FTM services can be offered
by single PV + BESS power plants  or by co-operated PV + BESS power plants  as Virtual
Power Plants (VPPs).
2.4.3 Classification of use cases based on temporal properties
Categorization of use cases according to their temporal properties is the approach followed by
the International Electrotechnical Committee (IEC). In the standard IEC 62933-2-1:2018 [12],
the relevant use cases are divided into three classes:
• Class A: Short duration applications. These are applications that require the BESS to
input/output the required power over a duty cycle for a short period of time (e.g. <1h).
Example applications are frequency and voltage regulation, as well as smoothing.
• Class B: Long duration applications. These are applications that require the BESS to
input/output the required power over a duty cycle for a long period of time (e.g. >1h).
Example applications are peak shaving and peak shifting applications.
• Class C: The BESS is used to supply power in emergency cases, without relying on
external power sources. An example application is back-up power.

## Página 25

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
27
2.4.4 Classification of use cases based on application
Classification of use cases based on application is a commonly used approach. One suggested
classification of use cases of PV + BESS according to their application is shown in Table 8. It
is worth mentioning that the temporal properties of the applied duty cycles overlap for several
of the discussed use cases.
The first group applies BTM operations to support energy management with the aim of improv-
ing performance and/or i ncreasing the profitability of the PV power plants  in which they are
integrated by time shifting production and/or load. This is sometimes also referred to as time
of use (ToU) management. This includes reducing energy consumption and/or targeting en-
ergy sales to peak hours, as well as increasing energy consumption and/or reducing energy
sales in off-peak hours. Self-consumption, where batteries are used to better align the elec-
tricity generated with local demand, is considered, as is the use of BESS to reduce feed -in
restrictions and losses caused by power curtailment . Although motivated by the end user
needs, this type of time shifting also facilitates grid integration and enables connection of larger
production capacities or loads within existing grid capacity limits.
The second group of use cases focuses on the deployment of the BESS, with the primary
objective being to maximise profitability through market operations. These include spot market
transactions such as energy arbitrage, whereby electricity is stored when prices are low and
then sold when demand and prices are higher . Another example is enabling the supply of
(power) capacity for prolonged periods, a strategy that enables revenues in capacity markets.
Instead of supplying kWh to a spot market, these PV power plants can operate under , e.g.,
power purchase agreements (PPAs) requiring delivery of firm power (W) for specific periods.
This is sometimes also referred to as capacity firming. In this group, we also add the use of
BESS to reduce imbalance fees associated with uncertainties in day-ahead bidding and intra-
day bidding in energy markets.
A third group of use cases addresses the resilience of the power system by reducing the impact
and/or duration of disruptive events and/or supporting the ability of the power system to absorb,
adapt to and/or rapidly recover from such events. Relevant applications for PV + BESS include
emergency power supply, off-grid operation and black-start capabilities for residential, indus-
trial and public users, as well as for infrastructure.
A fourth group of use cases focuses on increasing profitability or facilitating grid connection of
the PV + BESS by providing grid services. Time shifting to reduce clipping and/or curtailment
losses caused by excess production towards, e.g., the local grid capacity, is described above.
Here, we include capacity smoothing and ramp rate control which facilitate grid operation and
planning, as well as the  provision of ancillary services , i.e. services that ensure that the fre-
quency and voltage of the grid are maintained within predefined limits. This group also includes
phase balancing. Such services are divided into various sub-groups depending on the required
response time and are described in more detail in the following subsection. This group may
also include the use of BESS to defer investment in the electricity grid, substations, and other
electrical infrastructure.
A fifth group  comprises all off-grid PV + BESS applications, covering a very wide range of
applications.

## Página 26

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Table 8: Functional classification of PV + BESS use cases.
 Name of use case Function Typical duty cycle
Energy management
Peak shaving and
time shifting
Avoid/reduce clipping losses
Avoid/reduce curtailment losses
Increase utilization of infrastructure
Reduce energy costs of operation
Daily/few deep cycles
Self-consumption
and self-sufficiency
Maximize share of self-consumed PV
power Daily/few deep cycles
Market operations
Spot market Energy arbitrage Frequent cycles of vary-
ing depth
Capacity market
Profitability based on ability to supply
firm power (W) in accordance with con-
tract (PPA)
Daily/few deep cycles
with frequent smaller cor-
rections
Day ahead and intra-
day bidding
Reduction of production forecast un-
certainty
Reduction/avoidance of imbalance fee
Variable
Resilience
End user energy
resilience
Energy resilience for end users
Power back-up
Black start capabilities
Few deep cycles
Grid services Capacity firming and
smoothing
Capacity firming
Smoothing
Ramp rate control
Frequent shallow cycles
(firming, smoothing), few
deeper cycles (ramp rate
control)
Ancillary services Provision of frequency reserves
Provision of voltage support
Frequent fast and poten-
tially deep cycles
Off-grid
Off-grid PV and ap-
pliances
Off-grid PV systems
PV appliances Large variation

2.4.5 Ancillary services
Ancillary services are an important source of profitability for BESS systems, and this is also
the case for PV + BESS in many markets. This broad term includes a wide range of services.
Below, we describe a sample portfolio of ancillary services based on existing markets  in the
European Union (EU) [12,13]. Similar services also exist in other regions, but the terminology
and definitions differ. In this section, we refer to ancillary services using standard EU terminol-
ogy. Special balancing markets have been established here to ensure the availability of re-
serves for maintaining the grid frequency, even when the energy system is faced with unfore-
seen disturbances, outages or forecasting errors.  The available balancing products differ  in

## Página 27

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
29
terms of the required activation time, activation method, required duration, and their renumer-
ation, which may influence the selection of BESS for this purpose.
The overall terms defining the requirements, rules and re muneration for participating in the
market for ancillary services are set by  the transmission system operator (TSO), who is re-
sponsible for transmission of electricity in high voltage lines in a geographical area, as well as
for the reserves for maintaining nominal frequency in the grid. These reserves are typically
categorised as primary, secondary , and tertiary reserves. Primary reserves have a very fast
requirement on activation speed; secondary and tertiary reserves are consecutively slower.
Firstly, there are  the fast frequency reserves (FFR), which are activated rapidly to prevent
frequency deviations in the power system caused by major disruptions. In the Nordic balancing
markets, this fastest reserve has a required activation time of 1±0.3 s. FFR is set up to imme-
diately support the power system in returning to the required frequency span. Market partici-
pants are remunerated for making the capacity available for the operation of FFR, regardless
of whether that capacity is actually used or not.
Thereafter, we have the frequency containment reserves (FCR), which are set up to balance
the frequency during imbalances between production and use in the power system. These are
also known as primary reserves. This group includes two products: FCR-N (normal operation)
and FCR-D (disturbed operation), which differ with respect to the situations in which they are
activated. These primary reserves remain activated until the secondary and tertiary reserves
are activated and restore balance to the energy system.
Then there are the automatic frequency restoration reserves (a-FRR), i.e. products that must
be offered in a specific bidding area before the bidding closes at 07:30 CET, one day prior to
activation. These reserves are automatically activated by the TSO. The European a-FRR mar-
ket is coordinated through the Platform for the International Coordination of Automated Fre-
quency Restoration and Stable System Operation (PICASSO).
Finally, there are the manual frequency restoration reserves (m-FRR), which currently have an
activation time of 15 minutes. These are activated manually based on signals from the TSO,
hence the name. The common European m -FRR energy activation market is known as the
Manually Activated Reserves Initiative (MARI) platform. On this platform, bids are executed on
the market at 15-minute intervals.
In addition, distribution system operators (DSOs), which are responsible for the electricity dis-
tribution via medium- and low-voltage lines in a specific geographical area , are increasingly
seeking to integrate flexibility resources such as BESS to reduce grid congestion. They have
mechanisms available to support BESS operation in this context, including local flexibility mar-
kets and flexible connection agreements. For this purpose, BESS are increasingly deployed to
ensure that power delivery or consumption at a PoC does not exceed grid limitations.

2.4.6 Firm solar power production and capacity market operation
An increasing number of utility-scale PV + BESS power plants are designed and operated to
provide firm power production. The operation and revenue streams of such power plants are
often governed by power purchase agreements (PPAs). One recent example of such a power
plant is the Kenhardt project in the Northern Cape Province in South Africa, parts of which are
shown in Figure 3 below. This project as, at the time of inauguration in 2023, among the largest
PV + BESS power plants in the world. The PV power plant is made up of three individual PV
projects (Kenhardt Solar Power Plants 1, 2,  and 3), each with a generation capacity of

## Página 28

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

180 MWp. The total 540 MW p of PV capacity is fed into the BESS, which is responsible for
modulating the power output to enable discharge of a consistent 150 MW for 16.5 h every day.
To enable this, the BESS has a nominal capacity of 225 MW/1 .140 MWh. The project was
awarded by the South African Department of Mineral Resources and Energy as part of tech-
nology-neutral procurement programme for independent power producers, with a view to miti-
gating risk.
The project includes around 2 million components in the PV power plant, in addition to 456
units in the BESS. A key factor underpinning the total investment in this project, amounting to
around US$1 billion, is the long -term (20-year) power purchase agreement signed with the
main customer, South Africa’s state-owned electricity utility.
Kenhardt is designed to provide 150 MW of dispatchable renewable energy from 5:00 AM in
the morning to 9:30 PM every day of the year. Failure to deliver in line with the obligation is
financially penalized. Given the scale of the project and the specific terms of the power pur-
chase agreement, the reliability of power generation is of paramount importance, both during
the planning, engineering, procurement and construction (EPC) phases and in the subsequent
operation and maintenance (O&M) phases. Construction of the complex began in July 2022,
and commercial operation started in December 2023. Since it came into operation, the Ken-
hardt project has been running as expected.

Figure 3: Overview of the utility -scale Kenhardt PV + BESS project in South Africa
(Source: Scatec).

2.5 Modelling the use case-dependence of battery degradation
As described above, the degradation and lifetime of a BESS depend on multiple factors , in-
cluding the chosen technology, the sizing and design of the BESS, and the use cases. To shed
more light on the impact of the selected use case(s) upon degradation and lifetime, modelling
is a powerful tool. Much research has been performed to determine the ageing mechanisms
relevant to the different battery technologies , and to use this insight to develop degradation

## Página 29

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
31
models to describe the battery ageing under operation. This, in turn, is used in the development
of methods to support optimal, age ing-aware battery operation, as well as in the preparation
of end-of-life (EoL) estimates. The battery lifetime is usually defined as the time it takes for the
actual capacity to reach a predefined percentage of the nominal capacity. Today, vendors typ-
ically operate with a lifetime definition corresponding to a remaining capacity of 70-80%. This
percentage is often referred to as the state of health (SoH). Although capacity loss is usually
taken as the definition of ageing, it is important to also take other performance indicators, such
as the increase in internal resistance, into account to make accurate assessments of reliability
and performance. Battery ageing is a topic that has been covered extensively in the scientific
literature, and several well-researched review articles have been published on this subject [15–
21]. A brief overview is provided below.
Total battery degradation (Qloss
total) is composed of two additive components: calendar ageing
(Qloss
cal ) and cyclic ageing (Qloss
cyc ). In equation (1) specific stress factors impacting these ageing
modes are included. Time (t), state of charge ( SoC), and temperature ( T) impact calendar
ageing. Cyclic ageing is impacted by the number of cycles, the C-rate, temperature, and the
average SoC and Depth of Discharge (DoD) values under operation.

Qloss
total = Qloss
cal (t, SoC, T) + Qloss
cyc (cycles, C − rate, T, SoC, DoD)   (1)

Different categories of models have been employed to predict battery ageing. One category is
empirical models, in which models are fit to ageing data without considering models of the
actual degradation mechanisms involved. To improve on this, semi-empirical models in which
ageing data is fitted to models constructed to describe known degradation mechanisms and
causes are used [20]. Despite the popularity of the latter, some limitations should be consid-
ered [21]. The most important is the difficulty associated with isolating stress factors and their
corresponding impact, leading to difficulties in merging and extrapolating results beyond al-
ready available data. These limitations can be mitigated through proper test planning, includ-
ing, e.g., larger datasets or strict boundary conditions on the use cases. Both empirical and
semi-empirical models have gained popularity.
A third category comprises physics-based or physio-chemical models, which are based on a
set of equations describing the degradation mechanisms. Although such models can be com-
putationally intensive, they allow for extrapolation beyond the available data [20]. A fourth cat-
egory includes machine learning-based approaches. Such models have been used to calculate
EoL and to optimize BESS operation , also taking ageing into account. The impact of various
operating scenarios, such as frequency regulation and self-consumption peak shaving, on deg-
radation is significant [20]. It has also been shown that BESS control can have a large impact
on EoL. It emerged that different implementations of self-consumption strategies resulted in a
two-year reduction in the service life of the battery system that performed worst in test [21].
This inevitably has significant financial implications.
For Li-ion batteries, the overall ageing consists of three distinct phases. The first of these is
the formation phase, in which the important solid electrolyte interface grows. In the main oper-
ation phase, slower ageing is caused by sustained growth of this interface, as well as other
factors including cathode decomposition, particle cracking,  and dissolution takes place. This
phase continues until the so -called “knee point”, after which the ageing accelerates  towards
EoL, mainly due to lithium plating and electrolyte depletion [20].

## Página 30

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Real-world operations add complexity to predictive modelling of battery ageing. One complex-
ity comes from the opportunity of BESS operators to perform so-called value stacking, i.e., the
use of the BESS capacity to perform multiple use cases with additive revenue streams. Alt-
hough this is widely seen as an opportunity for both increasing profitability and de-risking can-
nibalization across the various markets for different use cases, it also leads to significantly
more complex operating cycles and, consequently, to different stressor regimes.
Another complexity arises when BESS operators choose to, or are forced , to adapt their use
cases over time due to changes in markets and/or regulations. A BESS that was originally
installed for a specific purpose may, under certain circumstances, be operated more profitably
for new use cases. This means that load conditions change over time, which complicates per-
formance analysis based on historical time series and the analysis of stressor-dependent deg-
radation.
A third complexity worth mentioning relates to the fact that “black box” machine learning ap-
proaches are currently being developed for both optimised battery operation and market oper-
ations. In such cases, the ability to create predictive models based on information about the
specifics of the operating duty cycles may be limited.
Finally, it is not only the use case itself that affects calendar ageing, but also the specific im-
plementation via the BESS control elements, which can have a significant impact [21].

## Página 31

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
33
 DETERMINATION OF PERFORMANCE INDICATORS
3.1 Introduction
The performance and reliability-related parameters available on BESS datasheets are deter-
mined using standard test procedures under controlled environmental conditions. This set of
conditions includes a controlled physical and electrical environment, the latter supplied by con-
trollable sources, loads, and sinks. This is well covered in the available literature.
In this report, we focus on methods for determining selected performance indicators (PIs) of
BESS after their deployment. This information is crucial for operators who rely on real-time
information related to the state of the ir BESS for reliable dispatch planning, as well as data-
driven methods for fault detection and diagnostics to ensure low-cost and reliable operations
and maintenance. This information can also guide technology developers and support devel-
opment and validation of improved ageing models and BESS operation strategies.
Performance analysis of BESS in operation is not a new field. However, the development of
performance analysis sufficiently supporting use cases specific to PV + BESS is a work in
progress. Performance analysis encompasses the determination of PIs related to the batteries,
the power electronics, the auxiliary systems within the BESS, as well as the control system. It
also involves assessing the ability of the BESS to meet use case-specific requirements.
Performance analysis on operational BESS is more complex than laboratory-based analysis
under standard test conditions. BESS operation involves incomplete and unpredictable charg-
ing and discharging events very different from the controlled test cycles used in laboratories to
determine the information available in the datasheet. Also, BESS in operation is exposed to
an outdoor environment with either limited control of environmental factors such as tempera-
ture or inclusion of heating and cooling systems which impact their overall standby consump-
tion. Environmental factors can have a substantial impact, as demonstrated in chapter 5.
Monitoring and time series analysis enables continuous determination of PIs  related to the
performance and reliability of BESS. Several of the PIs represent updates of BESS character-
istics already available in the datasheets.
In this chapter, we discuss the following approaches:
1. Factory and Site Acceptance Tests: Factory Acceptance Testing (FAT) and Site Ac-
ceptance Testing (SAT) can give crucial information related to BESS performance and
reliability prior to and from the time of deployment.
2. Data time-series based performance analysis: PIs can be determined by analysis
of either data from normal operation or by analysis of dedicated test duty cycles mim-
icking laboratory conditions. The latter allows for more robust PI determination.
3. Use-case specific PIs: System-level PIs are needed to evaluate the performance and
reliability of PV + BESS towards their specific use case. We focus on selected system-
level PIs relevant for the subsequent discussion of PV + BESS in chapters 4 and 5.

Several documents provide information regarding methods applicable to FAT and SAT and
subsequent performance analysis [12, 22-29]. Some are generally applicable to Electrical En-
ergy Storage (EES) systems and quite generic. The International Electrotechnical Committee
(IEC) has developed relevant standards, including the IEC 62933-1 (2024) “Electrical energy
storage (EES) systems ” [25], which serves as a terminology document . The IEC 62933-2-1
(2018) “Electrical Energy Storage Systems” [12] provides an overview of unit parameters and

## Página 32

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

testing methods e.g. for roundtrip efficiency assessment. The IEC 62933-2-2 (2022) “Electrical
energy storage (EES) systems” [26] includes detailed methodologies for unit parameters and
testing methods including application and performance testing. The Energy Storage Integration
Council (ESIC) has published the “Energy Storage Test Manual”, a comprehensive document,
including commissioning, qualification and system specification [27]. The “Energy Storage Test
Manual: Energy Storage Research Center at Southern Research” [28] describes a framework
for evaluating EES performance. Finally, the “ PNNL Protocol for Measuring and Reporting
Performance of Energy Storage Systems” [29] describes best practices for characterizing EES
systems and measuring and reporting on their performance. The BVES/BSW efficiency guide-
line methods are described in more detail in chapter 4. The IEEE 2030.2.1-2019 “IEEE Guide
for Design, Operation, and Maintenance of Battery Energy Storage Systems, both Stationary
and Mobile, and Applications Integrated with Electric Power Systems” provides comprehensive
guidelines for designing, operating, and maintaining BESS [30].

3.2 Factory and site acceptance tests
Factory Acceptance Tests (FAT) and SATs are commonly used for medium- and large-scale
BESS to give installers and operators access to updated performance and reliability data from
the time of deployment.
3.2.1 Factory acceptance testing
Factory Acceptance Tests involve conducting tests at the manufacturing facility prior to ship-
ping to verify that the BESS is manufactured according to specification and operates correctly
under controlled conditions. The FAT is set up to ensure that the BESS leaves the factory
without defects and can perform as specified, reducing risks before installation. The FAT
should include the following:
1. Visual inspection: Inspection of physical components, such as battery modules, inverters,
protection devices, and control systems. Inspection of the quality of the built, adherence to
design, and overall readiness.
2. Functionality testing: Testing of available control systems, monitoring, alarms, and safety
features, including charging/discharging under controlled conditions.
3. Performance testing: Testing to verify that the system meets rated capacity  and other
relevant PIs.
4. Environmental tests: Depending on customer requirements, testing in simulated environ-
mental conditions can be performed.
5. Documentation: Review and collection of test results, certifications, and manuals.

It is not always possible to run  a FAT with the complete BESS available. With many different
software and hardware vendors , situations in which only parts of the BESS are available at
one site prior to deployment are common. Moreover, realistic, external control possibilities are
often limited at the time of the FAT. Systems are tested with battery simulators or back-to-back
systems without access to all components and functionalities. Despite these limitations, FAT
gives important information related to both product quality, workmanship and performance.

## Página 33

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
35
3.2.2 Site acceptance testing
Site Acceptance Testing and trial operation are  conducted at the installation site once the
BESS has been installed in the PV + BESS power plant. This testing enables functional testing
of a BESS in its operational environment and is set up to  ensure that the system works as
expected in its real-world environment and under local grid conditions. To enable insights be-
yond those already available from the FAT, the SAT should include the following:
1. Physical installation inspection: Ensuring the site layout, cable connections, and en-
vironmental suitability meet design standards.
2. Integration tests: Testing of the grid interconnection, system start-up, and synchroni-
zation with local grid conditions.
3. Functional testing: Testing under real-world conditions, including communication, re-
mote monitoring, and interoperation with local generation and consumption units.
4. Safety testing: Testing safety features such as emergency shutdown, fault conditions,
and fire suppression systems.
5. Performance testing: Verifying rated capacity, efficiency, and other PIs.
6. Final approval: Documenting SAT results and finalizing approval for operation.

The SAT ensures that the system meets the specified requirements e.g. usable energy content
and efficiency, as well as that it is safely and correctly integrated into the site, minimizing risks
related to installation errors or site -specific issues. Whereas the FAT is performed in a con-
trolled environment, the SAT is performed under real-world conditions. We will return to per-
formance testing of the SAT in our discussion below.

3.3 Performance analysis using operational data
In this report we focus on a recommended list of six PIs, which is shown below. These can be
determined both during the above-mentioned FAT and SAT and under operation by analysis
of data time series from either normal operational or using data time series made available by
the use dedicated test duty cycles. More details regarding PIs 1 – 3 is found in Szczuka et al.
[22], PI 4 and 5 in IEC 62933-2-1:2018 [12] and PI 6 in the standard related to the EU battery
passport [31]. These PIs are required for understanding the current state of the BESS.
1. Energy storage capacity
2. Power capacity and tolerance
3. Standby losses
4. Round-trip efficiency
5. Response time
6. Internal resistance

To support their determination, dedicated test duty cycles can be executed while the BESS is
at rest from normal operation. Such test cycles can be programmed into the  EMS and are
generally viewed to enable more accurate determination of PIs than methods based solely on
data from normal operation. The allowable number and the timing of test cycles included for
this purpose will be limited by the available idle time, a use case-dependent factor.
The methods for determining the six PIs are based the availability of data time series, including
measured power, energy, voltages, currents, the SoC, and temperature. The performance of

## Página 34

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

a BESS is highly dependent on environmental factors, particularly temperature. For BESS, the
battery cells are typically maintained within their permissible operating temperature range by
means of active cooling or heating systems. However, ambient temperature has a direct impact
on the auxiliary energy demand associated with thermal management. Furthermore, the oper-
ational profile of the system influences thermal behaviour: higher power levels result in in-
creased losses, which in turn lead to elevated cooling requirements.
For all discussed approaches, testing should ideally be performed under conditions like stand-
ard testing conditions or the requirements of the installation site.  If environmental conditions
deviate substantially from reference conditions, corrections need to be made.
The quality of the performance analysis is limited by the measurement accuracy of the instru-
mentation and/or integrated sensors providing this data and their temporal resolution. Particu-
larly, the determination of efficiency and internal resistance requires a high measurement ac-
curacy and fidelity and internal data of the BMS. Periodic testing and/or calibration of integrated
sensors can reduce the impact of related measurement inaccuracies.
While the methods described herein are suggested for performance and reliability analysis, we
would like to stress that for warranty purposes, a contracted procedure description of how to
measure the relevant PIs between the vendor and owner is typically required.

3.3.1 Energy storage capacity
For a BESS, the capacity to deliver energy is a crucial parameter. Energy storage capacity is
the amount of electrical energy the BESS can store and later deliver , measured in kWh. In
practice, it refers to the available energy within the  allowed DoD range of the BESS taking
power electronics, operating temperature and fade from initial capacity into account. This is a
crucial PI directly impacting the ability of a BESS to perform important functions.
During a SAT energy storage capacity can be measured at the point of connection, accounting
for any conversion losses. It is worth mentioning that the manufacturer often provides perfor-
mance guarantees and datasheet values for the battery (DC) side. Installing calibrated third-
party measurement equipment on the DC side is usually not always possible for verification
purpose. Thus, only built-in voltage/current/power measurement can be used, with the given
measurement uncertainty.
The available energy storage capacity can be determined by first fully charging the BESS and
thereafter measuring the extracted energy while discharging  the BESS at a fixed power until
the BESS either is fully discharged or becomes unable to discharge at the requested power
level. A robust approach is to program the EMS to perform dedicated duty cycles at predeter-
mined intervals. This can be a few times per year (e.g. 4 times) to limit disruption to normal
operation, as well as associated wear. One possible approach is to use a procedure as follows:
1. Fully charge the BESS using constant power
2. Rest for 30 minutes
3. Fully discharge the BESS using constant power
4. Rest for 30 minutes

This test should be run several times to reduce and quantify measurement accuracy and SOC
inaccuracies. More details related to the method and testing conditions are found in IEC 62933-
2-1:2018 [12]. If only data from normal operation is available, algorithms identifying the pres-
ence of suitable duty cycles for such analysis in the data time series are required.

## Página 35

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
37
Either approach enables the operator to assess the fade in energy (“degradation”) from nomi-
nal rated values. This is important for both dispatch planning and O&M, among others by in-
forming decisions related to augmentation and replacement actions.

3.3.2 Power capacity and power tolerance
The power capacity is the maximum instantaneous rate at which the BESS can charge or
discharge energy, measured in kW. Power tolerance is a measure of how well a BESS can
maintain continuous power output  at different conditions, particularly  at different SoC. It is a
measure of the allowable deviation of actual delivered power from the nominal rated power
across the operational range of the BESS. The ability of a BESS to predictably provide power
is crucial for reliable operation. A steep decline in open -circuit voltage and, hence, the ability
to provide power at low SoC has been observed among others for LFP batteries due to cell
imbalance issues.
The power tolerance can be measured already during the SAT. This involves testing the sys-
tem's ability to deliver its rated active (kW) , reactive (kVAR) and apparent power across the
full operating range and includes verifying the PQ curve representing the active and reactive
power relationship to ensure that the system performs consistently within specified limits.
If it possible to run dedicated test duty cycles, using the procedure from 3.3 in a slightly modi-
fied form where also the duration of the discharge in step 4  is monitored is suggested. If the
measured duration differs substantially from a  calculated duration based on nominal power
and energy, this is a good indication of a deviation.
Assessments of a fade in power tolerance from nominal rated values is important to ensure
reliable BESS operation, particularly in high discharge condition. This is important for both the
planning of BESS charging/discharging operations and O&M.

3.3.3 Standby losses
For a BESS system, the standby losses include all energy consumption not related to the
charging and discharging of the battery itself. This added consumption can be caused by aux-
iliary systems, sensors, components, and controls, all of which provide essential functions and
require some power either drawn from the battery or grid to operate. A very important factor is
the consumption by heating and cooling systems. A BESS can often be programmed into dif-
ferent states, allowing for energy saving in idle, standby, or shutdown mode.  Standby losses
directly impact the round-trip efficiencies and the costs of operating a BESS.
Standby losses can be determined at different levels of the BESS hierarchy. One possible
approach which is both relevant for FAT, SAT and analysis based on dedicated test duty cycles
is as follows:
1. Fully charge the battery.
2. Wait for 1 day without charging or discharging the battery.
3. Measure the power and energy consumption of the BESS during the waiting time.
4. Afterwards, recharge the battery to its full state while measuring the power and re-
quired energy to do so.

The energy consumption of the BESS plus the measured recharge energy is the lost energy.
The standby loss is the lost energy divided by the test duration (24 h in the given example).

## Página 36

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

This gives the operator a direct measure of the standby losses. It can be important both for
developing more efficient BESS operation strategies and detecting deviations.

3.3.4 Round-trip efficiency
The round-trip efficiency (RTE) of a BESS is a measure of how little energy is lost during a
charge-discharge cycle. The RTE can be determined and discussed throughout the BESS hi-
erarchy, and it is common to discuss both the cell-level RTE (RTEcell), the RTE on the DC-side
of the inverter including cabling and interconnection losses (DC-RTE) and the RTE on the AC-
side of the inverter also including inverter-related losses, losses in the auxiliary system, as well
as standby losses (AC-RTE).
Here, we discuss how the efficiency of a BESS can be determined using three approaches, all
of which rely on access to charge-discharge cycles. The first approach mimics laboratory tests
and is most readily performed during the FAT, SAT or using dedicated test duty cycles. The
latter approaches are relevant for RTE determination under normal BESS operation.
The RTE is generally defined by equation (2).

RTE = εdischarge / εcharge.     (2)

Here, εdischarge  is the energy delivered from the BESS as it is discharged from its full state until
it reaches its lower cut-off voltage and εcharge the energy consumed as it is charged back up to
its full state.
The first approach is to measure round-trip efficiency using dedicated duty cycles in a con-
trolled environment, either in a laboratory, during FAT, SAT or in the field. In this approach, the
BESS is fully charged and then  fully discharged under a controlled set of conditions. Ideally
this involves a charging phase with constant power and constant voltage and a discharging
phase with constant power, as well as controlled temperature and resting times between the
charge and discharge phases . In this case , the BESS is charged/discharged until the upper
and lower cut-off voltages, as specified in the technical specification. Also, in this case, per-
forming a duty cycle as described in 3.3.1 is the basis. For RTE determination, the charged
and discharged energy is also recorded.
The second approach is referred to as duty cycle efficiency. This approach is based on per-
forming a similar calculation but using a specific suitable duty cycle that is available in the data
from normal operation. Peak shaving duty cycles are a good example; in their simplest form,
they rely on a long and monotonous charge, rest, and discharge phases comparable to stand-
ard test duty cycles set up for the purpose.
The third approach involves summing up the total charged and discharged energy related to
multiple events over a longer time window (days, weeks, or longer) as a basis for the calcula-
tions. In this case, selecting a time window starting and ending with the same SoC is needed.
A longer time window will reduce the impact of inaccuracies at this stage.
In all cases, the calculated efficiency depends strongly on where it is measured within the
BESS hierarchy. The literature on round -trip efficiencies on battery cells is abundant. In a
BESS, the situation is more complex. In a recent study of a fielded BESS, the third approach
above was used to approximate losses throughout the BESS. In th at study, the inverter loss

## Página 37

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
39
was responsible for the largest reductions in RTE (~10.6%), followed by losses in the battery
itself (~3.1%), standby losses (~2.2%) and other losses (~0.9%), resulting in a n AC-RTE of
83.2% [32]. Best in class large scale BESS achieve RTE higher than 88% . For C&I liquid
cooled BESS, impressive AC/AC RTE efficiencies up to 92 % were measured by the Austrian
Institute of Technology. Such a system requires a very high inverter and battery efficiency and
low power consumption for the auxiliary subsystem [33].
For RTE determination, including dedicated test duty cycles ensures as comparable and real-
istic conditions as possible. It is generally important to consider and state both how and where
the efficiency is measured and calculated in the BESS hierarchy to make it clear whether
losses related to, e.g., the inverter, auxiliary systems and other standby losses are included.
For BESS operators, particularly the AC-RTE is important when planning BESS charging/dis-
charging operations and O&M. DC -RTE and RTE cell enables more precise FDD and further
supports O&M.

3.3.5 Response time
The response time is the elapsed time between the moment at which a new power setpoint is
required and the moment at which the battery output power stabilizes within a specified per-
centage of this target setpoint. The response time is a critical PI for many use cases, particu-
larly so for BESS performing ancillary services. Response time includes two critical functions
of a BESS. The first  is referred to as either answering time, waiting time or mode switching
time and is a measure of the time it takes for the inverter to change its state after a prompt is
received. The second is the settling time, a measure of the time it takes for the BESS to stabi-
lize at the new operating point after receiving the request for setpoint adjustment, a parameter
mainly determined by the battery.
Both during the SAT and subsequent operation using dedicated test cycles, the response time
can be measured by measuring the time duration between  a new power setpoint request is
made until the required power output has settled at the new value. One possible approach is
to use a procedure as follows:
1. Start the test with the BESS at rest and at a predefined power set point.
2. Change the power setpoint.
3. Determine the time elapsed between the power request and stabilized power output.

The ramp rate can be determined using the same data set. Accurate determination of the ramp
rate PI obviously requires a sufficiently high temporal resolution. In this context, the ramp rates
for charging and discharging generally differ, and both should be monitored.  More details re-
lated to methods, formulas and testing conditions can be found in IEC 62933-2-1:2018 [12].
If one is confined to data from normal operation, identifying setpoint changes and determining
the time from said setpoint request is sent from the EMS to the power stabilizes at the new
value is needed.

3.3.6 Internal resistance
Measuring the internal resistance of a BESS is not always possible. However, this information
can be important for fault detection and diagnostics . Several factors can contribute to an in-
creased internal resistance in a battery, including changes in the electrolyte, at the electrode

## Página 38

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

interface and subsequently in electrodes, current collectors, contacts and interconnections. An
increased internal resistance can lead to lower available power, reduced round-trip efficiency
and local heat generation.
Determination of the internal resistance usually relies on pulse tests and subsequent calcula-
tion of the resistance based on Ohm’s law. In Equation (3) R denotes the internal resistance,
Vinitial is voltage before the application of the current pulse at no load, V pulse is the voltage during
the application of the current pulse, and Ipulse is the current during the pulse.

R =
Vinitial−V pulse
Ipulse
.      (3)

The calculation of the internal resistance relies on dedicated test pulses and measurements
with a high time resolution. Dedicated test duty cycles can be set up for this purpose. These
pulses and calculations should preferably be performed at stable temperatures and in a man-
ner spanning the full SoC range. The duration of the current pulse is usually in the range of 10
seconds. Pulse-based resistance determination, therefore, requires adequate temporal reso-
lution of data logging, which is sometimes an issue. The lack of suitable pulses in the use case-
specific duty cycles of the battery limits the potential for determining this parameter during
normal operation. More information can be found in DIN DKE SPEC 99100 [31].

3.4 Performance indicators related to specific use cases
In section 3.3, we have discussed 6 performance indicators giving important information
related to the performance and reliability of the BESS itself. In this section, we address system-
level PIs that enable evaluation of the performance of operational PV + BESS systems related
to their targeted use cases. The discussion is limited to PIs relevant to the discussion of the
case studies in chapter  5.
3.4.1 Self-consumption and self-sufficiency
Self-consumption and self-sufficiency are important metrics for a wide range of use cases with
motivations spanning from sustainability to resilience. When coupled with PV generation, the
quantity of self-consumed energy M(t) is defined in [34] as

M(t) = min[L(t) ; P(t) + S(t)],    (6)

where L(t) is the load demand, P(t) the PV generation, and S(t) the BESS power1. Integrating
equation (6) over time gives the rate of self-consumption θSC as

θSC = ∫
M(t)
P(t) dt.     (7)

1 S(t) is defined positive for discharge.

## Página 39

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
41
The definition in (7) is applicable if there is no interaction between the BESS and the grid, i.e.,
no direct charge or discharge. If the BESS interacts with the grid the rate of self-consumption
expands to [35]

θSC
∗ = ∫
M(t)−B(t)
P(t) dt,        (8)

where B(t) is the consumed grid energy. The rate of self-sufficiency is calculated from (7) and
(8) by changing from PV generation P(t) to load demand L(t) in the denominator.

## Página 40

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

 SOLAR POWER AND BATTERY ENERGY STORAGE
SYSTEM PERFORMANCE
4.1 Introduction
This chapter presents a standardized framework for assessing the performance of PV + BESS
[36]. Thereafter, selected results from a Storage Inspection  performed by the University of
Applied Sciences (HTW) in Berlin based on this framework are presented [37]. Some of the
methods and definitions are covered in more detail in the IEA-PVPS Task 13 report P erfor-
mance of New Photovoltaic System Designs [38].

4.2 The efficiency guideline and the HTW Berlin storage inspection
The efficiency guideline is a standardized framework developed by the German Energy Stor-
age Association (BVES) and the German Solar Association (BSW) to assess the performance
and efficiency of PV + ESS systems. This guideline ensures that BESS, particularly those used
in grid -connected PV systems, are evaluated consistently, focusing on PIs such as RTE,
standby losses and response times.
The HTW Berlin "Stromspeicher-Inspektion", hereafter referred to as the HTW Storage Inspec-
tion, is an independent analysis and comparison study led by HTW Berlin. The annual HTW
Storage Inspection evaluates the performance of PV + BESS in private households based on
tested products according to the BVES/BSW efficiency guideline  and from the year 2026 on
according to the standard DIN VDE V 0510 -200 VDE V 0510 -200:2025-11 [39]. It also ad-
dresses the economic aspects of real-world scenarios through simulation.
The HTW Storage Inspection includes assessments of inverter efficiency, battery RTE, control
speed and accuracy by means of laboratory tests. To this end, a "System Performance Index"
(SPI) is introduced, which compares the ability of different systems to maximize the use of
solar power and minimize power consumption from the grid. The SPI is given as a relation
between the simulated annual grid consumption of the system with losses and an ideal system
without losses.
The HTW Storage Inspection emphasizes practical performance under typical conditions, sim-
ulating real-world energy usage patterns. This approach provides accurate consumer insights
into how systems perform and offers transparent results that help consumers to make informed
decisions about which BESS will perform best for their specific needs. It also fosters competi-
tion among manufacturers, driving system design and efficiency improvements. The following
sections review selected test results published in the HTW Storage Inspection until 2024.

4.2.1 Round-trip efficiency and usable energy
In the HTW Storage Inspection, RTEs for multiple full cycles  are measured by fully charging
and discharging the battery at 100%, 50% and 25% of nominal power. The RTEs are calculated
as the ratio of discharged to charged energy and measured at the DC side of the inverter in a
method involving running multiple cycles. An example test sequence for such DC-RTE deter-
mination is shown in Figure 4.

## Página 41

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
43

Figure 4: Example of battery cycling of a system under test with 100%, 75%, 50% and
25% of nominal power to evaluate DC-RTE and net energy. Charging is controlled with
PV simulator production and discharging with an electronic load (Source: AIT).

Mean values over  cycles performed at  100%, 50%, and 25% power are compared for the
participating systems, most of which are LFP batteries. The HTW Storage Inspection 2024
identified substantial differences in the mean DC-RTEs among the tested systems. The highest
mean DC-RTE recorded was 97.8%. On average, the 20 Li-ion batteries tested achieved a
mean DC-RTE of 95.7%. However, some systems showed lower mean DC-RTE, with one
system only reaching 87.9%, nearly 10 percentage points lower than the top performer. The
system was listed as an anonymous participant, which was independently bought for testing.
Hence, details regarding the root cause are not available for this system.
The mean DC-RTEs reported were influenced by the batteries being discharged using different
C-rates. Different C-rates result from the current limitations of the inverter and battery. Never-
theless, the C-rates of residential systems did not vary strongly and are usually below 1 C.
In some cases, the usable energy differed from the manufacturer’s stated values in the
datasheet, with a general deviation of -2% and a maximum deviation of -11%. For two systems,
the usable energy was higher than what was declared in the datasheet, by +2%.

4.2.2 Inverter efficiency
The inverter efficiency plays a crucial role in the overall system performance. In the HTW Stor-
age Inspection, it is measured according  to the BSW/BVES efficiency guideline, like the
EN 50530 testing procedure for the  efficiency assessment of PV inverters. The inverter effi-
ciencies are determined for 8 power levels (100%, 75%, 50%, 30%, 25%, 20%,10%, and 5%
of nominal power) for different operation modes, which define the energy flow path as indicated
in Figure 4:
• PV2AC: Direct PV feed-in
• PV2BAT: PV battery charging
• BAT2AC: Battery discharging
• AC2BAT: Battery charging from the AC side.

## Página 42

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Figure 4: Energy conversion pathways of the individual topologies of PV storage sys-
tems [36] (Source HTW Berlin).

No combined power flows are considered for efficiency evaluation. This means that situations
such as direct PV feed-in and simultaneous charging of the battery from the grid are not inves-
tigated. An efficiency chart for BAT2AC is shown in Figure 5. The BAT2AC efficiency is meas-
ured in the laboratory test at 8 power levels, and then the efficiency is interpolated by averaging
it to 10 equally distributed points between 5% and 95% of nominal power of the battery [37].
The best-performing inverters achieved average BAT2AC efficiencies above 97%, as indicated
in Figure 6. These systems might benefit from higher DC voltage levels of the battery, which
reduce losses during the conversion process. However, lower -performing inverters had effi-
ciency levels as low as 91.2%, which resulted in substantial energy losses during both charging
and discharging cycles [37].

Figure 5: BAT2AC full and partial load efficiency of two systems [37] (Source HTW
Berlin).

## Página 43

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
45

Figure 6: Averaged BAT2AC efficiency for systems described in the HTW storage in-
spection [37] (Source: HTW Berlin).

The PV2BAT efficiency can be higher for DC -coupled systems than for AC-coupled systems
because no DC-to-AC conversion is required. In contrast, for AC-coupled systems, the power
rating of the  battery inverter can be sized independently from the PV inverter. A low power
rating of the battery inverter for residential households might benefit from higher BAT2AC effi-
ciencies at partial load power  below 5%. This can be a realistic scenario when discharging
batteries during evening hours and at night. Especially at low power , efficiency differences
between inverters become apparent. Such a test at low power output related to its nominal
power is also described in the HTW storage inspection [37]. The BAT2AC efficiency of several
10-kW systems was tested at low power . At the lowest powers (~100W), the BAT2AC effi-
ciency varied a lot, ranging from below 50% to almost 90%.
Systems using silicon carbide (SiC) power electronics and working with high battery voltages,
thereby decreasing the input/output voltage ratio, achieved high BAT2AC efficiencies also at
low power levels. For battery systems with small capacity, the trend is to go to high Ah ratings
for battery cells, resulting in a low battery voltage. In this case, it gets challenging for systems
to achieve high BAT2AC efficiencies.

4.2.3 Standby losses
Standby losses are reported as part of the overall system loss and minimizing this is crucial
for improving overall system efficiency. The lowest standby consumption in the HTW storage
inspection was 2 W for a 2.3 kW AC-coupled system, while most 10-kW DC-coupled systems
had an energy consumption between 10 and 20 W . One system consumed 64 W, illustrating
how standby losses can be substantial in BESS.

## Página 44

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

4.2.4 Response time
In the HTW Storage Inspection, the response time of the systems is evaluated. The report
uses the term “ control speed” as a measure of qu ickly a BESS can respond to changes in
conditions, such as power demand or generation variations . Slower systems with longer re-
sponse times can experience delays in supplying energy during peak demand periods, leading
to increased reliance on the grid and reduced cost savings.
In practice, the response time is evaluated by executing a total of 140 load (14 x 10 iterations)
steps during constant PV generation and measuring the answering and settling time at which
the BESS starts charging or discharging to compensate for t he resulting energy surplus o r
deficiency.
From available data, efficient systems show very short answering times, often < 1s. For sub-
sequent settling times, the top-performing systems stabilize quickly after a change, often within
a few seconds (< 2 – 5 s), depending on the load and system configuration.

4.3 Discussion
The HTW Storage Inspection is a comprehensive and valuable source of data and experience
related to the actual performance of fielded PV + BESS. The study clearly shows how the PIs
of different systems can exhibit substantial variation. This includes large observed variations
in the RTE of BESS approaching 10% and large variations in inverter efficiency, particularly at
low loads, which translates into substantially different average efficiencies. In addition to illus-
trating the need for continuous performance and reliability analysis, t he study results are im-
portant as a benchmark for other studies and systems  and as a source of information on the
impact of technology choices and designs on the overall PV + BESS performance. With the
increasing deployment of residential PV + BESS combined with an ageing fleet of such sys-
tems, it will be important to expand the use of such performance analysis. In this context, a
harmonization in terms of instrumentation, data format, quality standards, and the exact meth-
ods implemented for performance analysis and reporting will be beneficial.

## Página 45

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
47
 CASE STUDIES
In this chapter, three case studies based on systems designed to perform very different use
cases are presented.

A. The Florida SunSmart E-shelter Schools PV + BESS targeting resilience
B. The RISE PV + BESS targeting self-consumption and self-sufficiency
C. A fleet of BESS performing ancillary services

5.1 The Florida SunSmart Schools
The SunSmart E -Shelter Schools program is the first in Florida to outfit emergency shelter
schools with PV + BESS. At least 114 10-kWp PV systems, an example of which is shown in
Figure 7 below, are currently installed in schools designated as emergency shelters throughout
Florida. Florida Solar Energy Center (FSEC), Florida’s premier energy research center at the
University of Central Florida (UCF), coordinated the installations, which began in 2010. In the
event of an emergency, these PV + BESS systems use the energy stored in the batteries to
provide power to key aspects of the emergency shelters for the local population.  To ensure
that the systems are installed, operated, and maintained safely and reliably, FSEC and mem-
bers of Florida’s PV industry have worked closely with code officials in nearly every municipality
in the state and trained over 100 facility managers on the O&M of the systems. These systems
have become important centerpieces of community events, with students and teachers acting
as ambassadors to educate local citizens about local clean electricity production.

Figure 7: A PV + BESS installed in a school through the SunSmart E -shelters program
(Source: UCF).
An example of a  typical system is a grid -connected PV system with battery backup, with PV
generation consisting of 42 Solar World SW-240 modules with a combined nominal DC output

## Página 46

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

power of 10  kWp. The system batterie s are sized 610 Ah at 48 V, providing approximately
27 kWh to standby (uninterruptible) loads. Figure 8 below shows the system's design. When
the sun is shining, power from the PV array is used to keep the batteries  fully charged. After
charging the batteries, any excess PV power is made available to the critical loads. If the avail-
able PV power also meets the requirements of these loads, any remaining PV power is then
directed to the interruptible loads of  the occupancy. If any PV power remains after the inter-
ruptible loads have been powered, it is delivered to the utility. When utility power is available,
but PV power is not available, the utility supplies critical loads. If neither utility nor PV power is
available, critical loads must be supplied by the batteries. The batteries used are specially
designed, deep cycle,  maintenance-free, capable of undergoing approximately 3000 -4000
charge-discharge cycles. Designing the system to minimize battery cycling extends the life of
the batteries.

Figure 8: PV + BESS system design in the SunSmart Schools E -shelters program with
power flow illustration (Source: UCF).

The SunSmart E-Shelters Schools programme provides access to large volumes of real-world
data and is ideal for use in data -driven modelling. Details on using real -world data to under-
stand the behaviours of the systems can be found in a published foundation model applications
using spatiotemporal Graph Neural Networks  [40] and in the “Digitalisation and Digital Twins
in Photovoltaic Systems” IEA PVPS Task 13 report [41].
An important aim of this report was to develop a common framework for analysis of operational
PV + BESS and to access data from relevant systems performing different use cases. To sup-
port this goal and more generally research and education in this important field, the data col-
lected through the SunSmart Schools project is made available on  the open data platform,
OSF [42].

## Página 47

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
49
Table 9: Summary of the experience from the SunSmart Schools case study.
The SunSmart Schools – Back-up power
Description Distributed fleet of PV + BESS in emergency shelters (Florida/USA).
Use case Back-up power.
Relevance Reliable operation as source of back-up power crucially important.
Experience
Battery is designed to cycle when utility power is lost, an effective design in emergency
shelters. In addition to crucially supporting shelter operation, data made available from
these PV + BESS will support further research, training and education.

5.2 The RISE PV + BESS: self-consumption and self-sufficiency
5.2.1 The RISE Research villa
RISE’s Research Villa, shown in Figure 9, is a residential building in Sweden with space heat-
ing and domestic hot water generation using a ground -source heat pump. The house was
developed and built within the EU-FP7 collaborative project  (NEED4B) to demonstrate cost -
effective and energy-efficient technologies. Fourteen PV panels, each with a nominal capacity
of 260 kW p, were installed at a 45  tilt angle due south to help to achieve an annual primary
energy consumption target of 60 kWh/m2. Blueprints and more detailed information about the
house can be found in P. Ollas et al. [43]. Data is acquired from the Research Villa with a 15-
minute temporal resolution for a year’s operation. The total electricity demand was 6354 kWh.
The PV array has a rated peak power of 3.68 kWp and an annual generation of 3113 kWh.

Figure 9: RISE Research Villa in Borås, Sweden (Source: RISE).

## Página 48

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Ollas et al. [32] reported the effect of battery sizing and dispatch on self-consumption (SC),
self-sufficiency (SS) and peak power shaving in a simulation study. Two peak shaving algo-
rithms, “day-ahead” and “day-behind”, were taken from the System Advisory Model (SAM)
software2. A third algorithm titled “maximize self-consumption” was taken from Fares et al. [44].
A perfect forecast of the upcoming day’s PV generation and load demand is assumed in the
day-ahead approach. In the day-behind approach, the PV energy and load profile from the day
before are taken as if they were the actual data for the day in progress.  The maximize SC
dispatch prioritizes PV load coverage and battery charge before feeding any excess to the
external grid [45].
Figure 10 shows the annual degree of SC as a function of battery size for the three dispatch
algorithms. For the maximize SC dispatch, increasing the battery size beyond 7.2 kWh mar-
ginally enhances the SC. The saturation effect on SC from battery sizing is supported by pre-
vious findings [47, 48]. Beyond the saturation size , the battery is not fully discharged during
the night, so the following day’s excess PV will be sufficient to fully charge the battery during
the early hours. After that, the excess PV will be fed to the grid.

Figure 10: Self-consumption as a function of battery size for three dispatch algorithms
(Source: RISE).

In the peak shaving algorithms , day-ahead (DA) and day-behind (DB), some SC enhance-
ments are observed with increased sizing. However, as it is not the primary purpose of the
operation, the quantity is less than that of the maximize SC operation. It is also noticeable that
beyond 10.8 kWh battery sizing, the SC is reduced when the DA and DB operation modes are
chosen, while it saturates for maximize SC operation [32]. This illustrates how the optimal sys-
tem sizing of a BESS can depend on the selected mode of operation.

2 System Advisor Model—https://sam.nrel.gov, URL accessed 2024-02-19.

## Página 49

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
51
5.2.2 The RISE PV + BESS field
RISE has an experimental setup of nine PV arrays in Borås, Sweden, with various array sizes,
and cell technologies including building-applied and building-integrated PV systems. Figure 11
shows an overview of the test-site and the nine systems. In Figure 12 the system in the lower
right corner is equipped with a battery storage (5.7 kWh).

Figure 11: Overview of the PV array systems at RISE laboratory in Borås, Sweden
(Source: RISE).

Figure 12: Close-up photo of PV arrays at RISE. The PV array connected to the battery
system is in the lower right corner (Source: RISE).

## Página 50

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

(a) (b)
Figure 13: Annual (a) self -consumption as a function of array size and (b) self -suffi-
ciency as a function of array power and annual PV yield (Source: RISE).

Ollas et al. [46] verified the hypothesis of Luthander et al. [32] that there is a negative correla-
tion between array size and self -consumption using field measurements. In Ollas et al. [4 6],
the seasonal effect on SC and SS from the selected BESS is evaluated and compared to a
reference case without integrated storage. The annual evolution of the field performance con-
firms the SC and array power correlation from Luthander et al. [32], as shown in Figure 13a3.
However, in contradiction to Luthander et al. [32], no positive correlation between SS and array
power was observed; see Figure 13b. An explanation could be that SS uses the absolute SC
normalised by the load demand, unlike the SC that uses the PV yield in the denominator. Since
this study includes different cell technologies and roof integrations [4 6], comparing the yearly
SS with the energy yield is more relevant. The yield better reflects the system’s performance
and presents a more relevant index for this correlation. So, when comparing the annual SS
with the energy yield, a positive correlation is identified.
The weekly SC and SS of the PV + BESS are compared to a modified output profile in 5 to
examine the seasonal effect from battery self-consumption maximisation dispatch. As seen in
Figure 14a, there is no effect on SC from the battery during the winter period. Instead, the gain
from the battery is observed during periods with PV surplus, with a peak SC gain of 30 per-
centage points. In absolute terms, the battery increases the self-consumed PV energy annually
by 738 kWh. As for SS, peak gains exceed 40 percentage points during the summer; see
Figure 14b. However, the battery has a negative effect during the winter. The latter is due to
the standby losses associated with the maintenance charging of the battery. Annually, the
system without BESS has an SC of 50%; with a BESS, an SC of 70% was reached.

3 The results exclude the battery system and an additional system due to malfunction operation.

## Página 51

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
53

(a) (b)
Figure 14: Comparison of weekly (a) self-consumption and (b) self-sufficiency with and
without battery storage (Source: RISE).

Table 10: Summary of the experience from the RISE PV + BESS case study.
The RISE PV + BESS systems – Self-consumption and Self-sufficiency
Description PV + BESS systems deployed at the RISE campus in Borås (Sweden)
Use case Self-consumption (SC) and self-sufficiency (SS)
Relevance SC and SS strongly dependent on environmental conditions.
Experience BESS contributes strongly to both total SC and SS throughout the year. However, the
BESS plays a neutral to negative role in winter, having few occasions with PV surplus.

5.3 Grid-supporting BESS and market operations
5.3.1 An introduction to the Swedish markets for grid-supporting BESS
Since 2021, there has been a rapid increase in the deployment of BESS in Sweden . This
development has largely been driven by a substantial potential for generating revenue within
virtual power plant  (VPP) services. Within this field, ancillary services have  contributed to a
major part of revenue . For the years 2021 –2024, profitability for BESS in this context was
primarily associated with the provision of faster ancillary services, notably FFR and FCR ser-
vices. These ancillary services are quite technically demanding compared to , for example,
BTM services or slower forms of ancillary services and energy trading. A combination of dif-
ferent FCR services was usually financially optimal during these years, giving revenues of 0.6
– 0.7 MEUR/MW/year. This is about ten times higher than the revenue obtained in the more
mature BESS and VPP market in the UK. As of fall 2024 , the market in Sweden has shifted,
and the ideal VPP operation now includes a mix of flexib ility services [49]. The total revenue
level has also dropped significantly. This is a clear illustration of how changing market condi-
tions over time can lead to changes in targeted use cases for and optimal operation of BESS.
The large number of residential and Commercial- and Industrial-scale (C&I) BESS, both of
which are typically installed in combination with PV systems, participating in primary reserves
in Sweden during the past years is quite unique in a global context.

## Página 52

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

5.3.2 Operational experience from performing ancillary services in Sweden
Here we share the experience of an energy services company based in Sweden that provides
solutions for asset management, performance monitoring, and VPP and EMS platforms. By
September 2024, the company operated a VPP in Sweden and neighbouring Nordic countries
with roughly 250 MW of battery peak capacity. This capacity is divided equally across three
segments: residential BESS (up to size 50 kW), C&I BESS (50 kW - 1.5 MW), and utility-scale
BESS (1.5 MW and above). This translates to ~15,000 individual BESS sites, with the larger
quantity in the residential segment. Within the VPP, there are about 50 different BESS models.
The critical components in these systems are identified as the inverters and the batteries.
The operation of these BESS has generated substantial experience related to performance
and reliability. Among important learnings are the following:

● SoC level accuracy: Most BESS in the portfolio is based on LFP cell technology. As
mentioned in chapter 2, one inherent property of this technology is a rather flat voltage
to SoC curve. Therefore, the determination of the exact SoC at any given time and
voltage is challenging. Experience from operating different systems with different BMS
implementations shows that the calculated SoC differs between different systems on
the market. Using multiple test cycles can improve accuracy, as discussed in chapter 3.
● Cell balancing: As described in chapters 2 and 3, efficient operation of a BESS con-
sisting of several battery packs, each comprising multiple battery cells, requires c ell
balancing. Cell balancing involves charging the BESS up to a SoC of 100%. Since the
BESS typically needs to be removed from normal VPP operation for this purpose , a
frequent need for balancing can have a substantial negative impact on revenue. There
is still a need to improve BESS software solutions in this space. Today, imperfect cell
balancing routines can lead to reducing available capacity by as much as 5-10%.
● Limited cell cycling: In operational modes such as BTM peak shaving or energy ar-
bitrage, or in FTM operation related to the slower ancillary services, the BESS will be
subjected to cycling up to a SoC of 100%. But when a BESS provides primary reserve
ancillary services such as FCR, it is mostly in a state of preparedness, delivers power
in shorter bursts, and rarely or never performs SoC cycles up to 100%.
● Extreme temperature operation: As discussed in chapter 2, all batteries' calendar life
and performance are affected by the environment in which they are deployed. Different
cell chemistries respond differently to low and high temperature conditions. Even within
one technology, such as LFP, there are variations in cathode, electrolyte and anode
material, resulting in substantially different temperature-dependence. As outdoor tem-
perature decreases during fall and winter, VPP portfolios with distributed BESS in Swe-
den have experienced diminished available capacity by as much as 40% compared to
summer since wherever the systems are installed outdoors or in non-heated rooms. To
avoid or limit this effect, some BESS products have internal heating and/or insulation.
The BMS can also include temperature-dependent settings to protect the cells with a
dynamic safety margin. The largest reduction in capacity at low-temperature operation
is related to the services requiring faster ramp rates . The related impact on services
requiring slower ramp rates is low.

## Página 53

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
55
● Firmware stability and unexpected updates: A fair amount of software exists, even
for residential BESS. Manufacturers normally dispatch firmware updates regularly,
patching possible bugs and improving the  performance of installed fleets. It is crucial
that these manufacturers keep in mind that the systems are not negatively affected by
updates, as they are mostly operational in VPP services.
● Connectivity, local control interface and protocols, cloud services: A VPP opera-
tor provides the control logic for the various services that occur. This is either based on
control via a local device that controls the VPP operat ion or based on control via a
cloud service, i.e., a situation in which the VPP operator communicat es with a cloud
service that is, in turn, controls the BESS. VPP service off takers tend to prefer direct
control through a physical device to avoid relying on cloud services. When a local de-
vice is used , the physical interfaces of  Ethernet and RS485 are common. The most
common communication protocols are Modbus, MQTT and IEC 104.
● Cybersecurity: One important aspect of reliability is whether a manufacturer without a
contract or agreement with the VPP off-taker retains some control over the BESS in
parallel with the VPP operator. This is sometimes viewed negatively from an IT security
perspective. Ancillary services are crucial for the grid and, thus,  part of the critical in-
frastructure for society and industry.
● Grid connection capacity saturation: The ability of a BESS to charge and discharge
electrical power depends on the ability of  that power to be taken from or absorbed by
the grid. A BESS must therefore be designed according to the fuse size of the grid
connection. However, in most cases, there will be times when the level of PV production
will limit the remaining possibility of discharging the BESS: the grid connection is satu-
rated already. A similar situation is observed for sites with loads that consume electric-
ity, thereby limiting the possibility of charging the BESS. This need s to be considered
in VPP operations and will limit the ability to provide flexibility services.
● Ageing: VPP services have different characteristics in terms of how much energy there
is in their delivery and since batteries degrade both due to calendar ageing and cyclic
ageing, as discussed in chapter 2, the calculated cost due to such ageing is important
for VPP optimization. Ageing characteristics vary between different cell chemistries. In
many cases, manufacturers are currently unable to provide reliable data on these age-
ing characteristics. The manufacturer’s warranty may also differ depending on the op-
erational limits, such as the C-rate or depth of discharge used. In a Swedish context ,
the internalised cost of cycling has been set at a wide range of 50-250 EUR/MWh over
the past few years. This large span and substantial financial impact clearly illustrate the
need for improved data related to the ageing of PV + BESS.

## Página 54

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

Table 11: Summary of the experience from the VPP operator case study.
VPP operator – Ancillary services
Description Distributed fleet of residential and C&I BESS (Nordics)
Use case Ancillary services only (first year), value stacking (recent years)
Relevance To enable participation in the reserve markets, the TSO always requires reliable access
to the BESS units
Experience
Cell balancing is important for LFP cells batteries. Accurate SoC determination is chal-
lenging. Inaccurate cell balancing can cause SoC losses of up to 5–10%, in addition to
incorrect SoC estimates, impacting operation. Frequent balancing interrupts operation
and further reduces revenue.
Unless heating is applied, seasonally low outdoor temperatures in Sweden can reduce
usable energy be up to 40%. Also, kinetics are impacted. This is especially a challenge
for BESS providing ancillary services requiring fast ramping. Inclusion of heating leads to
large standby losses.
Not all manufacturers provide reliable data on aging. This impacts cost estimates for
O&M of BESS operation, particularly the estimated need for BESS replacements.
Connectivity and software-related issues can drive downtime and underperformance.

## Página 55

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
57
 CONCLUSIONS
In this report, we have reviewed battery technologies, common use cases of PV + BESS, and
models of battery ageing. The large variety in battery cell chemistries and battery designs, as
well as in the design and selection of components and software, affects the performance and
reliability of a complete BESS and its lifetime. The wide range of operating environments, both
physical and electrical, directly impacts the strongly temperature -dependent calendar ageing
and the duty‐cycle‐dependent cyclic ageing.
Owners and operators rely on precise information regarding the current state of health (SoH)
of their PV + BESS to schedule charging and discharging events in line with the relevant use
case(s). Moreover, they need to plan inspections, repairs and replacements in a cost‐effective
manner to keep their PV + BESS operating in line with expectations. Prior to operation, factory
acceptance tests (FATs) and site acceptance tests (SATs) are important and frequently used
methods to ensure functionality and performance. During operation, continuous access to data
combined with the determination of relevant performance indicators (PIs) is needed to support
operators in this work.
In this report, we focus on the determination of six selected PIs that are important both for
performance with respect to the selected use case(s) and for BESS operations and mainte-
nance (O&M). These PIs can be determined from available data time series fr om operational
BESS. They are capacity, power tolerance, internal resistance, round‐trip efficiency, response
time and standby losses. Major changes in any of these parameters can lead to substantial
underperformance and are useful for prioritizing and scheduling mitigating actions. Methods
for assessing the six PIs based either on data time series obtained during normal operation or
on dedicated test cycles for characterization can be applied. The latter enables cycling under
conditions more closely resembling standard test conditions. In this report, we outline methods
for determining relevant PIs in both cases.
To illustrate the type of information that becomes available from this kind of analysis, we show
selected findings from the HTW Berlin Storage Inspection. This important and openly available
work shows that there are substantial performance variations in i nstalled BESS, both in the
batteries themselves and in the inverters. We also share experience from the operation of PV
+ BESS set up to perform three very different use cases: resilience (back‐up power), self‐con-
sumption and self‐sufficiency, and grid services.
There are several main takeaways from this report. Firstly, the ageing of BESS supporting PV
power plants depends on the concrete use case, deployment environment, technology, and
design. To assess the fade of important BESS parameters from their initial values, monitoring
systems enabling the determination of the above ‐mentioned six PIs of a BESS in operation
are needed. Secondly, validated and representative ageing models are key for project devel-
opment and subsequent cost ‐optimal O&M, ageing ‐aware BESS operation, and precise
end‐of‐life (EoL) determination.

## Página 56

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

In addition to hardware -related issues, connectivity and software -related issues also impact
reliability and performance. Firstly, such issues drive downtime and underperformance. More-
over, cybersecurity is a crucial fundament for reliable operation.
To enable the required research and development, access to high ‐quality data with sufficient
temporal resolution is required for data ‐driven performance and reliability analysis. Data ac-
cess is a well ‐known bottleneck from the development of similar time ‐series‐based methods
for assessing the performance and reliability of PV modules and inverters. To improve on the
current situation with limited data availability, more system owners with sufficiently instru-
mented BESS will need to be willing to share their data and experience. An increasing amount
of data and experience generated and shared, including data from a growing fleet of aged
systems, will support future scientific and technological advancements in this important field.
As the fleet of operational BESS continues to expand, the assessment of their performance
and reliability will become increasingly important, mirroring the trend previously observed for
PV power plants. To support this work, IEA  PVPS Task 13 experts will continue working on
BESS performance and reliability during 2026 to 2029.

## Página 57

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
59
REFERENCES
[1] G. Masson et al., "Snapshot of Global PV Markets ", Report IEA-PVPS 2025
[2] Volta Foundation, “The Battery Report 2025.ˮ 2026
[3] J. Carroquino et al., “Comparison of Economic Performance of Lead-Acid and Li-Ion Batteries in Standalone
Photovoltaic Energy Systems”, Appl. Sci., 11(8), 2021, DOI: 10.3390/app11083576
[4] T. Costa, J. L. de Souza Silva and M. G. Villalva., “An overview of Electrochemical Batteries for ESS Applied
to PV Systems Connected to the Grid”, 14th IEEE International Conference on Industry Applications, 2021,
DOI: 10.1109/INDUSCON51756.2021.0529464
[5] L. Srinivasan, S. Shaw and E. Billaut., “Insights from EPRI’s Battery Energy Storage Systems (BESS) Fail-
ure Incident Database”, Electric Power Research Institute (EPRI) White Paper, 2024
[6] H. Zhang, W. Lu and Z. Li ., “Progress and Per spectives of Flow Battery Technologies”, Electrochemical
Energy Reviews, 2(3), 2019, DOI: 10.1007/s41918-019-00047-1
[7] K. Mongird et al. “An Evaluation of Energy S torage Cost and Performance Characteristics”, Energies,
13(13), 2020, DOI: 10.3390/en13133307
[8] C.P. Grey and D. S. Hall al., ”Prospects for lithium-ion batteries and beyond – a 2030 vision”, Nature Com-
munications, 11, 2020, DOI: 10.1038/s41467-020-19991-4
[9] R. Usiskin et al., “Fundamentals, status and promise of sodium-based batteries”, Nature Reviews Materials
6, 2021, DOI: 10.1038/s41578-021-00324-w
[10] H.S. Hirsh et al., ”Sodium-ion Batteries Paving the Way for Grid Energy Storage”, Advanced Energy Mate-
rials 10, 2020, DOI: doi.org/10.1002/aenm.202001274
[11] C. Doetsch et al., “Electric Energy St orage – Future Energy Storage Demand”, IEA ECES 2026 Final Re-
port, 2015
[12] IEC 62933 -2-1:2018 “Electrical energy storage (EES) systems – Part 2 -1: Unit parameters and testing
methods – General specification”, IEC, 2018
[13] Ø.S. Klyve et al. , ”The value  of forecasts for PV power plants operating in the past, present and future
Scandinavian energy markets”, Solar Energy, 255, 2023, DOI: 10.1016/j.solener.2023.03.044
[14] Ø.S. Klyve et al., ”Limiting imbalance settlement costs from variable renewable energy sources in the Nor-
dics”, Applied Energy, 350, 2023, DOI: 10.1016/j.apenergy.2023.121696
[15] I. Bloom et al., ”An accelerated cal endar and cycle life study of Li -ion cells”, Journal of Power Sources ,
101(2), 2001, DOI: 10.1016/S0378-7753(01)00783-2
[16] J. Wang et al., “Cycle-life model for graphite-LiFePO4 cells”, Journal of Power Sources, 196(8), 2011, DOI:
10.1016/j.jpowsour.2010.11.134
[17] X. Hu et al., “Cost-Optimal Energy Management of Hybrid Electric Vehicles Using Fuel Cell/Battery Health-
Aware Predictive Control”, IEEE Transactions on Power Electronics , 35(1), 2019, DOI:
10.1109/TPEL.2019.2915675
[18] W. Vermeer, G. R. C. Mouli and P. Bauer., “A Comprehensive Review on the Characteristics and Modeling
of Lithium -Ion Battery Aging”, IEEE Transactions on Transportation Electrification , 8(2), 2022, DOI:
10.1109/TTE.2021.3138357
[19] E. Wikner and T. Thiringer , ”Extending Battery Life time by Avoiding High SOC” , Applied Science, 8(10),
2018, DOI:  10.3390/app8101825

## Página 58

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation

[20] N. Collath et al., “Aging aware operation of lithium-ion battery energy storage systems: A review”, Journal
of Energy Storage, 55, 2022, DOI: 10.1016/j.est.2022.105634
[21] N. Munzke, B. Schwarz and J. Barry, “The Impact of Control Strategies on the Performance and Profitability
of Li-Ion Home Storage Systems”, Energy Procedia, 135, 2017, DOI: j.egypro.2017.09.504
[22] C. Szczuka. P. Sletbjerg and M. Bruchhausen, “Performance and Durability Requirements in the Batteries
Regulation - Part 1: General assessment and data basis”, Publications Office of the European Union, DOI:
10.2760/289331, 2024
[23] A. Claire et al., “BESSential – Modernizing Traditional BESS Factory A cceptance Testing with Advanced
Battery Diagnostics”, Sinovoltaics White Paper, 2023
[24]  “Battery Energy Storage Systems – from selection to commissioning: best practices”, Sinovoltaics, 2022
[25] IEC 62933-1:2024 “Electrical energy storage (EES) systems – Part 1: Vocabulary”, IEC, 2024
[26] IEC TS 62933-2-2 “Electrical energy storage (EES) systems – Part 2-2: Unit Parameters and testing meth-
ods – Application and performance testing”, IEC, 2022
[27] E. Minear, S. Willard and P. Ip, “ESIC Energy Storage Request for Proposal Guide”, EPRI Report, 2019
[28] “Energy Storage Test Manual for the Energy Storage Research Center at Sourthern Research: Task 4”,
EPRI Technical Update 2018
[29] K. Bray et al., “Protocol for Uniformly Measuring and Expressing the Performance of Energy Storage Sys-
tems” PNNL Technical Report, 2012
[30] “2030.2.1-2019 - IEEE Guide for Design, Operation, and Maintenance of Battery Energy Storage Systems,
both Stationary and Mobile, and Applications Integrated with Electric Power Systems ”, IEEE, 2019, DOI:
10.1109/IEEESTD.2019.8930450
[31] DIN DKE SPEC 99100, "Requirements for Data Attributes of the Battery Passport”, 2025
[32] S. Aljabore., “Efficiency of Lithium-Ion Battery Energy System”, Master thesis, University of Oslo, 2023
[33] ACCURE: “2025 Energy Storage System Health & Performance Report”, ACCURE, 2025
[34] R. Luthander et al., “Photovoltaic self -consumption in buildings: A review”, Applied Energy, 142, 2015,
DOI: 10.1016/j.apenergy.2014.12.028
[35] P. Ollas et al., “Impact of Battery Sizing on Self -Consumption, Self-Sufficiency and Peak Power Demand
for a Low Energy Single -Family House with PV Production in Sweden”,  IEEE 7 th WCPEC, 2018, DOI:
10.1109/PVSC.2018.8548275
[36] https://solar.htw-berlin.de/wp-content/uploads/Efficiency-guideline-for-PV-storage-systems-2.0.pdf
[37] J. Weniger et al., “Energy Storage Inspection 2024”, HTW Berlin Report, 2024
[38] M. Litwin et al. “Performance of New Photovoltaic System Designs” IEA PVPS Task 13, Report IEA-PVPS
T13-15:2021, April 2021 ISBN 978-3-907281-04-8
[39] DIN VDE V 0510-200:2025-11, ”Kennwerte stationärer Batteriespeichersysteme“, 2025
[40] P. Tripathi et al., “Data -Driven Digital Twins for Manufacturing, Parts and  their Service Life”, Scientific
Reports – Digital Twin Collection, 2024
[41]  A. Louwen, A., Schill, Ch. (2026). Louwen, A., Schill, Ch, Bruckman, L., Jahn, U.  (Eds.), “Digitalisation
and Digital Twins in Photovoltaic Systems” (Report No. T13-34:2026). DOI:10.69766/RMPH3089.
[42] W. Oltien et al., “Time-Series Data of Photovoltaic Systems Installed in Florida”, osf.io/8ucaq, 2023

## Página 59

Task 13 Reliability and Performance of PV Systems - Assessing the Reliability of Battery Systems in Solar Power Plants in Operation
61
[43] P. Ollas et al., “Energy Loss Savings Using Direct Current Distribution in a Residential Building with Solar
Photovoltaic and Battery Storage”, Energies, 16(3), 2023, DOI: 10.3390/en16031131
[44] R.L. Fares and M. Webber ,” The impacts of storing solar energy in the home to reduce reliance on the
utility”, Nature Energy, 2, 2017, DOI: 10.1038/nenergy.2017.1
[45] S. Quoilin et al., “ Quantifying self-consumption linked to solar home battery systems: Statistical analysis
and economic assessment”, Applied Energy, 182, 2016, DOI: 10.1016/j.apenergy.2016.08.077
[46] E. Nyholm et al.,” Solar photovoltaic-battery systems in Swedish households: Self- consumption and self-
sufficiency”, Applied Energy, 183, 2016, DOI: 10.1016/j.apenergy.2016.08.172
[47] P. Ollas, J. Persson and P. Kovacs, “Effect of Energy Storage on Self-Consumption and Self-Sufficiency:
A field study in a Nordic Climate”, Proceedings of the EUPVSEC , 2021, DOI:
10.4229/EUPVSEC20212021-6BV.5.16
[48] P. Ollas, J. Persson and P. Kovacs , “Technical Performance Evaluation of BIPV and BAPV Systems ”,
Proceedings of the EUPVSEC, 2021, DOI: 10.4229/EUPVSEC20212021-5DO.3.5
[49]  “Marknadsanalys balanstjänster”, Svenska Kraftnät, https://www.svk.se/aktorsportalen/bidra -med-
reserver/handel-prissattning/marknadsanalys-balanstjanster/, 2025

## Página 60

[Página sem texto extraível.]
