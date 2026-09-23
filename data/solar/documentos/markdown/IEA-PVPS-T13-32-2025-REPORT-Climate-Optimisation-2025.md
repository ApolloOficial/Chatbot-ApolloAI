# IEA-PVPS-T13-32-2025-REPORT-Climate-Optimisation-2025

Fonte original: `IEA-PVPS-T13-32-2025-REPORT-Climate-Optimisation-2025.pdf`

## Página 1

Optimisation of
Photovoltaic Systems
for Different Climates
Task 13  Reliability and Performance of Photovolatic Systems
PVPS
2025
Report IEA-PVPS T13-32:2025

## Página 2

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organi sation for Economic
Cooperation and Development (OECD). The Technology Collaboration Programmes (TCP) were created with a belief that the future of
energy security and sustainability starts with global collaboration. The programmes are made up of 6.000 expe rts across government, aca-
demia, and industry dedicated to advancing common research and the application of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCPs within the IEA and was established in 1993. The mi ssion
of the programme is to “enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone
in the transition to sustainable energy systems.” To achieve this, the programme’s participants have undertaken a variety of joint research
projects in PV power systems applications. The overall programme is headed by an Executive Commit tee, comprised of one delegate from
each country or organisation member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.
Australia, Austria, Belgium, Canada, China, Denmark, European Union, Finland, France, Germany, India, Israel, Italy, Japan, Korea, Malay-
sia, Morocco, the Netherlands, Norway, Portugal, Solar Energy Research Institute of Singapore (SERIS), SolarPower Europe, South Africa,
Spain, Sweden, Switzerland, Thailand, Türkiye, United Kingdom and United States of America.
Visit us at: www.iea-pvps.org
What is IEA PVPS Task 13?
Within the framework of IEA PVPS, Task 13 aims to provide support to market actors working to improve the operation, reliability, and quality
of PV components and systems. Performance data from PV systems in different climate zones compiled within the project will help provide
the basis for estimates of the current situation regarding PV reliability and performance.
The general setting of Task 13 provides a common platform to summarise and report on technical aspects affecting the quality, performance,
reliability, and lifetime of PV systems in a wide variety of environments and applications. By working together across national boundaries, we
can all take advantage of research and experience from each member country and combine and integrate this knowledge into valu able
summaries of best practices and methods for ensuring PV systems perform at their optimum and continu e to provide competitive return on
investment.
IEA PVPS Task 13 has so far managed to create a framework for the calculations of various parameters that can indicate the quality of PV
components, systems and applications. The framework is available and can be used by the PV industry which has expressed appreciation
towards the results included in the high-quality reports.
The IEA PVPS countries participating in Task 13 are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany,
Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand, and the United States of America, and the Solar Energy
Research Institute of Singapore.

DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and publica-
tions of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual  member countries.
COPYRIGHT STATEMENT
This content may be freely used, copied and redistributed, provided appropriate credit is given (please refer to the ‘Suggested Citation’). The exception is that
some licensed images may not be copied, as specified in the individual image captions.
SUGGESTED CITATION
Friesen, G., Micheli, L. (2025). Friesen, G., Micheli, L., Jahn, U. (Eds.), Optimization of Photovoltaic Power Systems for Different Climates (Report No. T13-
32:2025). IEA PVPS Task 13. https://doi.org/10.69766/QSYC8858
COVER PICTURE
PV system located in Albuquerque US, source: Sandia/Laurie Burnham; PV system in northern Chile, source: PVRadar/Thore Müller ; PV system located at Pitea
Sweden, source: OFI/Gabriele Eder; AES Lawai Solar Project- Kauai in Hawaii, US (Photo by Dennis Schroeder, NREL 58001), source: NREL Image Gallery,

## Página 3

Task 13 Reliability and Performance of Photovoltaic Systems – – Optimization of Photovoltaic Systems for Different Climates

INTERNATIONAL ENERGY AGENCY
PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

IEA PVPS Task 13
Reliability and Performance
of Photovoltaic Systems

Optimisation of Photovoltaic Systems for
Different Climates

Report IEA-PVPS T13-32:2025
June 2025

ISBN 978-3-907281-74-1
DOI 10.69766/QSYC8858

## Página 4

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

4
AUTHORS
Main Authors
 Gabi Friesen, University of Applied Sciences and Arts of Southern Swit-
zerland, Switzerland
 Leonardo Micheli, Sapienza University of Rome, Italy
 Gabriele C. Eder, Austrian Research Institute for chemistry and technol-
ogy, Austria
 Thore Müller, PVRADAR Labs GmbH, Germany
 Jaffar Moideen Yacob Ali, Solar Energy Research Institute of Singapore,
Singapore
 Mariella Rivera, Fraunhofer Institute for Solar Energy Systems, Germany
 Julián Ascencio Vásquez, Univers SAS, France
 Gernot Oreski, Polymer Competence Center Leoben, Austria
 Laurie Burnham, Sandia National Laboratories, USA
 Christopher Baldus-Jeursen, Natural Resources Canada (CanmetEN-
ERGY), Canada
 Alexander Granlund, RISE Research Institutes of Sweden, Sweden
 Elias Urrejola, Urrejola Ingenieros SpA, Chile
 Carlos D. Rodriguez-Gallegos, RINA Consulting, Australia
 Shariq Goriawala, RINA Consulting, Australia
 Hartmut Nussbaumer, Zurich University of Applied Sciences, Switzerland

Contributing Authors
 Julien Chapon, Total Energies, France
 Anika Gassner, Austrian Research Institute for chemistry and technol-
ogy, Austria
 Ana Gracia Amillo, National Renewable Energy Centre of Spain
(CENER), Spain
 Teodora Lyubenova, European Commission, Joint Research Centre, Is-
pra, Italy
 Oktoviano Gandhi, Solar Energy Research Institute of Singapore
(SERIS), Singapore

Editors
 Gabi Friesen, University of Applied Sciences and Arts of Southern Swit-
zerland, Switzerland
 Leonardo Micheli, Sapienza University of Rome, Italy
 Ulrike Jahn, Fraunhofer Center for Silicon Photovoltaics, Germany

## Página 5

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
5
TABLE OF CONTENTS
 Introduction ................................ ................................ ................................ .................... 12
 Climate classification ................................ ................................ ................................ ..... 13
 Climate specific module energy yield ................................ ................................ ............. 14
3.1 Climatic specific module energy rating (CSER) ................................ .................... 16
3.2 Climate specific performance loss rates (PLR) ................................ ..................... 21
3.3 Case studies: Climate specific technology benchmarking ................................ ..... 24
 Optimisation of module/system design for Cold & Snowy Climates ...............................  26
4.1 Cold & snowy climates ................................ ................................ ......................... 26
4.2 Stressors and typical problems (cold & snowy) ................................ ..................... 29
4.3 Best practice and mitigation strategies (cold & snowy) ................................ ......... 34
4.4 Case studies: Bifacial system at high altitude and high latitude ............................ 40
 Optimisation of module/system design for Hot & Dry Climates ................................ ...... 45
5.1 Hot & Dry climates ................................ ................................ ................................  45
5.2 Stressors and typical problems (hot & dry) ................................ ........................... 46
5.3 Best practice and mitigation strategies (hot & dry) ................................ ................ 50
5.4 Case studies: Cleaning strategies for Southern Spain and Negev Desert. ............ 56
 Optimisation of module/system design for Hot & Humid Climates ................................ .. 59
6.1 Hot & Humid Climates ................................ ................................ .......................... 59
6.2 Stressors and typical problems (hot & humid)................................ ....................... 60
6.3 Best practice and mitigation strategies (hot & humid) ................................ ........... 63
6.4 Case Studies: Module Technology Selection ................................ ........................ 68
 Conclusions ................................ ................................ ................................ ................... 72
References ................................ ................................ ................................ ........................... 74

## Página 6

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

6
Acknowledgements
This paper received valuable contributions from several IEA-PVPS Task 13 members and other
international experts. Many thanks to:
This report is supported by the Swiss Federal Office of Energy (SFOE) under the contract no.
SI/502398-01.
This report is supported by the Austrian Federal Government, represented by the Austrian Re-
search Promotion Agency (FFG) under contract no. FO999908094.
This report is supported by the German Federal Ministry for Economic Affairs and Climate Action
(BMWK) under contract no. 03EE1120B.
This report is supported by Sole4PV, a project funded by the Italian Ministry of University and
Research under the «Rita Levi Montalcini» Program for Young Researchers (2019 call).
This report is supported by the Swedish Energy Agency under contract no. 177609.

## Página 7

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
7
List of abbreviations
Al-BSF Aluminium Back Surface Field
AOI Angle Of Incidence
BOM Bill of Material
CAPEX Capital Expenditure
C-AST Combined-Accelerated Stress Testing
CdTe  Cadmium Telluride
CINEA Climate, Infrastructure and Environment Executive Agency
CIS Copper Indium Selenide
CONUS Contiguous United States
CSER Climate-specific energy rating
DNI Direct Normal Irradiance
ECA Electrically Conductive Adhesive
EEIM Energy Efficiency Index
EPREL European Product Registry for Energy Labelling
EQE External Quantum Efficiency
ER Energy Rating
EVA Ethylene Vinyl Acetate
EY Energy Yield
FEA Finite Element Analysis
FF Fill Factor
GCR Ground Cover Ratio
IEA International Energy Agency
IEC International Electrotechnical Commission
IP Ingress Protection
Isc Short-circuit current
KGPV Koppen-Geiger-Photovoltaic
KPI Key Performance Indicator
LeTID Light and elevated Temperature Induced Degradation
LID Light Induced Degradation
MD Machine Direction
ML Machine Learning
mono-Si Mono-crystalline Silicon
multi-Si Multi-crystalline Silicon
NUS National University of Singapore
OPEX Operational Expenditure
PE Polyethylene

## Página 8

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

8

PERC Passivated Emitter and Rear Contact
PET     Polyethylene terephthalate
PID Potential Induced Degradation
PLR Performance Loss Rate
PO Polyolefin
PP Polypropylene
PV Photovoltaics
PV CAMPER PV Collaborative to Advance Multi-climate Performance and Energy Re-
search
PVCZ Photovoltaic-Climate-Zones
RTC Regional Test Center
SABs Sub-Aerial Biofilms
SERIS Solar Energy Research Institute of Singapore
SLIPS  Slippery Liquid-Infused Porous Surface
SoG Slope of Ground
SSER Site-Specific Energy Rating
STC Standard Test Conditions
STDev Standard Deviation
T98 98th percentile of the module temperature distribution
TCEP Tracking Clean Energy Progress
TD Transversal Direction
TOPCon Tunnel Oxide Passivated Contact
UV Ultraviolet
Voc Open circuit voltage

## Página 9

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
9
EXECUTIVE SUMMARY
The impressive worldwide growth in installed photovoltaic (PV) capacity is mainly driven by cost
reductions and progress in cell and module technology. This growth is also advanced by increas-
ing global energy demand and the urgent need to combat climate change and reduce depend-
ence on fossil fuels. This has led to PV systems recently being built in harsh climates and becom-
ing economically attractive where they were not previously a viable option. Deserts and tropical
zones, as well as cold and snowy regions - once considered either challenging or not affordable
for energy production - are today recognised for their significant PV potential. These areas offer
high or at least seasonal ly favourable solar irradiance levels, which can lead to consistent or
enhanced energy production.
Large-scale PV deployment in desert climates like the Middle East, North Africa, Northern India,
and the Atacama Desert, where high irradiance levels and vast land spaces are available, started
already in the early 2000s. In recent years, driven in part by the introduction of bifacial modules,
the PV market has also expanded rapidly to latitudes above 40°N, such as the North of America,
Europe, and Asia. More recently, PV at high altitudes, such as in the European alpine countries
as Switzerland and Austria, where space for ground-based systems is limited and an increase in
winter production from renewables is envisaged, has gained interest. The tropical PV market has
also grown, driven by rising energy demand and an increasing commitment to renewable energy,
combined with consistent daily sunlight near the equator. However, the scarcity of land has fa-
voured the installation of PV on buildings or floating PV over utility -scale ground-mounted sys-
tems.
The increasing deployment of PV installations in these very different geographical regions pre-
sents numerous challenges in design, commissioning, and operation. Therefore, climate-specific
strategies are crucial to address environmental stressors affecting energy yields, module lifetime,
and system efficiency. While the design and operation of climate -specific PV systems have pro-
gressed, research and innovation must continue to enhance the efficiency, durability, and cost -
effectiveness in a wider range of e nvironments. The goal is to ensure that PV can be a reliable
energy source regardless of local weather patterns or environmental challenges.
This report specifically explores strategies for enhancing the performance and reliability of PV
systems in harsher climates: 'Cold & Snowy', 'Hot & Dry', and 'Hot & Humid'. Guidance is provided
to PV system developers on the selection of the most suitable PV module technology by as-
sessing theoretical and real-world energy yield data, performance losses and degradation rates
across different climates. The key climate-specific environmental stressors and existing mitigation
strategies are reported. Details are given for optimising module and system design for each en-
vironment, starting from the site assessment, followed by the component selection, and finally the
system design. Case studies showing practical approaches and experience to mitigate risks and
optimise performance for each climate are presented.
One of the aspects to be considered at the beginning of a PV project design is the selection of
the best PV module technology for a specific climate. The implementation of the IEC 61853 PV
module energy rating (ER) standard series IEC61853 provides the end-users with an easy and
repeatable method for comparing different products for their energy yield. In addition, it delivers
all relevant PV module parameters to increase the accuracy of energy predictions and foster in-
novation. It can be used by module manufacturers to maximise the energy yield, and not just the
efficiency, of the various PV cell and module technologies for different climatic conditions. The
increasing number of ER -related publications and the ongoing efforts to introduce a European
Energy label for PV modules, described within this report, demonstrates the growing interest and
need for standardised and climate-specific energy yield assessment tools.

## Página 10

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

10
However, the ER as present today does not give any indication about the long -term reliability of
a PV module, which depends on many other aspects such as the bill of material (BOM) and
manufacturing process. The degradation rate expressed in percentual power loss per year is
needed to determine the payback time and lifetime energy production of a PV project. The inclu-
sion of the degradation rate of PV modules into the ER concept however still represents a bottle-
neck. In the absence of a standardised approach to assessing the PV module degradation rate,
the de-rating information (rate and years) stated in the power warranties are currently used. These
are however mainly representative f or moderate climates and do not reflect real degradation
rates. For example, tropical regions typically show higher degradation rates, whereas colder cli-
mates show lower values. How to assess climate-specific degradation rates and include them in
the current energy rating approach is still under discussion within the research community.
Understanding PV losses and planning adequate mitigation strategies require a good knowledge
of the climate- or site-specific stressors. These start with site assessments, which can be carried
out either through specific field campaigns, such as deploying sensors in the field, by collecting
data from nearby PV installations, or by analysing satellite/re-analysis data. The early identifica-
tion of stressors is crucial for all subsequent phases, from the selection of the components through
the system design up to the definition of the most cost -efficient O&M strategy. Based on this
information, a conscious selection of PV system components and of PV module types is possible.
In cases where knowledge about site-specific requirements and/or the availability of climate-spe-
cific PV modules is lacking, standard products are often deployed with a high risk of under -per-
formance or high susceptibility to failures. For instance, the failures occurring in the first desert
installations highlighted the need to develop PV encapsulants which can withstand the high irra-
diation at increased temperatures of that environment. Furthermore, the push for cheaper mod-
ules has driven the trend toward larger PV modules with thinner glass, cheaper encapsulants and
backsheets, and reduced frame thickness, which a re nowadays increasing the degradation and
failure rates in harsh environments.
While existing climate-specific testing procedures are described and discussed in more detail in
a dedicated IEA PVPS TASK 13 Report ‘Accelerated testing - combined vs. sequential testing
and inclusion of specific load situations’,  this document gives recommendations on the need to
select PV modules with known BOM and tested for the specific climate in which they will be in-
stalled. Solutions like thicker front glass in glass/glass modules, innovations in module design like
new frame geometries, micro-crack-resistant cell interconnection technologies, or encapsulants
with lower glass transition temperatures  - such as POE or silicone  - improve resistance to me-
chanical stress in harsher environments. Special coatings, such as anti-soiling or heat-dissipating
coatings for deserts, snow-repellent coatings for cold climates, or corrosion-resistant coatings for
humid environments, are used or under investigatio n. Although promising, further studies are
needed to prove their durability and cost-effectiveness.
Often, mitigation measures aimed at addressing one issue can inadvertently exacerbate another,
making it essential to conduct thorough testing or gain a deeper understanding of actual load
conditions to identify the most effective solution. For instance, frameless  modules are designed
to shed snow more efficiently but have a lower mechanical stability and vice versa. The choices
in the system design influence the type of modules and components which can be used. Climate-
specific system design is often the k ey to further reducing the risks of underperforming PV sys-
tems. The orientation of PV modules and mounting structures play not only a crucial role in per-
formance but can also impact the reliability and lifetime of a system. Mounting structures in cold
and snowy regions are typically the most complex and costly, due to high structural demands and
the need to manage large snow loads and ice formation.

## Página 11

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
11
Soiling is one of the main factors affecting performance, degradation, and system design , alt-
hough of very different origin for the three climates . While dust dominates soiling in hot & arid
locations, snow is predominant in cold & snowy and biological contamination is a main concern
in hot & humid locations. Soiling loss modelling is increasingly employed to predict and mitigate
soiling-induced energy losses, though accurately isolating soiling effects remains a challenge. In
hot and arid climates, systems must be designed to facilitate cleaning, with requirements varying
based on the selected business model. In equatorial locations, soiling losses can be so severe
that steeper-than-optimal tilts may be preferable to reduce accumulation, despite the lower irra-
diation. In cold climates, high tilt angles and sufficient ground clearance help minimi se snow ac-
cumulation and shading, while snow fences and snow transport simulations further prevent un-
wanted build-up. The table below provides an overview of stressor s, their effects in different cli-
mates, and mitigation strategies, described in more detail within the report.
Table 1: Climate specific stressors, failures and mitigation measures.
Stressors Failures   Cold & Snow Hot & Arid  Hot & Humid Mitigation Measures
Low temperatures Embrittlement of
materials, cracking of
encapsulant and sol-
der joints
high - -
Use of flexible encapsul-
ants and back sheets
Extreme tempera-
ture fluctuations
Thermal cycling
cracks (solder joints,
inter-connections)
low-medium low-medium low-medium
Use thermally stable ma-
terials, reinforced inter-
connections
Mechanical Stress
(Snow, Ice, Wind,
Sandstorms)
Glass breakage,
frame deformation,
cell cracks, (severe)
power loss
high
(snow load)
high
  (sandstorms) -
Strengthened module
frames, thicker glass, spe-
cial coatings, smart track-
ing (for wind or snow)
UV Exposure Backsheet cracking,
encapsulant yellow-
ing, loss of adhesion
low-medium
(high altitude) high low-medium
UV-resistant cells, back-
sheet and encapsulant
materials
Moisture Ingress &
Humidity
Corrosion (junction
box, interconnec-
tions), delamination
low-medium
(frost) - high
Edge sealants, high bar-
rier backsheet, improved
lamination techniques,
moisture resistant cells
High Operating
Temperatures
Hot spots, mi-
crocracks, encapsul-
ant degradation
- high medium
Optimised ventilation,
high-temperature-re-
sistant encapsulants
Soiling Power loss, surface
degradation, hot
spot high
(snow load)
high
(dust, sand)
high
(biofilm)
Frameless modules, self-
cleaning coatings, sched-
uled cleaning, tilted in-
stallation to minimise ac-
cumulation of snow or
dust
Salt Mist  Corrosion, electrical
insulation failure, PID - High
(coastal)
High
(coastal)
Anti-corrosion coatings,
PID-resistant materials,
sealed junction boxes
This report aims to raise awareness about the risks associated with specific stressors and high-
lights how developing climate-specific strategies is essential to enhance the reliability and cost -
effectiveness of PV systems worldwide. It shows how innovation in module design, adaptation of
bill of materials, and system configurations can support the further deployment of PV systems in
harsher climates. Experience with climate -optimised PV modules is still limited, requiring more
field data and lessons learned to be exchanged within the PV community.

## Página 12

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

12
 INTRODUCTION
In 2022, solar PV passed the threshold of 1  TWp of installed capacity worldwide and achieved
the largest absolute generation growth of all renewable technologies. Toward the end of  2024,
the global PV capacity reached 2  TWp [1]. These major milestones have resulted in solar PV
becoming "on track" in 2023, according to the IEA's Tracking Clean Energy Progress (TCEP) [2].
As the global deployment continues, PV installations can be seen today practically in any geo-
graphical region, bringing new challenges in terms of design, operation and commissioning. The
synergy between climate and PV systems is critical, as environmental stressors, such as temper-
ature, irradiance, wind, and humidity, can significantly influence energy yields, module lifetime,
and overall system efficiency. Developing climate-specific strategies to address these challenges
is essential to enhance the reliability and cost-effectiveness of PV systems worldwide. The need
for such strategies becomes even more pressing when PV systems start showing high perfor-
mance loss as well as degradation rates [3], [4].
This report aims to offer comprehensive guidance and an overview of current strategies for opti-
mising the performance of photovoltaic (PV) systems across various climatic conditions.
Chapter 2 provides a brief introduction to common climate classification methods and outlines
the three broad categories used for the purpose of  this report: ‘Cold & Snowy’, ‘Hot & Dry’ and
‘Hot & Humid’. Chapter 3 of the report focuses on the methodologies for selecting the best PV
module technology for a specific climate. The concept of climate -specific module energy rating
(CSER) and the importance of considering climate-specific performance loss rates (PLR) are in-
troduced, together with some practical examples of where these are applied for the purpose of
technology benchmarking.
The core Chapters 4 to 6 detail strategies for optimising module and system design for each of
the three climate zones: ‘Cold & Snowy’, ‘Hot & Dry’ and ‘Hot & Humid’. First, the typical conditions
of each climate zone are described, followed by the typical stressors affecting photovoltaic power
plants in such climates and their potential consequences. The chapters present available mitiga-
tion and optimisation strategies through the different project phases: site assessment, component
selection and system design.
Site assessments are critical to minimising the impact of stressors on PV systems. The magni-
tude and the impact of the  various environmental factors need to be assessed at this stage to
ensure a comprehensive understanding of site-specific conditions. In general, assessments can
be carried out either through specific field campaigns, such as deploying sensors in the field, by
collecting data from nearby PV installations, or by analysing data available from satellite-derived
or reanalysis datasets, each with its own advantages and disadvantages.
By precisely identifying the magnitude of the stressors, stakeholders can develop and implement
effective, reliable, and cost-efficient mitigation strategies. These strategies encompass a range of
actions tailored to the specific environmental challenges, starting from the component selection,
with a particular focus on the possible module designs, and extending than to the optimisation of
the overall system design. This approach ensures enhanced system performance and longevity
while minimising operational risks and costs. As a rule, it is recommended to consider risk miti-
gation, O&M costs and performance optimisation as early as possible and to tailor the plant design
and financial planning to the specific conditions of the local site.
In the conclusion of each chapter, two climate-specific case studies are presented, highlighting
different aspects such as plant configurations, site conditions, and key performance indicators.

## Página 13

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
13
 CLIMATE CLASSIFICATION
The challenge when thinking about tailored climate -specific approaches is to define climate
zones. Recognising the weather dependencies, international standards, testing protocols, and
research methodologies have increasingly emphasised the need for robust climate classifications
to support the deployment and optimisation of PV technologies.
This can be tackled in a structured way that can help to classify climatic conditions. The most
popular way to classify climate areas is the Koppen-Geiger climate classification [5], [6], expanded
for PV technologies with the Koppen -Geiger-Photovoltaic climate classification (KGPV) [7]. The
KGPV divides the globe into six main climate categories (tropical, desert, arid, temperate, cold ,
and snow), followed by an irradiation layer that differentiates Low, Medium, High and Very High
irradiation locations. Another data -driven approach developed is called Photovoltaic -Climate-
Zones (PVCZ) [8], which focuses on climate variables most relevant to PV technologies, such as
irradiance, temperature, and seasonal variability. Additionally, emerging machine learning (ML)
techniques offer innovative approaches by uncovering complex synergies between meteorologi-
cal variables, such as temperature, solar irradiance, humidity, and wind speed  [9]. Unlike tradi-
tional threshold-based systems, ML -based methodologies can identify non -linear relationships
and hidden patterns.
Nevertheless, those are not the only systems that have been used in the industry and academia;
the International Electrotechnical Commission (IEC) has published standard s describing certain
conditions to emulate climate regions in indoor testing facilities, including hot and dry, hot and
humid, cold and snowy, temperate, and other specialised climates such as high-altitude or mari-
time regions [10], [11], [12]. Depending on the purpose of testing , these classifications account
for factors like temperature, humidity, precipitation, and irradiance, helping standardi se testing,
performance evaluation, and system monitoring across diverse geographic locations. The exam-
ple of classification for the purpose of climate-specific module energy rating (CSER) determina-
tion according to IEC 61853 is described in chapter 3.
To describe strategies for optimising the performance of PV systems in non -moderate climates,
the report is organised into three main sections, each representing a specific climate zone: “Cold
& Snowy”, “Hot & Dry” and “Hot & Humid”. For better understanding and application of the clas-
sification, in the introduction of each chapter the relation with the different threshold-based climate
classifications is given.

## Página 14

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

14
 CLIMATE SPECIFIC MODULE ENERGY YIELD
One of the steps in the design of a photovoltaic system is the choice of the PV module technology
with respect to its energy yield. Guidance is here provided on how to identify the module type/tech-
nology with the theoretical highest annual and lifetime ene rgy yield for a specific climate repre-
senting the site where the photovoltaic system is to be built , and examples are given of how the
theoretical numbers compare to real module or system data.
The energy production of a PV module over its lifespan is influenced by its initial energy yield, as
well as its performance and degradation over time. There are several approaches to assess the
expected energy yield of a PV module. Table 2 summarises these approaches, highlighting their
respective advantages and disadvantages.
Table 2: Inter-comparison of different module energy yield assessment approaches.
PV Module Performance in kWh
Scope Energy rating Energy yield simulation Energy yield measurements
Product selection/benchmarking Energy prediction for specific lo-
cation and installation
Benchmarking under real condi-
tions
Used for relative comparison be-
tween different modules to identify
the best one for a specific climate
Used for absolute comparison be-
tween modules and selection, as
well as input for the economics of
the PV project
Used for relative comparison be-
tween different modules under
real operating conditions and for
validation of energy yield simula-
tions
Module
data
IEC 61853-1 & 2 Specific to simulation tool
(e.g. datasheets, STC values, tem-
perature coefficients, IEC 61853-1
etc.)
Real field data (Pmpp, IV-curves)
Model IEC 61853-3 Specific to simulation tool
(e.g. PVSYST model, SAM model) NA
Meteor-
ological
data
IEC 61853-4 (6 reference climates) Meteorological data base
(e.g. Meteonorm, Solargis)
Measured meteorological data
Pros Fast, repeatable, uncertainties
coming from the model and the
meteorological data are avoided,
measurement uncertainties are
well known
Fast prediction of the energy out-
put for a specific location and any
system configuration, degrada-
tion rates can be simulated
Allows for technology bench-
marking under real conditions,
degradation rates are also de-
tected
Cons The CSER values do not give any
information about the real perfor-
mance, modules are compared
for 20°tilt (AZ 0°) open rack only,
degradation rates are not consid-
ered, extension to bifacial mod-
ules under development
High uncertainty, strongly de-
pendent on the used simulation
tool and meteorological data, real
degradation rates are not known,
and theoretical values must be
assumed.
Requires long-term measurement
campaigns, higher uncertainty,
not repeatable, the result is site
dependent

## Página 15

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
15

Energy Rating (ER) is a standardized method to assess PV module energy output under repre-
sentative climate conditions. It is not meant for site-specific predictions but serves to benchmark
different PV technologies under comparable conditions.  Because the ER is derived using con-
trolled lab data, a standardized calculation method and climate profiles, its uncertainty is lower
compared to field measurements (which are subject to varying and often uncontrolled real-world
factors), or energy yield s imulations (which depend heavily on site -specific inputs and assump-
tions). As the name says it is used to rate a PV module with respect to another one based on an
annual energy yield calculated according to the IEC 61853 Energy Rating standard series [13].
The KPI obtained by this approach is the dimensionless climatic specific energy rating (CSER )
which will be described in more detail in 3.1. The purpose of ER is to help the end -user choose
the module with the potentially highest energy output for a specific climatic zone. The method has
the main advantage of being easy and reproducible , but it gives no information about the real
energy output of a PV module in a specific location or installation, as it is based on a fixed mete-
orological data set and fixed module mounting conditions (stand-alone ground mounted open rack
facing the equator and 20o tilt). In this regard, the standard defines six reference climatic profiles.
System losses due to the inverters or string inter-connection and external losses due to soiling or
shading are not considered. The current version of the standard applies only to monofacial PV
modules and does not consider the degradation rate of a PV module under different climatic or
working conditions. Ongoing efforts to include these aspects, as well as studies on the uncertainty
and validation of ER , including the representativeness of the propose d reference climates, are
discussed in 3.1.
Energy yield simulation  tools have the advantage of allowing the user to input site -specific
weather data, actual orientation, expected soiling, shading scenarios and albedo, etc. Compared
to ER user-defined annual degradation rates can be applied . Potential disadvantages are  that
each tool is based on its own ‘PV module’ model and meteo rological database, increasing the
risk of unrealistic inter -comparisons. The absolute and relative accuracy of the simulations are
strongly dependent on the source and accuracy of the module input data, the model itself and the
meteorological data. Validations of the models and the use of comparable module input data are
here the key. The use of module input data from test laboratories measured according to
IEC 61853-1 and IEC 61853-2 and tools accepting these inputs and capable of simulating various
effects like the spectral effects or the angle of incidence effect increases the accuracy of the
estimated power output data.
Energy yield measurements are instead used to compare different modules under real operat-
ing conditions. The measurements allow to detect also degradation rates and under-performing
modules, but long measurement campaigns of good quality data are needed. Module energy yield
benchmarking is site and season dependent and consequently not reproducible or easily compa-
rable between test sites. Besides, a PV module outperforming another one in one location would
not necessarily perform better under other circumst ances regarding both the climatic conditions
and the mounting configuration. Examples of field data are given in chapter 3.2.

## Página 16

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

16
3.1 Climatic specific module energy rating (CSER)
3.1.1 IEC 61853 energy rating standard
The climatic specific energy rating (CSER), defined by the IEC 61853 energy rating standard
series, is a theoretical KPI, corresponding to the module performance ratio, which helps in com-
paring the annual energy yield of different modules.

Where EY M(DC)Y1 is the estimated energy yield for one module over the first year of operation
(kWh), Gref is the irradiance under Standard Test Conditions (STC) of 1000 W/m2, Pmax,STC is the
module’s power output under STC in W and H p is the total yearly in-plane irradiation provided in
Part 4 of the standard series, in kWh/m 2. For c-Si technologies, typical CSER values lie in the
range between 0.8 to 0.95.
The IEC standard series Part 1 and Part 2 describe how to measure the module parameters
required as input for the determination of the energy rating. Part 3 describes how to calculate the
CSER values for different reference climatic profiles listed in Part 4 and shown in Figure 1.

Figure 1: IEC 61853 reference climates. Monthly average global and beam (direct) horizon-
tal irradiance (W/m2) and monthly mean, maximum and minimum ambient temperature (oC)
(source: ©European Union, 2024-2025).
Detailed information about the ER approach can be found in an earlier IEA PVPS TASK 13 report
[14]. The IEC TC82 WG2 is currently working on an amendment to the whole standard series
including the extension of the scope to bifacial modules. Based on the approach elaborated within
the European PV ENERATE project, Vogt et al . (2023) [15] proposed a new methodology for
bifacial modules. A new project was launched in 2023 by the Climate, Infrastructure and Environ-
ment Executive Agency (CINEA) to further develop and validate different methodologies for

## Página 17

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
17
bifacial devices and to develop a methodology or testing sequence to determine the degradation
rate of PV modules [16].
The current IEC 61853 -4 standard [17] defines six climatic profiles (tropical humid, subtropical
arid, subtropical coastal, temperate coastal, temperate continental and high elevation), by  a da-
taset of hourly values over one year containing data of the horizontal and in-plane (20°tilt) global
and direct irradiance s, spectrally resolved global in -plane irradiance, ambient temperature and
wind speed. The average monthly values of global horizontal and direct irradiances and ambient
temperature ranges are shown in Figure 1.
The choice of these six reference climates was based on the requirement that the differences
between the estimated CSER values in the different climates should be higher than the uncer-
tainty in the estimation of the CSER, as explained by Huld et al. analysing considered KPIs at
various studies at continental scale [18], [19], [20]. The uncertainty of CSER depends mainly on
the uncertainty of the module parameters described in Part 1 and 2, which are defined through
the measurement uncertainties of the test laboratory at which the module is tested. The model
and the climatic datasets defined in Part 3 and 4, respectively, are not contributing to this if the
standard approach is followed correctly. A best practice guideline and data-set for the validation
of the CSER calculation were developed within the European Project METRO-PV [21]. Within the
same project, Herrmann et al. calculated a typical combined CSER uncertainty of ±2.3% for c-Si
modules [22]. The uncertainty is dominated by the contribution of the (G-T) power matrix (75%),
followed by the contribution of the thermal module parameters u0 and u1 (20%), the angular
response (5%) and spectral responsivity (1%). Similarly, Blakesley et al . [23], obtained an aver-
age CSER uncertainty ranging from ±1.9% to ±2.18% depending on the testing scenario.
The CSER estimated for a c-Si module using input data of irradiance, ambient temperature and
wind speed with global coverage is shown in Figure 2 [24]. However, due to the lack of spectrally
resolved irradiance at global scale, the spectral effects could not be considered in the estimation
of the CSER. Notwithstanding, as shown by Huld [19], this effect could have a significant impact
in certain regions, like high elevation areas. Therefore, for the delimitation of the geographical
distribution of the six reference climates, all effects should be considered, including the analysis
of other PV technologies as well. A recent study by Anderson [25] added spectral irradiance data
to analyse  how different PV module technologies perform across climates in the contiguous
United States (CONUS).

Figure 2: CSER of a c-Si module, estimated without considering spectral effects [24].
3.1.2 Implementation of CSER into European Energy Label
The IEC 61853 Energy Rating standard series is the base of a proposal for a European Energy
Label for PV modules. The proposal is part of the Ecodesign Directive (2009/125/EC) [26] and
Energy Labelling Regulation (EU 2017/1369) [27]. The Ecodesign establishes a framework under

## Página 18

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

18
which manufacturers of energy -using products are obliged to reach a minimum level of quality
and performance considering the energy consumption and other negative environmental impacts
occurring throughout the product life cycle. It establishes performance criteria, which manufactur-
ers must meet to legally bring their product to the market, whether produced inside or outside the
EU. It is complemented by the Energy Labelling scheme through which the consumer can recog-
nise the best -performing products. In follow-up of a feasibility analysis, carried out by the Joint
Research Centre of the European Commission  [28], [29], the proposed legislation is in the pro-
cess of being approved [30].
Instead of CSER, the Label proposes to rate a module according to its energy efficiency index
(EEIM in kWh/m2), i.e. the ratio between the estimated annual energy yield (EY) per unit area (AM,
module area in m2), which uses CSER as an input (see Table 3). As the IEC 61853 standard still
takes into consideration only monofacial PV modules, a transitional method is applied for bifacial
modules until harmonised standard or technical specification becomes available for bifacial mo-
dules [31]. Instead of using the nameplate STC power (Pmax,STC), the use of the Power at Bifacial
nameplate irradiance (PBNPI) is proposed, which corresponds to the power output of the module
obtained under irradiance corresponding to 1000 W/m2 on the module front and 135 W/m2 on the
module rear as defined in IEC 61215 -1 [32], and taking into account the power bifaciality coeffi-
cient (φPmax) according to IEC TS 60904-1-2 [33]. Ground albedo is not considered here.

Table 3: Methodology for the estimation of EEIM for mono and bifacial PV modules [32].
Energy efficiency
index (kWh/m2) PV monofacial PV bifacial

An example of the latest version of the proposed label for PV modules is shown in Figure 3. The
label aims to give information on the area specific energy yield of a module, i.e. the energy that
the PV device would generate for one year if it was installed in the representative location of each
of the three European reference climatic regions , namely, ‘temperate coastal’, ‘temperate conti-
nental’ and ‘subtropical arid’, represented in the label. The geographical distribution of the three
most relevant reference climates for Europe are based on the average yearly global horizontal
irradiation described in the transitional method [34]. The label allows consumers and profession-
als to have immediate and comparable information on the product performance for reliable pur-
chasing decision. The example label exhibits both pictograms, for monofacial and bifacial mod-
ules, while a unique icon would appear on the label corresponding to a specific PV module type.
For clarity in the example, a unique energy class for all three climatic areas in Europe is proposed.
The exact values of EEIM for the three climatic zones will be also displayed.

## Página 19

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
19

Figure 3: Example of a possible energy label for PV modules (monofacial or bifacial)
(source: ©European Union, 2024-2025).

The scale of energy efficiency classes ranging from A to G corresponds to “the best” (class A)
and “the worst” (class G) (see table in Figure 3). Additional information regarding module lifetime
degradation rate (VII) and dimensions (VIII) are also suggested. The module lifetime degradation
rate is not considered for the calculation of the EEIM, but it would be contemplated for a specific
requirement included in the Ecodesign Directive. The energy efficiency classes have been deter-
mined to stand for homogeneous distribution along the different geographic areas. The proposed
label granularity is shown in the Table in Figure 3 and expressed by EEIM threshold values. To
stimulate further technological progress, the energy classes “A” and “B” would initially remain
unpopulated. Hence, the high-quality PV modules currently available on the market would fall into
class “C” or “D”. Before energy -related products covered by energy labelling are placed on the
EU market, the products must be registered by their supp lier in the European Product Registry
for Energy Labelling database (EPREL) for public access and consultation  [35]. A link to the
EPREL database is provided via the QR code depicted on the label (see Figure 3).
Validation of the applicability of the European Energy Label standard across different geographic
regions is currently underway. The following section presents some of the initial results.
3.1.3 CSER validations
As a validation of the ER methodology, Rivera et al. [36] conducted outdoor performance meas-
urements in Freiburg, Germany. They calculated the DC Performance Ratio (the site-specific en-
ergy rating, as SSERREAL) for two types of SHJ PV modules over a year and compared it with the
site-specific energy rating (SSERMODEL) for the same location and time period using specific cli-
mate profiles, generated following the IEC 61853 methodology. The modules were tilted at 20°
and facing the equator as foreseen by the standard. The results revealed a strong correlation
between SSERREAL and SSERMODEL for Freiburg. The weekly comparison ( Figure 4) shows the
SSER values for Freiburg (green line) modelled by the methodology for the year 2022 and also
from two PV modules exposed outdoors (dashed lines) from October 2022 to October 2023, with
the standard CSER for the temperate continental climate as a reference (red line). The average
deviations of real (dashed lines) and modelled (green line) daily SSER values were around 1.8%
I
II
 III
IV
V
VI
VII
VIII
IX
X
 Module Energy Efficiency Index, EEIM (kWhm-2)
Energy Class Subtropical arid Temperate coastal Temperate continental
A > 679 > 308 > 396
B [678 – 598] [307 – 271] [395 – 349]
C [597 – 511] [270 – 235] [348 – 305]
D [510 – 427] [234 – 197] [304 – 256]
E [426 – 372] [196 – 168] [255 – 218]
F [371 – 318] [167 – 140] [217 – 181]
G ≤ 317 ≤ 139 ≤ 180

Legend: I: QR code; II: Supplier’s name or trade mark; III: Supplier’s model
identifier; IV: Scale of energy efficiency classes (from A to G); V: Module energy
efficiency index value EEI M under ‘temperate coastal’  (Northern Europe, light
yellow) ‘temperate continental’ (Central Europe, dark yellow) and ‘subtropical
arid’ (Southern Europe, orange) climate conditions, expressed in kWh/m 2; VI:
Typology of PV module: monofacial or bifacial; VII: Annual performance degra-
dation rate, expressed in %; VIII: Photovoltaic module area, expressed in m2; IX:
Climatic condition’s map of Europe; X: Regulation  number; Table: Energy effi-
ciency index (EEIM) granularity.

## Página 20

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

20
to 2%, highlighting how the ER methodology aligns well with the expected uncertainties. The
deviation with respect to the CSER highlights the climatic difference between Freiburg and the
reference climate.

Figure 4: Weekly CSER in Temperate continental (red), SSERMODEL in Freiburg (green) and
SSERREAL (dashed lines) for a year of outdoor exposure between  2022-2023 with module
manufacturer M01 (Modules M01.1 and M01.2) [36].
A further validation of the ER methodology for benchmarking of different PV technologies is de-
scribed in Rivera et al. [37], where the CSER and SSERMODEL values were compared for 3 different
locations representing temperate continental, subtropical arid and subtropical coastal conditions.
The site-specific climatic profiles were generated with data from weather monitoring stations at
Fraunhofer ISE, in Freiburg (Germany), in the Negev Desert (Israel) and in Gran Canaria (Spain).
The benchmarking study analysed 11 different monocrystalline silicon PV modules from technol-
ogies like SHJ, IBC and PERC ( Figure 5). PV modules showed standard deviations (STDev) of
CSER ranging from 0.5% to 0.7% across southern climates, and with higher deviations ranging
from 1% to 1.4% for profiles in northern regions (temperate coastal, high elevation, and temperate
continental) where high diffuse ratios and high angles of incidence (AOI) can be found. Neverthe-
less, these deviations remain within the expected uncertainty range of approximately 2% for the
methodology across all climates.

## Página 21

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
21

Figure 5: CSER (left) and SSER (right) for 11 monocrystalline silicon PV modules from
different manufacturers and a reference PV module (Mod_00). Comparing Temperate con-
tinental-Munich/Freiburg, Subtropical arid -Negev, and Subtropical coastal -Gran Canaria.
“G”: ground, “S”: satellite measurements [37].
The study demonstrated that the ER methodology effectively describes the ranking of PV modules
in different climate conditions, whereas the absolute values differ significantly depending on the
location. As an example, the PERC modules (Figure 5: ModE_05, ModC_03, ModB_02) present
the highest CSER but lower performance in high-temperature, high-irradiance conditions, which
is well correlated with their high temperature coefficients and low open-circuit voltage. Conversely,
HJT modules (Figure 5: ModF) with an overall lower performance, outstand in high temperature
high-irradiance climates due to their favourable temperature coefficients.
The study by Anderson  [25], which validated the ER approach came to the conclusion that the
IEC 61853-4 reference datasets do not represent the full range of climates where PV systems
are currently deployed in United States and an alternative approach is proposed.
Monokroussos et al. [38] demonstrated the comparability of the IEC 61853 energy rating to a
commonly used simulation tool like PVSYST, by performing climate specific simulations with the
same input parameters. Despite differences in the modelling, minor differences in mean annual
specific energy yields (<0.9%) were observed for c -Si modules. The good agreement is given
using all input parameters of the IEC  61853 Standard Part 1 and Part 2. There are some differ-
ences of how these are implemented in the calculations, which leads to differences particularly at
low irradiances. Also, spectrally sensitive devices could lead to different result s, as PVSYST is
primarily validated for c-Si modules.
3.2 Climate specific performance loss rates (PLR)
The Performance Loss Rate (PLR) quantifies the power loss over time in units of percent per year
(%/year) and it is one of the most important KPIs needed to determine the payback time and
lifetime energy production of a PV project [39]. The PLR is also a valuable diagnostic indicator for
plants that are underperforming. In absence of real data, the derating and years stated in the
power warranties are used. Numerous studies, listed at the end of this chapter, have shown that
the warranty data mainly represent moderate climates and do not accurately reflect the degrada-
tion rates observed in harsh climates (e.g., desert or alpine) or in specific environments (e.g.,

## Página 22

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

22
building integration, floating PV). Climate specific PLRs that account for such variability range
from 0.3%/year to around 2.5%/year, leading to significant yield and revenue differences for the
owners of PV systems. Uncertainties and approaches for the determination of PLRs are dis-
cussed in a former IEA report  [40]. One of the main contributors to the PLR is certainly the PV
module degradation rate - which as indicated by the following simulations and supported by sub-
sequent field studies - is influenced by the climate in which the modules are deployed.
J. Ascencio-Vásquez, in his work [41] modelled climate-specific degradation rates worldwide. The
simulations do not include temporal or external degradation factors or failure modes such as light-
induced degradation (LID), light and elevated temperature degradation (LeTID), potential -in-
duced-degradation (PID) or mechanical damage due to wind or snow loads which must be deter-
mined separately through laboratory tests performed according to the relevant IEC standards
(e.g. IEC 61215). One of the outcomes is shown in Figure 6 below, where the globe is divided
into the KGPV climate zones [7], clustering the modelled degradation rates. Hereby, the tropical
climate with high irradiation zones exhibit s the highest degradation rates with an average of
1.03%/year, while the colder areas, such as snowy and cold climates, can get below 0.25%/year
on average.
Figure 6: Distribution of degradation rates in different KGPV climate zones (the average
total degradation is indicated below in %/year). The width of each shape represents the
density of degradation rates within each zone; wider sections indicate more frequent
values. KGPV climate legend: A(tropical), B(desert), C(steppe), E(temperate), D(cold),
F(polar), K(very high irradiance), H(high irradiance), M(medium irradiance), L(low
irradiance) [41].

Even though the theoretical results are coherent with what is observed in the field, some climate
and degradation modelling topics need further investigation: (1) lack of UV irradiance measure-
ments spread around the world does not allow a representative validation of models, (2) moisture
ingress and related triggering of degradation processes, such as corrosion or delamination, need
to be understood for different interaction of materials, and (3) the understanding of degradation
mechanisms under high UV irradiation and shallow humidity exposure.
Because of this , and to validate the existing degradation models , further field data are crucial.
Field data are collected worldwide to validate the performance of mainstream and emerging PV
module technologies across different climates. A former IEA PVPS TASK 13 report [42] presented
some of the major test laboratories performing technology benchmarking in the field. Some of the
new initiatives are here presented with a focus on climate specific testing.
Fraunhofer ISE operates solar test sites that enable precise monitoring data collection, custom-
ised performance and reliability evaluations of components and systems, and benchmarking of
different module types. The available sites include the "Outdoor Performance Lab" located in
Merdingen, Germany, as one of the largest test fields for solar energy systems in Europe, as well
as additional sites in Gran Canaria, Spain, and the Negev Desert, Israel.  Studies have focused

## Página 23

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
23
on estimating degradation rates in these diverse climates  [43], [44], where monitored data has
also served as validation for degradation models. For example, Kaaya et al. [45] reported a deg-
radation rate of 0.74%/year in the arid climate of Negev, dominated by thermomechanical-induced
degradation modes. In comparison, degradation rates of 0.5%/year and 0.3%/year were observed
in maritime and alpine environments, respectively, with photo thermal degradation being more
prominent in Gran Canaria due to high UV exposure and relatively high average temperatures.
The US Department of Energy's Sandia National Laboratories oversees a network of multi-climate
field sites - so-called Regional Test Centers (RTCs) for Emerging Solar Technologies - that have
comparable instrumentation and adhere to the same technical standards for data collection. The
RTCs are of high value for both validation of new technologies and for R&D studies that illuminate
the climatic influences and design factors that contribute to PV performance and reliability [46].
The RTC program expanded five years ago when the PV Collaborative to Advance Multi-climate
Performance and Energy Research (PV CAMPER)  was formed [47], [48]. Like the RTCs, PV
CAMPER is a network of global outdoor sites spread across six continents and all major climate
zones, with members committed to common standards for data quality and availability . To date,
members of PV CAMPER have tackled R&D challenges of global interest, including soiling, meas-
urement uncertainty and albedo modelling (see Figure 7).

Figure 7: PV CAMPER cross-climate albedo study. Results of one-year albedo data: (left) -
Histogram of α for each test site together with mean (μ), median and the standard deviation
(σ), (right) - Seasonal variation, monthly average of rear/front side ratio.
Sandia has also published an early-life solar module degradation study, that examined 834 fielded
PV modules taken from different PV systems , representing 13 types from seven manufacturers
in three climates  [49]. Six of the studied modules were determined to have power degradation
rates that will exceed panel warranty limits in the future, while 13 systems demonstrated the ability
to extend their lifetime beyond 30 years. The mean degradation rate values of 0.62%/year are
consistent with rates measured for older modules. As shown in some  studies of SUPSI [50], [89],
the degradation rates are not only driven by the cell technology, but also by the BOM which can
lead to different degradation rates.
A study conducted by the TruePower TM Alliance under the leadership of the Solar Energy Re-
search Institute of Singapore (SERIS) at the National University of Singapore (NUS), investigates
the PV module performance and prediction uncertainty across varying climate zones. Identical

## Página 24

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

24
PV systems with mono-c-Si modules situated in four locations - Australia (hot and dry), Germany
(temperate), Singapore (hot and humid), and China (cold) - are analysed for the impact of climate
factors such as temperature, humidity, irradiance, and spectral variations on performance  com-
pared to the operation under standard test conditions. As shown in Figure 8, the PV systems in
the hot climates (Singapore and Australia) experience much larger performance losses because
of temperature, named here as temperature losses, compared with Germany and China. The
temperature losses in Singapore are higher than those in Australia because of the lack of winter
in Singapore, the lower wind speed (characteristic of equatorial regions) . Furthermore, the PV
modules in Singapore are installed almost horizontal (which will further reduce the wind influence
on temperature reduction). Meanwhile, the PV systems in Germany and China experience much
lower temperature losses (average of 2.2% and 4.0% respectively) and sometimes even a tem-
perature gain during winter months as the module temperature goes below that of STC  (25°C).
The lower temperature loss is the main factor of higher PR in Germany and China compared with
Singapore and Australia.

Figure 8: Monthly and Total average values of different sources of PR reduction in a) Aus-
tralia, b) Germany, c) Singapore, and d) China sites. Source (TruePowerTM Alliance, SERIS).
The magnitude of spectral losses in the Singapore location is also the largest among the four
locations, although the magnitude is much lower (average of 1.92%) than temperature losses.
Furthermore, the PV system in Singapore experienced the highest degradation rate, followed by
the systems in Australia, China, and Germany. The higher degradation rate experienced by sys-
tems in Singapore and Australia might be due to higher temperature and UV radiation (as well as
humidity for the case of Singapore).
3.3 Case studies: Climate specific technology benchmarking
The main advantages of climate-specific energy ratings and performance loss rates are: (1) to
provide end-users an easy method for selecting a product based on its energy yield, which is
essential for estimating economic revenue, (2) to increase the accuracy of energy predictions by
providing access to module parameters measured in accordance with Part 1 and Part  2 of the
Energy Rating standard and (3) to foster innovation and stimulate PV module manufacturers for
optimising PV cell and module technology  with respect to energy yield and lifetime and not just

## Página 25

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
25
efficiency and STC power. Practical examples of implementation are given here including other
energy prediction tools.
Protti at el. [51] used climate specific energy rating to study and quantify the effect of module
design parameters using Cell-to-Module simulations and by performing a sensitivity analysis with
11 different module design parameters (e.g. number of strings and cells in series, thickness and
width of interconnectors, thickness of encapsulant, cell distances etc.) to optimise the energy yield
of a half-cut cell module. The paper demonstrates how ER can assist module manufacturers in
their decision making and speed up the development of photovoltaic modules with improved per-
formance by reducing the need for prototyping and testing especially in the early stages of product
development. S. Ramesh et al. performed a similar study [52] but based on a one-diode model
and 13 different climates to study how modules with the same nominal efficiency and bifaciality,
but with varying combinations of VOC, ISC and FF, have different yields at the same operating
conditions. With this study they could quantify the energy gain obtained for the oceanic-temperate
climate by optimising ISC×VOC, in tropical-humid zones VOC and in hot arid/desert areas with high
albedo VOC×FF. This translates into a cell technology choice which favours PERC technology for
oceanic-temperate climates and HJT or TOPCon cells for hot climatic zones that require a high
VOC and respectively lower temperature coefficients. The authors highlight also how degradation
of e.g. FF will have a different effect on the yield at different locations although the underlying
degradation mechanisms and FF loss may be similar.
M. Kumari at el. [53] adds the electricity price to their analysis to estimate the regional revenue
gain by choosing modules with different temperature coefficients or anti reflective coatings. They
highlighted also how higher temperature coefficients lead to higher yields in regions where the
modules operate at temperatures below 25°C for longer periods of time over the year. The lowest
energy and revenue gains come from the antireflecting coating analysis, which was however lim-
ited to fixed latitude tilted modules. The study of Rivera et al. [37] showed how at lower tilt angles
and moderate climates, where the temperature coefficients have a lower impact, the angular
losses can dominate privileging technologies with low angular losses compared to a HJT modules
with worse angular response. In building integrated modules reaching module temperatures com-
parable to hot climate simulations, it is recommended to quantify the thermal losses.
However, it has to be highlighted here that the differences in annual kWh/kWp in today’s main-
stream silicon-based PV modules are in the range of ±2.5% or lower  [54], [55] and that techno-
logical differences in climate specific degradation rates can compensate after a few years the
initial advantage given by a better temperature coefficient. To assess the economic impact of
performance losses over the PV system lifetime, one also has to consider the price of electricity.
Micheli et al. [56] investigate the distribution and the variability of the PV revenues  for different
countries and its evolution over time, as well as when mitigation measures and lower degradation
rates have the highest impact.

## Página 26

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

26
 OPTIMISATION OF MODULE/SYSTEM DESIGN FOR COLD &
SNOWY CLIMATES
Nearly 50% of the total land area in the northern hemisphere, equivalent to 67 million km 2, is
covered with snow in a typical winter. Moreover, depending on the latitude and altitude, snow may
persist for as long as nine months a year and account for more than a third of the total annual
precipitation. Today, the economics of solar have shifted dramatically and , as a result, some of
the fastest growing regions in the world for solar are above 40oN [57], where snow is a repetitive
occurrence and a significant challenge for PV systems across North America, Europe and Asia.
Also, high -altitude PV installations are becoming increasingly important, particularly in alpine
countries such as Switzerland and Austria [58], where the availability of open space for ground -
based PV systems is limited or in conflict with other interests such as agriculture, landscape or
biodiversity. Due to the high irradiance combined with low temperatures and high albedo  when
snow is present, alpine PV systems are particularly suitable for increasing the contribution of
renewable energy during the winter months and, thus, reducing the dependence on electricity
imports. High altitude PV also has strong synergies with hydropower due to the pre-existing infra-
structure and grid connection and the greater flexibility in the management of water reservoirs
and ski resorts, which require a lot of energy.
4.1 Cold & snowy climates
Cold and snowy climates are characteri sed by consistently low ambient temperatures and, in
certain areas, substantial snowfall. In these climates, temperatures are often well below freezing
for long periods of time. This reduces heat losses from PV systems, which, although favourable
for performance, can pose a risk to long -term stability. Additionally, such climates can have in-
creased snow shading and/or long winters with reduced sun -light hours, decreasing the annual
energy yield and potential PV system profitability caused by snow covers on the modules. In-
creased mechanical stress at low temperatures can lead to an increased frequency of failures in
laminates and connectors. Chemical material (polymer) degradation, however, is drastically
slowed down at low temperatures resulting in lower overall degradation rates. Heavy snowfall and
ice accumulation add significant weight, potentially damaging modules, structures or equipment.
In such climates, precipitation in the form of snow can be abundant, and persistent snow cover
can limit access and increase maintenance challenges.
Cold and snowy climates primarily fall into two groups of the Köppen-Geiger Classification: Con-
tinental (Group D) and Polar and Alpine (Group E). Within Group D, the main cold and snowy
climate categories are:
• Dfa and Dfb (humid continental climates), characteri sed by cold snowy winters, with the
coldest month mean temperature below -3°C. In Dfa, the warmest month average is above
22°C, while in Dfb between 10°C and 22°C. These climates are primarily found in the
northern United States, southern Canada, Eastern Europe, and parts of northern Japan.
Precipitation is distributed relatively evenly throughout the year.
• Dfc and Dfd (subarctic climates), characterised by long, cold winters and short summers.
They can be found in northern Canada, Alaska, Siberia, and parts of Scandinavia above
the 60° north latitude. The warmest month has an average temperature between 10°C
and 18°C. Precipitations are consistently di stributed throughout the year. Dfc climate is
characterised by average temperature below -3°C in the coldest month, which can go
below -38°C in Dfd.

## Página 27

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
27
• Dwc and Dwd (Monsoon-influenced humid subarctic climates), characterised by long, cold
winters and short humid summers. Precipitation is seasonal, with a distinct dry winter and
wet summer due to monsoonal influence. They can be found in northeastern Siberia,
northern China, and parts of Mongolia. The warmest month has an average temperature
between 10°C and 18°C, while the coldest month has an average temperature below -3°C
in Dwc and -38°C in Dwd.
• Dsc and Dsd (dry -summer subarctic climates), characteri sed by long, cold winters and
short and dry summers. They can be found in high-altitude regions of mountainous areas,
such as in Alaska and Northeast Canada. The warmest month has an average tempera-
ture between 10°C and 18°C, while the coldest month has an average temperature below
-3°C in Dsc and -38°C in Dsd.
In group E, the most common climate for PV installations so far has been the Tundra climate (Et),
characterised by cold temperatures year-round (maximum average monthly temperature between
0°C and 10°C). This climate is typically found in high-altitude regions, such as the Swiss Alps, the
Rocky Mountains, and the Andes. Precipitation mainly occurs as snow, resulting in extended
snow cover.
Following the KGPV climate classification, and as shown in Figure 9 and Figure 10, the cold and
snowy climates exhibit the lowest average temperatures worldwide, most of them located in the
Arctic (this study excludes the Antarctic) and a couple of other locations in the southern hemi-
sphere – notably in the Andes. Interestingly, high annual solar irradiation can be achieved in these
regions – especially in the mountains. Regardless of the solar potential, the low temperatures
also generate ice and snow, which leads to  risks for performance and reliability, as mentioned
below.

Figure 9: Correlation of latitude with an-
nual ambient temperature highlighting
the cold and snowy/polar KGPV climate
zones.

Figure 10: Correlation of latitude with an-
nual effective irradiation highlighting the
cold and snowy/polar KGPV climate
zones.

## Página 28

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

28
Figure 11 presents a map of snow loads across Europe, highlighting the regions that are the most
impacted by snow, like the Scandinavian countries at high latitudes and the alpine regions with
high altitudes.

Figure 11: European ground snow load map, resulting from the current set of available
National Annexes to EN1991-1-3 “Actions on structures: Snow loads” [59].

## Página 29

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
29
4.2 Stressors and typical problems (cold & snowy)
The stressors encountered in cold and snowy regions can be divided into three categories: (i)
main stressors that are present in all regions and occur with some regularity, (ii) site -specific
stressors, and (iii) stressors with low probability but significant impact on failure load. See stress-
ors and failures compilation for the cold and snowy climate in Figure 12.

Figure 12: Mind map of stressors and corresponding adverse effects for PV powerplants
in cold & snowy climates.
The most important stressors encountered in cold and snowy regions are snow and ice formation
accompanied by low temperatures as well as higher module temperature fluctuations compared
to lowland which can occur under certain circumstances. Some stressors are site-specific such
as increased (UV) radiation (at high altitudes or in presence of snow , which increases albedo),
strong wind conditions leading to snow drifts or low sun angles (at high latitudes). Further singular
high impact events in cold and snow y climates are extreme snowfalls or snowstorms, lightning
and freezing rain.
Concerning the long-term reliability of modules exposed to repetitive winter stress, including cold,
snow and wind loading, only a few studies exist [60], [61], [62]. Despite there are good examples
of systems in cold and snowy climates that have been functioning without issue for long periods,
as for example the system installed in the Swiss alps [63], the trend towards larger, thinner and
less robust modules driven by cost considerations is increasing the risk of higher degradation and
failure rates in harsh conditions.  Therefore, the consideration of c limate specific stressors and
mitigation measures is crucial.
The impact of the most important stressors is discussed in more detail in the following sub-chap-
ters.

## Página 30

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

30
4.2.1 Snow and ice formation
Snow is ubiquitous for PV in cold climates. Snow and its characteristics can however vary greatly.
As represented in Figure 13, individual snow crystals’ formation in the atmosphere changes with
both temperature and water saturation [64], [65]. Individual snow crystals will then adhere together
and form a porous sintered material that is undergoing constant transformation throughout the
winter, changing its properties further [66]. Snow adhesion is not the sole mechanism that inter-
acts with PV modules. Ice adhesion from meltwater, freezing rain or sleet, as well as ice accretion
such as frost can all affect modules on their own, or enable snow to adhere to a surface where it
otherwise might not [67].

Figure 13: Nakaya diagram showing the change in snow crystal structure with temperature
and supersaturation [64], [68].
The weight of the snow load primarily acts as a mechanical stressor on the modules, BOS com-
ponents, and racking system. Snow loads typically accumulate in a non -uniform manner, with
greater weight concentrated on the lower portions of the modules, including the frames, if present
[69]. Microcracks in the cells can form and progressively propagate over time. The ingress of
meltwater into module frames or other electrical components can cause the connection to the
frame (components) to burst/dissolve due to the increase in volume during freezing after several
thaw-freeze cycles [70].
Furthermore, snow coverage of a PV  module will lead to periods with little or no electricity pro-
duction. Snow both absorbs and reflects solar radiation, but in general transmitted light levels are
low, with maximum values measured between 450 nm and 550 nm. Research has shown, for
example, that as little as 10 cm of snow can reduce visible transmission at 500 nm to about 5%
of the incident irradiance and infrared transmission at 800 nm to less than 1%, with further de-
creases depending on increasing grain size and snow density [71]. Detailed information on soiling
from snow can be found in a previously published IEA PVPS TASK 13 report [72].
4.2.2 Low temperatures and thermal cycling
Low temperatures and fast temperature changes/fluctuations can lead to failures such as delam-
ination or mechanical damage of the laminate stack with strong focus on the interlayers with pol-
ymer films, encapsulant and backsheet [73]. But the electrical connection systems ( e.g., cell in-
terconnections, polymer cable sheaths and module connectors) and the inverters are also se-
verely affected by low operating temperatures, which can destroy or drastically reduce the service

## Página 31

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
31
life of the components. Despite the strong impact of low temperatures on physical and thermo-
mechanical degradation modes it must be noted that , in principle, lower ambient temperatures
slow down most (chemical) material degradation reactions [41].
The low-temperature behaviour of polymers is characterised by several key phenomena that
affect their mechanical, thermal, and physical properties [74]. The modulus-temperature curve of
polymers illustrates how a polymer's stiffness, typically measured by its elastic modulus, varies
with temperature. Generally, the curve can be divided into several distinct regions, each corre-
sponding to different physical states of the polymer [74]:
• At low temperatures, polymers are in a glassy state where the modulus is high, indica-
ting that the material is rigid and brittle. In this region, molecular chain movements are
practically frozen, and the polymer exhibits minimal deformation under stress.
• As the temperature approaches the glass transition temperature , the modulus drops
significantly. The polymer becomes softer and more pliable because molecular motion
increases, allowing for more segmental mobility.
• Above the glass transition the polymer reaches the rubbery plateau region, the modulus
stabilises at a lower level compared to the glassy state. The polymer is now flexible and
elastic, capable of significant deformation. Molecular chains have increased mobility but
are still entangled, providing elasticity.
• With increasing temperature, the modulus decreases further as the polymer transitions
into a viscous or flow state. The material behaves like a viscous liquid, with chains mov-
ing freely past one another, resulting in significant deformation under stress.
At high temperatures, materials become more ductile, increasing their impact toughness. In con-
trast, at low temperatures, certain plastics that are typically ductile at room temperature become
brittle due to reduced molecular mobility. This transition is e specially pronounced in amorphous
polymers near their glass transition temperature (Tg) – see Figure 14.

Figure 14: Ductile-brittle transition temperature curve of polymers.
Polymers with higher degrees of crystallinity are generally more brittle because the ordered crys-
talline regions restrict molecular mobility. Amorphous polymers, with less ordered structures, are
typically more ductile as their molecular chains can move mo re freely. Also, the incorporation of
additives and plasticizers can enhance the ductility of polymers by increasing the free volume and
reducing intermolecular forces, allowing chains to slide past each other more easily [74].

## Página 32

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

32
At low temperatures, encapsulants based on polyethylene (PE) copolymers ( e.g., EVA, POE,
TPO and EPE) become much stiffer. While the storage modulus value of these encapsulants
ranges between 1 to 50  MPa at room temperature, this value increases to about 1000  MPa at
temperatures below 0°C indicating a significant increase in stiffness [75], [76]. This can affect the
mechanical performance of PV modules as a stiff encapsulant cannot deform as easily to absorb
and distribute mechanical loads , resulting in higher stress concentrations in the solar cells and
interconnections. The increased stress can lead to micro -cracks or even fractures in the brittle
silicon cells, which can have adverse effects on the electrical performance of the PV module. The
metallic interconnections, which are usually made of soldered ribbons or wires as well as conduc-
tive adhesive materials, can also experience higher stress, potentially leading to fatigue and fail-
ure over time [77], [78], [79], [80].
These effects are strongly enhanced when PV modules are subjected to temperature variations
caused by passing clouds , day night variations or  seasonal temperature variations, leading to
repeated expansion and contraction of the materials (thermal cycling, TC). Over time, the re-
peated thermal cycling can accumulate fatigue damage in the cells and interconnections and the
stiffer encapsulant amplifies these stresses, accelerating the fatigue process [81], [82].
The differential thermal expansion between the encapsulant and other materials in the PV module
can also lead to delamination, where layers of the module separate, further compromising the
structural integrity and performance [81], [82].
One example of polymers exhibiting a brittle -ductile transition is polypropylene (PP). This effect
has already been observed and reported for PP based backsheets [83]. At room temperature, the
PP backsheet exhibits high plastic deformation ability. At -40°C however, strain at break values
drop dramatically (see Figure 15) and differentially in the two directions. It was concluded that PP
backsheets might have a higher likelihood of crack formation if subjected to prolonged operation
at temperatures well below 0°C (-10°C to 0°C = glass transition PP), when the backsheet shows
significant damage due to material degradation combined with high thermo-mechanical stresses.

## Página 33

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
33
0
10
20
30
40
50
MD
PET backsheet

Stress [MPa]
MD
PP backsheet
0
50
100
150
200

0 200 400 600 800 1000
0
10
20
30
40
50
TD

TD
Stress [MPa]
Strain [%]
 -40°C
  23°C
0 30 60 90 120 150
0
50
100
150
200

Strain [%]

Figure 15: Tensile test curves of PP and PET backsheets measured at -40°C and 23°C, both
in machine direction (MD) and transversal direction (TD) [83].
4.2.3 High irradiance and UV exposure
For PV systems in mountainous regions, i.e., at high altitudes, higher irradiance and UV input s
are added to the above-mentioned loads. A higher total irradiance of up to max. 1700 W/m2 was
measured at Jungfraujoch [63], which is due to the combination of the altitude effect and the high
albedo of snow-covered ground. Snow reflects up to 80-90% of the radiation in the UV range [84].
Therefore, high albedo leads to higher UV doses on the back sheets or rear side of bifacial mod-
ules which accelerates the degradation of materials or cells  [84], [85], [86]. Due to the high alti-
tude, many days with snow-covered ground and less fog [87], the total insolation can also reach
about 1600 kWh/m2/year (measured on the Zugspitze, Germany at 2656 m above sea level). In
addition, the percentage of UV insolation was higher there than in other climate zones in the world
(4.7%) [88].
4.2.4 Wind and snow drifts
The snowpack formed on the ground can be susceptible to erosion and transportation by strong
wind. Strong wind can transport snow from open and wind -exposed areas to areas with lower
wind speeds, typically the aerodynamic wake of an obstacle such as a building, roof ridge, or PV-
array [89]. This phenomenon can concentrate seemingly low levels of snowfall into a large snow
drift that can cause uneven shading, or heavy snow loads on PV modules [89]. High snow pres-
sure from the rear can also occur. These stressors can cause mechanical failures, such as glass
or cell breakage , or damage to the mounting structure  [90]. The special mounting construction
(see Figure 16) allowing for change between a steeper winter and lower summer seasonal angle
can further increase the accumulation of snow.

## Página 34

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

34

Figure 16: PV-system at Wildkogel/Austria; wrong site-selection: every winter, a snow roll
always covers the PV fields and causes severe damage; the PV plant must be relocated.
4.3 Best practice and mitigation strategies (cold & snowy)
4.3.1 Site assessment
When the question comes to the assessment of the optimal installation site, the following param-
eters must be taken into consideration, particularly for high altitudes:
• Environmental conditions: UV irradiance, snow depth, wind loads/direction, fog frequency
• Specific local conditions: snow deposits and wind drifts, albedo, terrain morphology/hori-
zon, thawing and freezing ground, geology/soil conditions, hydrology
• Local restrictions: environmental constrains, grid connection, remoteness, seasonal ac-
cessibility, glare
• Probability of catastrophic events: avalanches, rockfall, earth slides, hail, lightning
The safe installation of PV modules in mountainous terrain or remote areas often requires excep-
tionally strong foundations, mounting structures and fastenings to withstand the high mechanical
loads of the harsh environment. The transport of this heavy and bulky infrastructure to the high -
altitude locations is often associated with great challenges and costs.
Depending on the specific location chosen for the PV system, stressors such as high wind loads,
and snow drifts may occur. A thorough knowledge of the site-specific wind and snow depth con-
ditions is therefore essential. If there is no existing measuring st ation in the project area, wind
data must be extrapolated based on neighbouring stations at the expense of precision. To select
the right components and better dimension the PV mounting structure, it can be useful to install
a measuring station in advance. The maximum wind gusts and the frequency with which they can
occur must be considered. Another important aspect that must be determined for the site is the
expected snow depth, which must then be included in the design phase of the system together
with the topography and wind data.
4.3.2 Optimisation of module design and BOM
After having assessed the local conditions for the installation site, the next step involves the se-
lection of the best module-type for the cold and snowy environment. In general, the cell and con-
nection technology, the materials and thickness of the polymer embedding films and the glass as
well as the module structure/design (including the frame) can be selected for a PV module.

## Página 35

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
35
An open question remains, for example, on how the different thermal expansion coefficients of a
module’s laminates may impact module integrity over multiple winters. Similarly, not much is
known about the long -term durability of solar cells and modules with large surface to volume
ratios, although cold is known to increase the risk of cell cracks [91]. In addition, the trend toward
thinner front glass for glass/glass large format modules does not favour reliability under heavy
snow loads. Studies on this topic are underway at Sandia National Laboratories. More data exists
on the impact of module selection and system design on the performance of PV systems in winter,
with multiple studies demonstrating [92], [93], [94]  the efficacy of design choices that minimi se
snow adhesion and accelerate snow shedding.
The mechanical stability of the module is the primary requirement in cold and snowy regions,
on which the module size, glass thickness, frame selection and mounting structures have a strong
influence. One effective design choice is the use of frameless modules, which lack the phy sical
impediment created by the module frame and have been demonstrated to shed snow 50% faster
than their framed counterpart [94], [95]. In frameless modules , the snow slides off more easily
avoiding high snow loads and shading  [92], [95]. On the other hand, framed modules are me-
chanically more stable and easier to attach to the substructure. Higher glass thickness,
glass/glass configuration, modules with back rails and a reduction of the module size are some
of the available options to increase the mechanical stability of modules. Such modules are , for
example, modules with a front glass thickness of 4 mm, an area of 2 m2 and a design load of 5.3
kPa, which corresponds to a typical test load of 8 kPa . Thicker, reinforced or special shaped
module frames (e.g., larger glass surface contact area) or steel frames can further increase the
stability of modules  [96]. Special geometries of the frame which avoids snow accumulation or
facilitates melt water drainage mitigates frame deformation caused by snow loads or ice for-
mation. For example, snow clings more to a sharp edge than a smooth one. Frames with silicone-
based adhesives can resist higher loads without any frame bending or permanent damage while
the tape-based adhesives are less resistant  [97]. Finally, the mechanical load resistance of a
module depends strongly on the mounting configuration, in particular on the type, number and
position of module clamps. Module data sheets specify which mechanical loads are compatible
for which type of mounting.
Also, selection and design of the cell interconnection can increase the robustness of a PV mod-
ule in cold climates. Invisible cracks can occur more easily under high snow load conditions or
transport to remote areas. Compared to former ribbon-based modules with 2 to 4 cell interconnect
ribbons, more recent multi wire/busbar solar modules demonstrate much lower power losses due
to cell cracks. Another example, using finite element analysis (FEA), Lang et al. [77] showed that
for solar cells that are shingled using an electrically conductive adhesive (ECA), joint thickness,
joint width, and cell overlap each significantly reduce stress in both the joint and adjacent silicon
cells at low temperatures. Specifically, increasing the joint thickness from 20 μm to 40 μm reduces
stress in the x -direction by about 40% at -40°C. Increasing the cell overlap reduces stress by
approximately 23% and 25%, while joint width increases contribute to 18% and 19% reductions
at these r espective temperatures. This suggests joint thickness has the most impact on stress
reduction, while cell overlap, and joint width are comparatively less effective.
In addition, the choice of encapsulation and backside material has a strong influence on relia-
bility, including UV stability, when used at high altitudes. Encapsulation materials with a lower
glass transition such as POE or silicone polymers retain their elasticity even at low temperatures
[98], [99] which ensures that the cells are best protected against high mechanical loads such as
snow and wind in cold weather. The same is valid for backsheets, where each single backsheet
layer material must be checked for a ductile-brittle transition [83]. Also, backsheets with fewer
layers are favoured, as they provide less potential for delamination, especially as t he adhesive
layers within laminated backsheets are susceptible to degradation.

## Página 36

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

36
Some last generation cell technologies like TOPCon and SHJ seem to be affected by UV in-
duced degradation [100]. It is however not clear how these test results translate from lab into the
field. Selecting modules manufactured with UV-blocking encapsulants can help mitigate UVID by
preventing UV radiation from reaching the UV -sensitive c-Si/passivation interface. A technical
specification for UV-induced degradation is under development [101].
Mitigating problems caused by snow accumulation on PV modules is one of the main concerns
in cold climates. New module types with 6 or more bypass diodes minimise the effects of snow
shadow losses. Compared to monofacial module s, bifacial modules  have the inherent ad-
vantage that the additional energy captured from the backside can promote faster snowmelt at
the module surface, even under diffuse or low-light conditions [102].
More specific snow clearing measures  are described in the following, going from passive to
active snow removal technologies. Snow repellent coatings are a topic of great interest in cold
climates not just for PV, but also for wind turbines, aviation, power distribution, heat pumps, and
ventilation. As previously mentioned, snow characteristics can vary greatly; a well performing
coating needs to efficiently prevent snow and ice adhesion, as well as ice accretion [67]. Coating
should also be durable enough to remain effective throughout the module’s technological lifespan.
For most PV applications it should also not negatively affect the PV module’s performance in anti-
reflectivity, light transmittance, heat retention, and non-snow soiling, as to not lower energy output
during periods without snow. A study from Sandia National Laboratories in the US showed initial
promise for a thin polymeric coating with high transmissivity, low interfacial toughness and
strength but its reliability needs to be evaluated over multiple winters and in different climatic
zones [103]. Hydrophobic coatings are commercially available but tend to offer little to no perfor-
mance gain, limited to certain snow conditions and can struggle with durability and degradation
[104], [105], [106], [107]. Super-hydrophobic coatings typically rely on a nanostructure that mini-
mises contact area with water droplets. They can see an increased performance [108], [109], but
suffer from poor durability and can struggle with ice accretion [110], [111], as frost can form within
the nanostructure and then increase ice adhesion. SLIPS (slippery liquid-infused porous surface)
coatings also consist of a porous nanostructure but are also infused with a lubricant that enhances
certain properties, for instance  a lipid for hydrophobicity. They have shown promising perfor-
mance for both ice and snow [112], [113], but there is concern of the lubricants retaining soiling
particles such as dirt or depleting over an extended period. Elastomer coatings have shown prom-
ising results when applied to PV [103] but require further validation across multiple locations and
winters. There are no commercially available coatings that , at the time of writing , have been
proven in literature to be truly crynerophobic for a wide range of real-world conditions and subse-
quently increase net energy output across an extended period of time [67].
Actively removing snow can in some instances be warranted  to avoid catastrophic failure, e. g.
from a rooftop-mounted installation near its snow load limit. Active snow shedding and removal
can be done either mechanically or thermically. Mechanical snow removal typically utilises tools
to physically remove snow. As snow's characteristics can vary widely, so does the suitability of
different types of tools  [105]. Using tools also introduces a risk of mechanically damaging the
modules. It is therefore in many cases only relevant to use tools as a last resort to avoid snow
loads that would otherwise risk catastrophic failure to the PV  system or underlying construction.
Snow melting solutions, thermically removing snow, are another possibility. This can be done
by either forward biasing a direct current through the modules or by installing a heating wire or
mesh on its rear side. This heats up the module and either facilitates snow shedding or complete
melting of the snow [105], [114], [115]. A PV module is not typically designed to also function as
a heater, since in regular operation a cool temperature and efficient heat transfer from the module
is desired to operate optimally. This means that the entire surface, front and back, should transfer
heat away as much as possible.  There are commercially available forward bias snow melting

## Página 37

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
37
solutions primarily meant for snow load reduction of commercial and industrial rooftop mounted
PV. This has however mostly been tested in southern Norway but not in regions with longer win-
ters yet [116]. Specifically for rooftop-mounted PV, snow melting systems could prove problem-
atic. If they become inoperable during heavy snow loads, the snow must still be removed. Densely
packed PV modules on a snow-covered roof can make it difficult to maneuver around and remove
snow from in a safe manner. In contrast to forward bias heating, external heating has been
demonstrated in a few cases applied to either the front or back surface of the module. In a study
by Tanahashi et al. [117], a copper mesh was applied to the PET backsheet of test modules under
heavy snow at 10°, 20°, and 30° tilts. Furthermore, a study by Khodakarmi et al. combined both
active and passive snow shedding methods. Resistive heating of a front side transparent con-
ducting oxide was used to cause melting at the snow-module interface combined with hydropho-
bic aluminum nanos tructures to enhance snow sliding [118]. Completely melting the snow re-
quires a lot of energy and is likely only justifiable as a means to avoid heavy snow loads and
failure, whereas melting to facilitate snow shedding would require less energy and ideally give a
net gain in energy due to the negated shading losses  [115]. Electrical heating through forward
biasing requires a DC power source and would affect the bill of materials and cost. The long-term
impact of sending a current through the module in a way that it is not designed for are yet un-
known.
4.3.3 System design
Snow, ice, and frost can stick to PV  modules at any inclination. However, the steeper the incli-
nation, the less  soiling is to be expected [119]. Snow that accumulates on tilted modules will
come off and form a pile at the bottom of the installation [120]. Depending on the ground clear-
ance, these piles can become large enough to cover the bottom module rows, thus shading them
and possibly damaging them. Module orientation also impacts the performance and reliability of
a system. With a transversely aligned (landscape) module, the frame is more perpendicular to the
falling snow, which hinders snow shedding. Module orientation influences the behaviour of a mod-
ule’s bypass diodes in inhomogeneous snow cover. Partial snow coverage typically occurs at the
bottom edge of the PV modules and therefore it is advantageous to shade as few strings of cells
as possible. For the most common bypass diode configurations, a transversely (landscape)
aligned orientation is therefore advantageous [72]. The newer module types with 6 or more by-
pass diodes, minimise the impact of the orientation choice on performance. System design should
consider the local conditions to identify the most appropriate module orientation.
The mounting structure of a PV system typically consists of the module support structure and
the poles with their anchors. The entire system must be designed to withstand the specific site
conditions. Where necessary, the structures must be adjustable and modular to accommodate
steep and uneven terrain. Ground clearance is generally increased to account for local snowfall
or to allow for animal grazing or access for agricultural vehicles. The steeper the terrain, the more
difficult it is to install the system. Structures adaptable to different module sizes, modular mount-
ing, ease of transport and easy replacement of individual modules in the event of damage must
be considered . Additionally, anchorage points and typology should be determined based on
ground conditions. Different module mounting structures are used  in cold and snowy climates
(see Figure 17):
• Rack-mounted PV modules (mainly high tilt to facilitate snow shedding)
• Vertically mounted bifacial modules (east/west or cross structure)
• Rope mounted PV modules (1-axis tracking possible)
• Bifacial tracking systems

## Página 38

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

38

Figure 17: Examples of mounting structures in cold & snowy climates . Legend: Sedrun
Solar (top-left), Pitztaler Gletscher  (centre-left), Bartholet [121] (bottom-left), HELIO-
PLANT® (top-right), Next2Sun (centre-right), All Earth Renewables (bottom-right).

PV racking in cold climates  can be subject to frost heave, a phenomenon where the ground
moves upward as the soil freezes. The extent of the ground’s movement depends on factors such
as soil type, moisture content, and frost depth.  Well drained soil such as gravel and sand suffer
less from frost heave than clay and silt that can retain plenty of moisture  [122]. The frost depth
might also change with the installation of a PV systems as the modules shields the ground directly
beneath them from snow accumulation, which in turn reduces insulation against cold air and could
enable the frost  to penetrate deeper down into the ground.  Frost heave can  grip the shafts of
poles and unevenly lift the racking of a PV system and cause stress in its structure and potentially
bend racking, loosen clamps, or damage modules. Some potential ways of mitigating the impact
of frost heave are: deeper poles, if they reach beneath the frost depth they will have more traction
to stationary soil and are then more likely to remain in place; reduce traction, opt for a smooth pile
without perforations or other points of contact within the frost depth that could enable lifting; gravel
sleeve, encasing piles with well drained particles ; ground screws, unlike a pile, a ground screw
has a wider tip than shaft which if located below the frost depth can act as an anchor and resist
lifting forces on the shaft [122].
The chosen mounting structure influences strongly the snow accumulation. Snow transport sim-
ulations that consider the system and local wind conditions are therefore recommended.

## Página 39

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
39
Preventive measures can be taken to avoid undesired snow drifts. If a site has a prevailing wind
direction, snow fences can be installed in front of the PV arrays. These are designed to ensure
that a significant portion of the snow transported by the wind is deposited far away from the mod-
ules [123]. Changing some parameters in the system design of the PV array itself can also mini-
mise snow drifts but can have a negative impact on the power output of the system. Increasing
the distance between the modules and the ground should reduce snow drifts without affecting
performance, although probably at a higher cost for installation [123]. Reducing the slope and/or
module tilt or changing azimuth to align the modules parallel to the wind direction should reduce
snow drifts but also decrease the overall power output [123].
To predict how snow losses will affect the performance of a proposed PV project, or to forecast
energy production, snow loss algorithms are required. For example, meteorological parameters
that influence the removal (or shedding) of snow from PV module surfaces  may be used to esti-
mate array energy losses based on curve -fitting formulae from empirical correlations between
measured array outputs and meteorological sensors  [124]. Alternatively, threshold models em-
ploy simple limits based on the ambient temperature/ irradiance to predict snow sliding. Models
are generally based on a foundation of free-body physics for snow sliding down an inclined plane
but may also involve more complexity incorporating first principal energy balance equations to
model melting and sliding. In a recent study by Pawluk et al.  [125], 11 models were identified to
quantify energy losses due to snow. Some were validated at multiple sites, while others remain
relatively untested. Of these, the Marion et al.  [126], [127], [128], Townsend and Powers  [124],
SunPower [129], and Andrews et al. [69] models seem to be the most documented in the litera-
ture. Comparison of different snow loss models using data from utility-scale arrays in partnership
with O&M companies would be helpful to gain further experience on how snow loss modelling
can be integrated into best-practice procedures. PV software can simulate array performance to
a high degree of accuracy when irradiance, wind speed, ambient temperature and other data are
provided. In this case, the primary challenge is not simulating the array output u nder snow-free
conditions but rather finding a way to identify exactly when the array is covered. This may be
accomplished by examining camera images, the performance ratio, or monitoring the output from
inverters. However, snow effects must be clearly isolated from other confounding factors.
Compared to systems in moderate climates, at high altitudes or latitudes factors such as in-
creased or low solar irradiance, high albedo, low ambient temperatures, and the potential use of
bifacial modules require inverters to be sized differently.  High latitude systems often experience
a higher energy share at irradiances greater than 1000 W/m2 than low altitude systems, while cell
temperatures can be below STC (25°C). Depending on their specific situation, high-latitude sys-
tems might see either higher or lower relevant irradiance peaks. The higher the share of energy
at irradiances above 1000 W/m2, the smaller the DC/AC ratio (sizing ratio) should be chosen. For
low latitude PV systems, the sizing ratio is often around 1.1 to 1.2. Especially for high latitu de
systems, the sizing ratio is normally chosen at 1.0 or even below.  Besides the energy yield, the
maximum short-circuit current capacity of the inverters should be taken into account when select-
ing the inverter for high altitude or latitude systems. As the maximum input short circuit current of
an inverter must not be exceeded at any time, extra high irradiances must be considered when
planning these systems. Measurements have shown peak irradiances exceeding 1600 W/m2 for
high-altitude systems.

## Página 40

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

40
4.4 Case studies: Bifacial system at high altitude and high latitude
4.4.1 Case study 1: Optimisation of winter yield in the Alps
This chapter provides an overview of various simulation results for bifacial PV systems conducted
for an alpine location in Switzerland [130]. Key parameters such as Ground Cover Ratio (GCR),
azimuth, module tilt, and Slope of Ground (SoG) were systematically varied and analysed (Figure
18 and Table 4). The simulations were performed using the PVsyst software tool version 7.4.6.

Figure 18: Systematic analysis of the System design.
A uniform PV system with adjustable azimuth, GCR, and SoG parameters was utili sed for the
simulations. The design consists of 10-module tables arranged in eight-table rows across 40 rows.
The Swiss alpine location “Davos Totalp” at 2470 m.a.sl. was chosen as site for the simulation,
using weather data of Meteonorm 7.3 and horizon profiles relevant to the simulations, but without
considering the specific topography.
Table 4: Analysed parameters and parameter settings.
Simulation
Batch
Horizon Con-
sidered? GCR Azimuth [°] Module
Tilt [°]
Slope of
Ground [°]
Number of
Simulations
1 Yes 0.5 – 1.3 (0.1;
step size)
-90 – 90 (45;
step size) 60, 75, 90 0 – 40 (10;
step size)
675
2 No 675

The parametric study varies parameters from  Table 4, with each combination simulated for one
year at hourly resolution (675 simulations per batch). Each batch is also recalculated without a
horizon profile for broader applicability.
Simulations using Meteonorm data show that the global irradiation in Davos Totalp is ~50% higher
compared to typical Swiss location in the lowlands. Bifacial modules were utili sed in the simula-
tion, with albedo values set to 0.8 from November to May and 0.2 from June to October.

## Página 41

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
41
Simulation Results
To evaluate the performance of the configuration, the "specific energy yield" (kWh/kWp) and the
"energy yield per area" (kWh/m2) were employed. Exemplary results for specific yield at an
azimuth of 0° are presented in  Figure 19. Similar analyses were performed for an azimuth of  -
45°/45° and -90°/90°. In all cases, the energy yield per area was included (not shown here).

Figure 19: Simulation results for annual specific yield at an azimuth of 0°.
Higher SoG enables the use of an increased GCR without reducing specific yield due to the
reduction of self-shading of neighboured module rows with increasing SoG. The highest annual
yields were achieved with module tilt angles of 60°.
Figure 20 provides an overview of the systems with the highest and lowest shares of specific yield
during the winter months (October – March).

Figure 20: Winter energy yield percentages of the simulated systems.
The simulation results confirm the expected trend that systems oriented closer to the south
orientation exhibit a higher winter share of specific yield. The highest winter share was achieved
by a vertically installed system facing south with a ground slope of 40°. The annual yield maximum
is achieved for a module tilt angle of 60° for south-facing systems.

## Página 42

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

42
4.4.2 Case study 2: Lessons learned from East-West facing bifacial PV systems at
high latitudes
This chapter provides an overview of field experience with vertical bifaci al systems at high
latitudes, where the extreme sun angles and long winter months are to be taken into account.
The vertical East-West configuration has the advantages of potentially catching the light under
low sun elevations and a wide range of solar azimuth angles in the summer as well as the reflected
light from snow covered ground and minor snow coverage of modules in the cold seasons.
Studies show that PV systems with vertical East-West mounted bifacial modules has virtually the
same annual production as south -facing latitude tilted bifacial modules, but with an energy
production profile which matches better the typical grid load profiles [131]. The paper of E. Tonita
[132] describes how row spacing affects system performance comparing southfacing fixed -tilt,
horizontal single-axis tracked, and East–West vertical configurations for North American locations
at latitudes of 17 ̊N up to 75 ̊N.
Figure 21 shows an example of a vertical east/west bifacial pilot system built in Northern Sweden
where snow depth typically does not exceed 1.5 meters, but is present for a long period of the
year [https://sunnagroup.com/en/project/lilla-norrskenet/].

Figure 21: Vertical bifacial 90 kWp PV system (Lilla Norrskenet) in Northern Sweden with
pictures showing natural snow accumulation around the vertically mounted PV modules
and the map of the last day of snow cover in Sweden from the SMHI (Swedish Meteorolog-
ical and Hydrological Institute).
The system aims to study the potential for electricity production and profitability of large vertical
solar parks in Norrland (Northern Sweden region) in conjunction with hydropower stations of the
region and to test the mounting configuration and related snow losses and gains under real
operating conditions.
The vertical configuration offers clear advantages due to its resilience (natural shedding) against
snow-related losses. However, it introduces new challenges in mounting structures, particularly
regarding wind loads and snow drifts. Vertical panels can create wind barriers, causing snow to

## Página 43

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
43
accumulate on the ground near the base of the system. Over time, the drifted snow can become
substantial and may block sunlight from reaching the lower sections of the panels or nearby rows
in a solar farm. Local snow depths and wind conditions must therefore be well known. Figure 21
shows an example of how, under optimal conditions, the vertical configuration favours the snow
accumulation away from the modules  due to wind scouring caused by aerodynamic snow drift
effects. The pilot system combines strings with East-West and West-East orientated bifacial
modules of high bifaciality (>80%). Figure 22 shows the energy production during two different
days of the year. The production curve follows the consumption demand with peak in morning
and afternoon and with highest production at times with generally higher electricity prices.
Shading losses are obs erved. This leads to a slightly lower power production compared to a
closeby south facing tilted power plant, but with production starting earlier in spring.

Figure 22: Daily production profile of 4 strings within summer (left) and winter (right) of
solar parks in Norrland, Sweden.
Figure 23 on the left shows a detail of the mounting frame of the pilot system. The vertical
configuration of half-cut cell modules, with junction boxes and cables in the centre, encourages
snow accumulation. In addition, snow tends to accumulate along the lower edges of the frames.
Both issues contribute to electrical loss and potential structural damage if the frames and cable
routing are not properly designed. The landscape configuration together with the use of unframed
modules would mitigate electrical losses caused by snow, but little experience is available in such
environments.

Figure 23: Portrait (vertical) mounting configuration in pilot system compared to landscape
(horizontal) configuration.

## Página 44

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

44
In general vertical racking systems are more expensive and less readily available but are gaining
traction with new products emerging on the market  and the more recent adoption of vertical
configurations in agrivoltaics. On the rig ht, Figure 23 provides an example of a horizontal
mounting configuration for frameless modules from Next2Sun.

## Página 45

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
45
 OPTIMISATION OF MODULE /SYSTEM DESIGN FOR HOT & DRY  CLI-
MATES
Hot & dry climates offer large areas with high solar irradiation levels. These have led to the in-
creasing development of large-scale projects in regions such as the Middle East, North Africa,
North India, and the Atacama Desert, which currently stand out as new industry hotspots. Despite
the many advantages, the installation of PV power plants in hot and dry regions also presents
drawbacks. For example, t he high temperatures and dusty conditions  typical of these environ-
ments can dramatically decrease the performance of solar systems.
5.1 Hot & Dry climates
Hot and dry climates such as deserts are characterised by high temperatures and scarce rainfall.
In this environment, modules can heat up to challenging temperatures well above standard testing
conditions. With hot days and (relatively) cold nights, modules can also undergo severe thermal
cycles. In addition, these regions receive exceptionally low precipitation, typically less than 250
millimetres per year. This low precipitation, coupled with high temperatures, leads to high evapo-
ration rates which further amplify aridity.
According to the Koppen-Geiger Classification, arid and semi-arid conditions are subdivided in
four categories depending on the typical temperatures, namely BWh, BWk, BSh, BSk.
• BWh (Hot Desert Climate) represents the hottest and driest of the four climate catego-
ries. Examples of BWh environments are the Sahara Desert in North Africa or the Simp-
son Desert in Australia. BWh climates experience scorching year-round temperatures,
with average monthly temperatures exceeding 18°C. Rainfall is extremely scarce and
highly erratic. While these regions are characterised by high solar insolation throughout
the year, the lack of reliable rainfall and the presence of dust storms can pose chal-
lenges for solar panel maintenance and efficiency.
• BWk (Cold Desert Climate) experiences relatively colder winters compared to BWh. This
climate is typically found at higher latitudes or in continental interiors, further from mod-
erating influences of sea and oceans. The Gobi Desert in Mongolia is an example of this
category undergoing a high variation of thermal cycles. Precipitation remains scarce
throughout the year, though snowfall may occur during the colder months. Here, solar
energy production can be significant during the long hot summers. However, winter per-
formance will be lower due to shorter daylight hours.
• BSh (Hot Semi-Arid Climate) showcases hot summers and mild to warm winters. Re-
gions with such climate, like the Great Plains of North America or the grasslands of cen-
tral Asia, experience more precipitations than deserts, but it is still insufficient to support
extensive tree growth. Grasses and shrubs dominate the landscape, providing suste-
nance for grasing animals. BSh climates offer excellent potential for solar energy gener-
ation, thanks to the high solar insolation during the extended summers and the minimal
dust concerns. However, careful consideration of seasonal precipitation patterns may be
needed to optimise system design and ensure proper drainage around panels.
• BSk (Cold Semi-Arid Climate) experiences hot summers, but considerably colder win-
ters. Examples are the Patagonian steppes in South America or the Eurasian steppe re-
gion. Precipitation remains low throughout the year, limiting tree cover and favouring
grasslands. Compared to BWk climates, winters are less severe, allowing for a wider
range of plant and animal life to thrive. While solar energy production will be lower during
colder months in BSk regions, it can still be a viable option.

## Página 46

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

46
Figure 24 and Figure 25 show a correlation between the Köppen-Geiger-Photovoltaic classifica-
tion introduced by Ascencio-Vásquez et al. [7] with the latitude, ambient temperature and irradia-
tion. It is observed that, as expected, the steppe and desert areas, where ambient temperature
and irradiations are considerably high , are mainly located between latitudes of -40 and +40 de-
grees.

Figure 24: Correlation of KGPV climate
zones with annual average temperature
highlighting the Desert and Steppe climate
zones.

Figure 25: Correlation of KGPV climate
zones with annual effective irradiation
highlighting the Desert and Steppe cli-
mate zones.
5.2 Stressors and typical problems (hot & dry)
Physical, chemical, mechanical, or biological phenomena can produce adverse effects on one or
multiple Key Performance Indicators (KPIs) of PV power plants. Stressors specific to the Hot and
Dry climates are shown in Figure 26 and are categorised into three distinct groups: main stress-
ors, site-specific stressors, and low probability high impact events. Main stressors, such as soil-
ing, high temperatures, and thermal cycling , persistently manifest in hot and arid climates . Site-
specific stressors, such as intense UV irradiation, strong winds, and windborne sand , appear in
some locations but are absent in others. For example, in coastal desert regions (e.g., parts of the
Arabian Peninsula or Northern Chile), salty mist may be present and contribute to corrosion and
soiling. The last category groups events like strong winds and dust storms that may have severe
or even catastrophic effects.

## Página 47

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
47

Figure 26: Stressors and corresponding adverse effects for PV power plants in hot & arid
climates.
5.2.1 Soiling
Soiling refers to the accumulation of dust, dirt, and other particles on the surface of PV modules.
This contamination reduces the energy conversion and can also cause partial shading, leading
to permanent damages in case of hot spots . A previous IEA PVPS TASK 13 report provides
detailed information on both soiling losses and mitigation strategies [133].
The losses due to soiling can be particularly significant in the Hot & Dry climates, because of the
increased resuspension of dust and sand from arid soils and the lack of regular rainfall events.
For example, Li et al. [134] reported annual soiling losses as high as 20%  in Egypt and 15% in
Saudia Arabia, while most global locations experience losses closer to 5% or less. According to
a different estimate, losses can be as high as 35% in Hot & Arid locations of North Africa and
Middle East [135]. These can have substantial economic repercussions in heavily soiled loca-
tions, since one must consider both the missed revenues due to the energy loss as well as the
increased costs for operation and maintenance. A report by IRENA indeed showed that preven-
tive maintenance and module cleaning can  make up to 75% -90% of the total  operation costs
[136].
As discussed in chapter 5.3.3, given the substantial impact of soiling, planning cost-effective mit-
igation strategies at the early stages of power plant design is crucial.
5.2.2 High Temperatures
High ambient temperatures, coupled with high irradiance levels cause the operating temperature
of PV modules to rise. Depending on the temperature coefficient of the solar cell technology, this
results in higher or lower  efficiency and performance losses.  Very high temperatures can also
lead to accelerated ageing and increase material fatigue.
On top of the short - and long-term impacts on PV modules, high temperatures will also affect
inverters. Above certain temperatures (i.e ., 45°C to 60oC), indeed, depending on the manufac-
turer and inverter design, the inverters will start limiting the power conversion to prevent further
damage to the power ele ctronic devices. Figure 27 shows a real example of central inverters

## Página 48

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

48
running in Texas, USA, where ambient temperatures can reach 50o Celsius, forcing the inverters
to downtime for safety reasons.
Experience also shows that high temperatures, and extreme temperature cycles (discussed in
the following section) can induce failures into batteries, which can cause may cause tracker mal-
functions or blockages, introducing additional performance losses.

Figure 27: Visualisation of measured and modelled active power of an inverter suffering
from strong thermal derating (Source: Univers).
5.2.3 Thermal Cycling
Thermal cycling refers to high temperature variation, which induces thermo-mechanical stresses
in the structure of PV panels. Due to very hot operating temperatures during the daytime and
quite low temperature s at night, PV modules and structures in Hot & Dry climates experience
mechanical stresses that can lead to delamination and material fatigue. Adothu et al. [137] listed
several failures that thermal cycling can induce in desert climates due to the different thermal
expansion coefficients of PV components. These include, for example, finger and interconnect
breakage, ribbon interface and cell cracks, and delamination [138].
5.2.4 Salty Mist
In addition to these chronic stressors, PV power plants in hot and dry climates occasionally face
site-specific stressors. Many of these climates are found in coastal areas, where the atmosphere
is rich with various salt components. Near the sea, salty mist induces high humidity every night.
For example, the relative humidity can be higher than 90% in the Arabian desert, while  the Ata-
cama Desert experiences nearly 100% relative humidity due to the Camanchaca , a daily west-
east wind from the sea. This moisture, combined with fine dust containing a high salt concentra-
tion leads to detrimental corrosive reactions [139].
High humidity can favor the ingress of water vapor in the modules, and this can deteriorate the
electrical insulation and degrade other components [137]. Additionally, salt-mist can corrode PV
systems components, e.g., frames, mounting system and silicon adhesives that seal the edges
of the PV modules  [140]. Furthermore, research suggests salt mist c an accelerate degradation
processes such as potential-induced degradation (PID) due to erosion and penetration of salts
(e.g., sodium ions) into the encapsulant, so far just tested at small scale under experimental con-
ditions [140], [141].

## Página 49

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
49
Salty mist can also worsen the soiling loss. Kazem and Chaichan [142] conducted a study of six
sites in a coastal area of Oman, where the composition of dust particles showed high concentra-
tions of sodium salts, calcium, and magnesium oxides. They found that, due to the high relative
humidity at night, a layer of dew formed, reacting with dust components on the surface of PV
modules and dissolving the salts. This enabled the salts to enter cracks, and , after the water
evaporated after sunrise, the remaining salt and sulphates formed a solid layer adhering to the
surface. This layer prevented sunlight from reaching the cell and increased its temperature.
5.2.5 UV Irradiance
UV radiation significantly impacts the degradation of polymer materials in PV modules. The ultra-
violet (UV) region, spanning from 280 to 400 nm, accounts for approximately 4.6% of the total
solar power under reference conditions . Despite this small fraction, UV photons possess high
energy capable of causing significant damage to polymeric materials used in PV modules. High-
energy UV photons, particularly in the UVB range  (280–315 nm) cause bond scission, breaking
down carbon-carbon and carbon-oxygen bonds within the polymer chain [82], [143], [144]. This
leads to the formation of free radicals and subsequent  auto-accelerated photo-oxidation. As a
result, embrittlement and discolouration of the affected polymers can be observed. Although UVB
constitutes only about 1.5% of the UV region's power, its impact on polymer degradation is more
pronounced compared to UVA (315–400 nm), which makes up about 98.5% of the UV power [82].
Additionally, UV-induced degradation can cause surface cracking and delamination, further com-
promising the module’s performance and durability and leading to issues such as moisture in-
gress, reduced electrical insulation, and potential structural failures [145], [146]. To mitigate these
effects, manufacturers incorporate UV stabili sers and absorbers into polymer formulations, de-
velop advanced materials with better UV resistance, and apply protective coatings  [147], [148],
[149].
PV degradation may be accelerated by the detrimental mix of high-ultraviolet solar radiation dos-
age in combination with damp heat, or with salt mist or aggressive thermal cycling, which can
cause degradation of materials of such PV panels not adapted to harsh conditions [150].
In addition to polymer degradation, UV radiation can also affect the solar cells. Recent evidence
suggests that newer generations of solar cells are increasingly susceptible to UV-induced degra-
dation, because of higher vulnerability to UV deterioration of the passivation layer, compared to
conventional aluminum back surface field cells [137], [151].
5.2.6 Strong Wind
Strong wind load can occur in locations such as the Atacama Desert, where surface winds can
reach speeds above 8 m/s in summer and autumn, and between 11 m/s and 13 m/s in winter and
spring [139]. This wind load has two paramount impacts . First, it favours the transportation and
the deposition of soiling (and potentially of chemical components from nearby mining infrastruc-
tures for example). Second, it causes strong mechanical-load-stress and vibration, especially on
the tracking systems, which can lead to damages and failures . Depending on the design,  how-
ever, trackers can be used to move PV modules into a stow positions to reduce such loads [152].
5.2.7 Dust and Sandstorms
Hot & arid locations can also be subject to frequent dust and sandstorms, whose effects on PV
power plants are thoroughly discussed in this report. In these events, a large amount of sand and
dust is suspended, and can have a double effect on PV modules. First, the suspended particles
lower the visibility, therefore reducing the intensity of the surface irradiance. The drop in irradiance
is particularly intense for the direct component, with attenuations in direct normal irradiance (DNI)
that can be as high as 80-90% [153]. The repercussions on the global horizontal irradiance  are

## Página 50

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

50
lower but can still result in substantial performance losses at both local and national scales [154].
Second, if the particles deposit on the PV modules, exceptionally intense soiling losses can be
experienced, which could requir e extraordinary cleaning efforts . Furthermore, one should con-
sider that dust and sandstorms can contribute to if not even accelerate the abrasion of coatings
deposited on the PV module surface [155].
5.3 Best practice and mitigation strategies (hot & dry)
5.3.1 Site Assessment
In the following section the assessment of soiling, one of the main stressors in hot & arid locations,
is presented.
If soiling losses are known beforehand, their energy and economic impacts can be included in the
preliminary analysis of a site for a new PV installation, along with the expe cted mitigation ex-
penses. Also, as later discussed in 5.3.3, the system can be designed to reduce the soiling accu-
mulation rates, and to facilitate cleaning operations. An early assessment of the soiling loss and
mitigation profits is especially important as experience shows that if cleaning budgets are defined
based on standard values, O&M operators might have a hard time ensuring top performance of
the asset while stay ing within their (usually very small) budgets. Due to the nature of contracts
signed it is usually very difficult to increase the budget locking the plant in a suboptimal solution.
In this phase, s oiling can be assessed in different ways. First, experimental campaign s can be
put in place  by deploying specific soiling sensors to the location of interest . Several sensors,
based on different technologies are commercially available, and have been discussed in a previ-
ous IEA PVPS TASK13 report [72]. However, at least 6 months (ideally 12) of data are necessary
for a preliminary assessment, which might delay the site selection and assessment process. An-
other option consists of estimating soiling at a location using the losses measured at nearby sites.
Several spatial interpolation techniques can be used for this purpose, depending on the number,
the distance and the geographical distribution of the available sites [156]. However, this approach
can lead to significant errors if only few data are available, and if the climate, the geography, or
the configuration of the sites differ  substantially. Research also indicates that this approach is
unreliable if only a single site is available more than 40-60 km from the location of interest [157].
Alternatively, soiling losses can be estimated through the analysis of historical environmental
data. The literature offers several soiling estimation models, which have also been described in a
previous IEA PVPS TASK 13 report [72]. These include the HSU model  [158], which is readily
available in the pvlib python library [159]. Models can be fed with local ground monitoring data or
with satellite or reanalysis derived data, depending on the availability [160]. Additionally, commer-
cial providers can offer tailored soiled estimations based on such data. This approach allows
reducing the time needed for the site assessment but the uncertainty associate with this estima-
tion is higher compared to that offered by a well -maintained soiling sensor. However, this ap-
proach also offers a longer -term perspective on the soiling losses, as the estimation is typically
based on multi-year datasets, rather than on a shorter experimental campaign, allowing a better
understanding of soiling seasonality and inter-annual variability.
Once soiling is estimated, a preliminary cleaning schedule, and, therefore, the associated costs,
revenues and technical requirement s (e.g. minimum row spacing), can be defined. Nowadays ,
mechanical cleanings are still the most common strategy to tackle soiling [161]. Since they have
a cost, a cleaning optimisation process must be conducted to find the most cost-effective cleaning
schedule. This involves determining the ideal frequency and methods for cleaning to maximise

## Página 51

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
51
the difference between the additional revenues due to the increase in energy output after cleaning
and the cost of cleaning. An adequately planned cleaning schedule is typically profitable, meaning
that soiling mitigation represents an investment rather than a solely maintained task. A cleaning
optimisation process typically follows the steps depicted in Figure 28.
Figure 28: Recommended Cleaning Optimisation Process (Source: PVRADAR).

Soiling is typically quantified through the soiling level, defined as the percentage of potential en-
ergy production lost due to light blockage by dust  [162]. Typically, the monthly average soiling
levels, also referred to as soiling loss factors, are required inputs for every energy yield simulation.
The general accepted soiling model suggests that the loss level gradually increases over time
and abruptly drops when artificial or natural cleanings occur. The daily variation in soiling levels
is represented by the soiling rate. While this rate can often be approximated to a linear trend , it
can also change seasonally driven by the interplay of dry and wet weather patterns. For example,
a soiling rate of 3% per month  - or 0.1% per day  - implies that an initially cleaned module  will
reach a 3% soiling level at the end of the month  if no rain or mechanical cleaning occurs. Con-
versely, as shown in Figure 29, if cleaning does take place, the soiling level rapidly decreases
and then starts raising again. The area in between the red and the blue line , multiplied by the
energy yield, expresses the energy gain achievable through cleaning. If multiplied by the electric-
ity price, this returns the economic value of cleaning.

## Página 52

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

52

Figure 29: Example of soiling levels with and without artificial cleaning, simulated with
PVRADAR software. A longer dry period stretching from March to July is followed by two
months of frequent rain. The blue line shows the soiling level if the systems is cleaned in
April by the O&M team. The red line shows the soiling level if no artificial cleaning is per-
formed (Source: PVRADAR).
In addition to evaluating the energy and economic losses due to soiling, cleaning optimi sation
requires the understanding of the cleaning costs. These depend on the size of the PV power plant
and on the cleaning technology. The latter is mainly influenced by the technical specifications of
the machines, such as cleaning speed, water , fuel consumption, and cleaning efficiency . How-
ever, the choice of the cleaning technology might not be solely based on its economics, as it must
consider its compatibility with the installation environment, the operational needs and the availa-
ble resources, such as manpower and water. The market offers a diverse range of cleaning tech-
nologies, from tractors equipped with rotating brushes suitable for both dry and wet cleaning, to
semi and fully autonomous cleaning robots.
5.3.2 Optimisation of module design and BOM
The high temperatures experienced in Hot & Arid locations worsen the performance of PV mod-
ules, whose thermal degradation is expressed through the temperature coefficients (performance
drop per increase in operating temperature). Different module types have different temperature
coefficients, meaning that some technologies could therefore be more suitable for application in
hot & dry environments (see chapter 3.3). In addition, several solutions have been proposed, such
as heat spreading plates, air cooled fins, phase change materials  [163], to actively or passively
cool down PV modules, but are not yet used in large commercial applications.
In addition to initial failure modes that lead to a rapid drop in performance at the beginning of the
service life of PV modules, performance losses due to progressive aging and degradation of ma-
terials/components ("midlife failures") determine the long-term stability and profitability of PV sys-
tems in specific climate regions [164], [165]. Therefore, artificial accelerated aging tests that sim-
ulate this aging-related degradation of PV modules under specific (e.g. hot and dry; arid) stress
conditions are needed to enable climate-specific development of new PV module designs, com-
ponents and innovative material [166], [167]. Accelerated ageing test for hot and dry conditions
(Tchamber = 95°C, RH = 50%, 1200 W/m2 Xenon irradiation = simulated sunlight) result in severe
electrical degradation. Significant correlations were found between the material changes - as in-
dicated by the spectral measurements - and the electrical power loss of the test modules during
climate-specific ageing. Another test approach is the combined-accelerated stress testing (C -
AST), proposed by Hacke et al.  [11], that also includes a test sequence for desert environment
and was successfully validated by reproducing failure modes from the field like backsheet crack-
ing [168].

## Página 53

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
53
As the main stressors – apart from soiling - in arid regions are high temperatures, high tempera-
ture differences, and increased irradiation levels at low humidity levels, accelerated ageing tests
combining these stressors are used. Climate specific failures and degradation effects observed
in PV-plants in hot and dry areas are mainly related to the cells and busbars (29%), followed by
glass (22%), junction box (15%), encapsulant (11%) and backsheet (8%)  [164], [165]. By com-
paring these findings with the results of specific accelerated ageing tests  [169], [170], it can be
demonstrated that additional irradiation had a strong influence on the degradation of power and
materials. High irradiance doses ( simulated sunlight 1200 W/m2) caused high module tempera-
tures and resulted in enhanced stress for the polymeric materials: the backsheet material (PET)
showed high colour change, embrittlement and cracking, the encapsulant (EVA) exhibited high
UV-Fluorescence paired with chemical degradation as detected in the pronounced formation of
(corrosive) acetic acid. The IEC TS 63126:2020 standard describes methods to calculate an es-
timated annual module temperature distribution, depending on location and mounting conditions
[171], [172]. If the 98th percentile of the distribution (T98) is between 70° and 80°C (Level 1) or
between 80° and 90°C (Level 2), different test modifications in [32] and [173] test protocols are
recommended. For T98 exceeding 90°C, no material combinations are known to mitigate failures
in modules induced by such high temperatures. The encapsulation degradation results in subse-
quent corrosion effects and cell problems and electrical degradation. Direct evidence for the for-
mation of acetic acid and lead -acetate in the encapsulant EVA was found by TD -GC/MS and
FTIR-measurements of the encapsulant of the test modules after storage in the arid accelerated
ageing test [170], [174]. Formation of increased amounts of acetic acid in the encapsulant was
always paralleled by strong UV -F and mainly triggered by high irradiation doses which caused
increased module temperatures. For TPO and POE no such corrosion effects were observed up
to now [175]. Polyolefin encapsulation materials TPO and POE show great potential to be a valid
replacement for EVA for hot and dry climates.
As PV modules without permeable backsheets (glass/glass-types) lead to an accumulation of
acetic acid within the EVA encapsulant, the corrosion effects are even stronger with this module
type. However, when polyolefin encapsulants are used, also glass/glass modules are applicable.
PV panels are typically designed for standard test conditions, and these might not adequately
account for harsh desertic conditions. This is the case, for example, of the intense UV radiation
present in desert environments. In the Atacama Desert, the total UV annual dosage reaches ap-
proximately 175 kWh/m2/year [139], while in the Negev Desert it is around 120 kWh/m2/year [176],
values substantially higher than those considered in current testing standards. For example, IEC
61730 includes a UV dose of 60 kWh/m2/year, and IEC 61215 applies a dose of 15 kWh/m2/year
[139][176]. Similar considerations have been reported for the temperature fluctuations, whose
typical values in the desert climates are not adequately reproduced in the IEC 61215 [176].
After assessing the main degradation mechanisms, Adothu et al. [137] recommended, for desert
applications, the development of modules with low-temperature coefficients, high efficiency, and
stability under both high UV light and elevated temperatures. Additionally, they highlighted the
need for thermally and UV stable back sheets and encapsulants , free of acetic acid groups and
with low water vapor transfer rates. However , it should be noted that the module selection is
typically taken on the procurement level, depending on price, availability, quality, compliance and
contracts. This means that, e ven if optimal modules for a given site were available, it might be
difficult to install them there, for example because of pre-existing long-term contracts with other
suppliers.

## Página 54

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

54
5.3.3 System Design
The design of PV systems in hot & arid locations must consider the effects of the various previ-
ously mentioned harsh stressors.
As described in 4.3.1, a first cleaning optimi sation analysis should be performed during the site
assessment phase. This must be reviewed during the design phase and then later during opera-
tion. The key task during the system design phase is to (i) identify how the system configuration
(i.e., tilt angles, tracking, etc.) affects the soiling accumulation, and (ii) facilitate s the cleaning
operation. Indeed, the selected cleaning technology might require specific changes in the layout
of the power plants. In addition, one should always try to minimise the time needed by the O&M
team to operate, for example considering the distance between the combiner boxes and the
roads.
Fully autonomous cleaning robots, for instance, require precision in solar tracker alignment to
meet strict tolerance levels, as well as adequate space for docking stations and rails . Similarly,
considerations for cleaning tractors include ensuring adequate row -to-row distance, sufficiently
levelled terrain, and sufficient space for turning around. It is very important for project developers
to discuss these requirements as early as possible with the EPC contractor and structure OEM to
avoid any mismatch. Sometimes increasing the row-to-row distance a little bit might result in much
lower cleaning cost even if it requires a slight increase in CAPEX.
When cleaning modules, it is vital to handle them with care, especially when using water. Spraying
cold water on hot modules can cause thermal shock, potentially damaging the modules and void-
ing the module guarantee. To mitigate this risk, some cleaning pr oviders might heat the water,
operate during cooler nighttime hours or employ dry cleaning methods that prevent damage and
preserve module warranties.
In some areas, water may be scarce or its usage restricted due to competing demands, particu-
larly from local agricultural communities. Transporting water over long distances can be both
costly and environmentally unsustainable. Additionally, if the available water has high hardness,
it may require treatment before use to avoid leaving residues on the modules. In such cases,
evaluating the feasibility of dry -cleaning methods may be advisable, even if they offer slightly
lower cleaning efficiency.
Beyond technical considerations, the crucial strategic question is the business model: the power
plant could either purchase and operate the cleaning system or contract a cleaning service pro-
vider. The "buy and operate" model typically involves a substanti al initial capital expenditure
(CAPEX) but can lead to reduced operational expenses (OPEX), thereby allowing more frequent
cleaning which might optimise performance. Conversely, the "service" model offers greater flexi-
bility in resource usage.
In some cases, the DC side of the power plant can be oversized compared to the size of the
inverter (inverter undersizing) to mask DC losses as those due to temperature, degradation, and
soiling. When the energy produced by the DC side of the power plant is greater than the inverter
size, “clipping” takes place [177]. During clipping, the excess DC energy is not converted into AC.
Therefore, DC losses are not visible on the AC side during clipping if they do not exceed the
difference between the energy rating of the modules and the inverter's capacity (Figure 30) [178].
However, inverter undersizing might not always completely mask the losses, leaving the need for
additional mitigation actions, as shown for soiling losses occurring in the U.S . [179]. In addition,
as the system ages, clipping becomes less frequent and, thus, a less effective loss mitigation
strategy. Furthermore, it is always important to regularly monitor the performance of the inverter
to detect any sign of temperature-induced inverter derating. Additionally, it should be considered

## Página 55

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
55
that clipping can induce higher operating temperatures [180], which may lead to higher degrada-
tion rates.

Figure 30: The effect of inverter clipping on soiling losses. (Source: PVRADAR)
The PV system design and installation methodology is a challenge in desert areas also due to
hard soil corrosion. Corrosion generated by electrochemical interaction between soil and steel
has become one of the biggest challenges for many PV plants during construction. This problem
raises serious concerns both in the acquisition of existing assets and in the developmen t and
maintenance of new facilities. The foundation of the panels using steel profiles is the most com-
mon approach worldwide due to its low co st and quick installation, and it works well if the slow
thickness loss of metallic coatings and steel under the surface is considered. Therefore, an ap-
propriate soil study must be conducted during or even before the design phase to plan an ade-
quate mitigation strategy. In general, the industry should review at which rate corrosion is occur-
ring and how it will affect the metal infrastructure and, in the long-term, their asset.
In addition to corrosion, the soil hardness also makes the installation of structures on the ground
very difficult, increasing CAPEX during the PV project construction phase as pre-drilling can in-
duce many design challenges during the installation of the foundations. Not considering or inves-
tigating this ahead of time can lead to significant cost increases, time delays, and, subsequently,
liquidated damages.
The strong winds occurring in some hot & arid locations can pose significant loads on the systems.
Therefore, when designing PV systems for desert conditions, it is essential to engineer structural
solutions that can withstand the mechanical stresses imposed by strong wind loads, particularly
on tracking systems. In the current hyper-competitive solar market, tracker manufacturers are
forced to take risks to be competitive and this can lead to reckless designs [181]. Wherever pos-
sible, smart tracking solutions can be put in place  to reduce the wind load  by stowing the PV
panels when wind speeds exceed predetermined thresholds. wind sensors and automated stow
strategies to reduce the risk of wind -related damage. However, these measures, along with the
installation of anemometers,  are not necessarily sufficient as wind-induced failures have often
been reported due to poor implementation, misconfigured thresholds, or communication issues
[152].
One should consider that any mitigation efforts will require proper monitoring as a first step. This
can be realised through specific measurements done by the O&M team, which might be effective,
even if slower, less systematic and potentially more expensive, than automatic sensors. In addi-
tion, operators may be prone to occasional human errors, particularly when involved in routine or

## Página 56

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

56
monotonous tasks. On the other hand, sensors may sometimes provide inaccurate reading, such
as when dust accumulates on pyranometers, and therefore require careful and regular mainte-
nance.
5.4 Case studies: Cleaning strategies for Southern Spain and Negev
Desert.
This section presents two examples of cleaning optimisations: one in Southern Spain and one in
the Negev desert (see Figure 31). The process is performed using PVRADAR and starts with the
definition of the most likely soiling conditions for each PV plant. This estimation is made through
the analysis of the historic environmental conditions for the period 2002-2022 and of the geomet-
rical characteristics of each facility. Subsequently, the impact on energy and revenue of multiple
cleaning scenarios are assessed.

Figure 31: Location of the example projects for the two case studies.
In these scenarios, different cleaning technologies are considered, from wet and dry -cleaning
tractors to full or semi -autonomous robots. For each technology, technical characteristics and
representative costs have been defined based on the products currently available on the market.
For each site, the result is a cleaning strategy that yields the maximum economic benefit at mini-
mal cost.

Figure 32: Direct comparison of optimal cleaning strategies for both sites , for one
particular year. The exact cleaning dates (and number) changes depending on the
expected rain patterns. “Virtual” gains and losses refer to energy that is lost due to inverter
clipping. (Source: PVRADAR)
The cleaning optimisation, whose results are summarised in Figure 32, returns that a single wet
tractor cleaning during the summer , performed by an external cleaning service provider,  is the
most cost-effective approach in Southern Spain. In this region, the low cleaning frequency yields

## Página 57

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
57
modest economic benefits.  In contrast, the Negev Desert demands a more intensive cleaning
strategy due to its harsh environment. In this example, the plant invests in three cleaning tractors,
enabling it to lower the cost per cleaning compared to relying on external services and t o utilise
the equipment year-round for a significant increase of revenue after cleaning cost.
5.4.1 Case Study 1: Southern Spain
The 30 MWp project is located in the Southern region of the country, exposed to long hot and dry
summers, followed by a higher frequency of rainfall in winter. The area enjoys abundant irradi-
ance, exceeding 1,800 kWh/m2 per year.
Soiling has a seasonal behaviour, influenced by dust storms and olive harvesting. Historical anal-
ysis shows low to medium soiling, with an average annual loss factor of 1.3%. During winter,
soiling remains below 1%, increasing from May onwards and reaching  a maximum in August of
up to 10% recorded in some years of high soiling. From September onwards, rainfall reduces
soiling to around 0.5% by the end of the year.
The most cost -effective cleaning strategy proved to be the 1 -wet tractor cleaning service. The
frequency of cleaning varied depending on the cost of cleaning, however the best time to perform
the cleaning remains fixed between July/August. The results of a cleaning optimization process
obtained using PVRADAR are reported in Table 5. This web-application optimi ses cleaning
strategies by modelling energy and economic losses and using historic dust concentration and
environmental data and considering a set of technical parameters (e.g., cleaning efficiency,
cleaning speed) and costs (e.g., labour, water, fuel). It iterates through numerous scenarios,
varying the type of cleaning s ystem (e.g., tractor, robot, manual), the number of systems, and
cleaning schedules to identify the most cost -effective strategy. Specifically, Table 5 shows the
optimal cleaning frequency for three different cleaning costs ranging from 250 to 750 EUR per
MWp cleaned. For the highest assumed cost, the optimal strategy would be to only clean in years
with especially dry summers, roughly every 5 years. For the lower end of the range, the optimum
means cleaning every year at least once and sometimes even twice.
Dry tractors and semi-autonomous robots were viable options but proved to be less economical.
Wet cleaning recovered more energy compared to dry cleaning, which justified the higher ex-
penses for water and equipment. Conversely, semi -autonomous robots requi re higher labour
costs, rendering them uncompetitive. Fully autonomous robots were also not cost -effective due
to their significant initial investment.
Table 5: Optimal cleaning strategy for Southern Spain depending on cleaning cost
(assuming an energy sales price of 60 EUR/MWh), simulated with PVRADAR.
Assumed cleaning cost
[EUR/MWp/cleaning]
Cleaning frequency
  [number of cleanings/year]
Economic benefit
[kEUR/MWp]
750 0 – 1 (0.2 avg.) 0.2
500 0 – 1 (0.5 avg.) 1.2
250 1 – 2 (1.3 avg.) 4.3

5.4.2 Case study 2: Negev Desert
The Negev Desert has extremely scarce rainfall and high solar isolation. A soiling assessment
based on historical conditions indicates an average loss factor of 16.2%, which is more than 11
times higher than the average loss found in the Spanish project. The dry season lasts from April

## Página 58

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

58
to early November and allows soiling to accumulate to values above 20%. Considering an energy
selling price of 35 EUR/MWh, the project is expected to experience revenue losses of about 200
kEUR/MWp during the 30-year lifetime.
The most cost-effective cleaning strategy for this 150 MW power plant is investing in three dry-
cleaning tractors and use them to clean the plant  10 times per year in average, depending on
precipitation. This approach provides the best balance between cost and recovered energy, de-
livering the highest economic benefit while keeping soiling losses low.
Fully autonomous robots, operated every two days, also present a profitable alternative, though
they produce about 10% less benefit compared to the dry tractor method. This frequency has
been identified as optimal after evaluating various options, considering the additional energy rev-
enues and costs associated with consumables and the lifespan of each component. The profita-
bility of this approach largely depends on the configuration of module tables that can be connected
and cleaned by each robot. For this analysis, a four-table setup was assumed, and the economic
evaluation should be reassessed for different scenarios. Implementation feasibility, including table
alignment and compatibility with robotic systems, should also be carefully considered.
Table 6: Optimal use and resulting economic benefit of dry -cleaning tractors and fully
autonomous cleaning robots for site in Negev Desert, simulated with PVRADAR.
Cleaning
technology
Nb of
cleaning devices
Cleaning
frequency
Economic benefit
[kEUR/MWp]
Dry-cleaning tractor 3 10 cleanings per
year (avg.) 128.2
Fully autonomous
Robot
1031
(1 every 4 tables) Every 2 days 114.7

## Página 59

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
59
 OPTIMISATION OF MODULE/SYSTEM DESIGN FOR HOT & HUMID CLI-
MATES
While Chapter 5 addressed the challenges faced by PV systems in hot and dry climates, this
chapter focuses on the unique issues arising from hot and humid environments. Humidity intro-
duces a new set of complications that can significantly impact the performance, reliabili ty, and
longevity of PV systems. High moisture content in the air, coupled with elevated temperatures,
creates a particularly challenging environment for solar energy installations. This chapter explores
the various ways in which hot and humid conditions affect PV systems and their components and
discusses strategies for optimising their performance in these demanding conditions.
6.1 Hot & Humid Climates
Hot and humid climate zones, typically found in tropical and subtropical regions, are characterised
by high temperatures and elevated moisture levels throughout the year. Those conditions often
come with heavy rainfall, with annual precipitation typically exceeding 1000  mm, and humidity
levels frequently above 70%. These regions typically experience minimal temperature variation,
with averages remaining above 18°C throughout the year. In such locations, the combination of
heat and moisture accelerates the risk of certain failure modes for PV modules and system com-
ponents. Corrosion, mold, and material degradation are some of the challenges to overcome to
improve PV durability in highly humid conditions. In addition, high temperatures can decrease
yield performance, reducing module and inverter efficiencies, while frequent rain and high humid-
ity increase the potential for water ingress and electrical failures [182]. Hot and humid regions can
exhibit very high irradiation profiles and be subject to occasional extreme weather events, such
as tropical storms, further amplifying the performance and reliability risk.
In the Köppen-Geiger climate classification system [6], hot and humid areas are classified as "Af"
(tropical rainforest) or "Am" (tropical monsoon). The Af climate is characterised by consistently
high temperatures around 30°C, abundant annual rainfall ranging from 150 to 1000 cm and heavy
cloud cover. The Am climate is also characterised by high temperatures, with small annual varia-
tions, and abundant precipitation, which however often exceeds that of Af zones. Both zones can
be found in the sub-tropical belt, particularly in southern and southeastern Asia.
Figure 33 and Figure 34 exhibit two illustrations that correlate weather variables (annual temper-
ature and annual irradiation) with latitude for all the globe excluding Antarctica. As shown, tropical
climates are primarily located between -20° and 20° latitude and achieve the highest annual av-
erage temperatures (higher than 20°C) but not the highest ann ual irradiation due to high cloud
coverage, frequent rainfall and other atmospheric phenomena.

## Página 60

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

60

Figure 33: Correlation of KGPV climate
zones with annual  ambient temperature
highlighting the Tropical climates.

Figure 34: Correlation of KGPV climate
zones with annual effective irradiation
highlighting the Tropical climates.
6.2 Stressors and typical problems (hot & humid)
This section explores the key environmental factors that stress PV systems in hot and humid
climates and the typical problems they cause. These environmental stressors and their adverse
effects are also visually represented in the mind map in Figure 35. They include high tempera-
tures, elevated humidity levels, intense UV radiation, frequent precipitation, and in coastal areas,
exposure to salt mist. Also, these climates often favor biological growth and are prone to extreme
weather events like tropical storms. Most of the adverse effects are associated with stressors like
heat, humidity, UV radiation, and salt spray. In contrast, low-impact stressors such as wind, pre-
cipitation, and biological growth contribute to fewer effects.

## Página 61

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
61

Figure 35: Mind map of stressors and their adverse effects in hot and humid climates.
6.2.1 High humidity in combination with high temperature
High temperatures significantly impact the performance of solar cells, by reducing their voltage
output and consequently lowering power production. While the exact impact varies depending on
the specific cell technology and module design, the temperature effect remains a critical factor in
hot climates. High humidity worsens this issue by hindering effective heat dissipation from the
modules, leading to even higher cell temperatures and further efficiency reductions. Additionally,
the accumulation of water droplets on solar panels can diminish the level of direct solar irradiation
they receive since the light is backscattered by the droplets, leading to an additional drop in power
output [183].
The combination of heat and humidity also accelerates the various degradation mechanisms in a
PV system. Hacke  et al. [184] found that high humidity can contribute to PID, especially when
combined with high system voltages and elevated temperatures. The study also revealed that
conditions exceeding 70°C and 70% relative humidity triggered water-induced chemical reactions
leading to degradation effects, such as silicon nitride deterioration and increased cell series re-
sistance. Modules in tropical Singapore were found to be more susceptible to PID than those in
subtropical and continental climates [185]. This highlights the critical influence of humidity on PID
progression. PID reduces shunt resistance and fill factor (FF), and therefore the module power
output.
Prolonged exposure to a humid environment can cause the PV module components (solder joints,
busbars and fingers) to corrode because moisture seeps into the solar cells. This trapped mois-
ture also raises the electrical conductivity of the materials, leading to leakage currents. Cracks in
the cells of modules in hot & humid locations have been found in the same place as the crack in
the backsheet [186], suggesting that moisture enters through the crack in the backsheet, deforms
the EVA and cracks the solar cells. Additionally, when water condenses between the encapsulant
and the solar cell materials, it speeds up corrosion, which can result in the encapsulant peeling
away [187].
In high-humidity environments, especially near water bodies, photovoltaic systems can experi-
ence significant drops in insulation resistance  [188], [189]. Inverters typically monitor insulation
resistance during startup and may not activate if minimum thresholds are not met. A study of a
Singapore floating PV testbed revealed frequent delayed morning startups for some systems,
resulting in notable energy p roduction losses. This effect is illustrated by the red dots in Figure

## Página 62

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

62
36, whereby despite the increasing irradiance from 7 to 8 AM, the current, and therefore power,
output of the inverter remained zero [190].

Figure 36:. Startup delay measured at floating PV in the Tengeh reservoir (Singapore) be-
cause of reduced insulation resistance. Source: SERIS
6.2.2 Enhanced dust adhesion
Humidity plays a significant role in the accumulation of dust on PV module surfaces. In regions
with high humidity, dust particles adhere more easily and strongly to module glass cover which
then requires thorough cleaning to restore the PV modules to their initial power output levels [191]
[192]. The increased adhesion of dust to the PV surface is due to the stronger capillary forces,
which prevent wind from resuspending particles [193].
In addition, high relative humidity values can favour gravitational settling, further worsening the
soiling deposition [193]. Indeed, high humidity can also contribute to the formation of stubborn
dust layers on PV module surfaces, further complicating maintenance efforts and potentially re-
ducing system efficiency  [191]. Therefore, the cumulative effect of dust accumulation in humid
conditions over time can result in substantial energy losses which happens due to reduced light
transmittance.
Dew can also have a significant impact on soiling accumulation, as it can cause cementation of
dust particles making them hard to remove by natural cleaning  [194]. Condensation should be
measured, rather than estimated from dew point and surface temperature, and can be monitored
using industrial moisture sensors. These are available at lower costs than scientific -grade tools
and were found to provide reliable resul ts when employed to characteri se condensation on PV
modules [195].
6.2.3 Biological growth
PV systems installed in hot and humid climates face unique challenges, particularly in the form of
organic growth on PV modules and other system components. These biological agents can not
only negatively impact the performance and longevity of PV installations but also increase mainte-
nance costs for PV system operators.
A study conducted in São Paulo [196] revealed insights into the formation and impact of biological
growths on solar panels. The research found that biofilms begin to develop on photovoltaic sur-
faces within a half-year period, progressively maturing over time. These formations result from a
complex interaction between airborne particles and microbial communities known as sub -aerial
biofilms (SABs). This biological fouling has substantial consequences for solar energy production,
with the study reporting a notable 11% decrease in photovoltaic cell efficiency over an 18-month
timeframe.
Another study [197] investigated the composition of soiling on photovoltaic glass in two distinct
soiling-prone locations: Dubai (hot and dry) and Mumbai (hot and humid). The two sites showed
markedly different soiling patterns. Mumbai's samples exhibited substantial growth of filamentous

## Página 63

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
63
fungi, while Dubai's were primarily affected by inorganic contaminants.  This highlights how local
environmental factors like humidity can significantly influence the type of soiling that occurs.
Typically, this biological contamination is harder to clean than inorganic soiling and is not removed
by natural cleaning  [198]. Rinse or low -pressure washing might not be an effective solution to
remove fungi from PV modules. Wiping techniques and more frequent cleaning should be adopted
in such cases.
Biological growth on PV system components beyond the modules themselves is an often over-
looked but significant issue in solar energy installations, particularly in  hot and humid climates.
Components such as mounting structures, cables, and junction boxes are susceptible to biofoul-
ing. These growths can lead to accelerated corrosion of metal parts, degradation of cable insula-
tion materials, and potential short circuits in electrical connections.
6.2.4 High irradiation and frequent cloud cover changes
Tropical and subtropical locations can be characterised by rapid and frequent variations in irradi-
ance, due to frequent cloud cover changes,  which cause rapid, low -amplitude temperature
changes in PV modules. A study by Bosco et al. showed that this variation in temperature, to-
gether with the mean daily maximum temperature and the daily maximum temperature variation,
is one of the three key factors in determining thermo-mechanical fatigue stress on cell intercon-
nects [138]. The IEC 62892:2019 (Annex B) provides a metric, r(55), which quantifies how often
within a year the module temperature fluctuates across the 55°C threshold.
6.3 Best practice and mitigation strategies (hot & humid)
While the previous section explored the challenges faced by PV systems in hot and humid cli-
mates, this section focuses on strategies to optimi se their performance and longevity in these
demanding environments. Three key areas of optimisation are examined: site assessment, com-
ponent selection, and system design. Each of these aspects plays a crucial role in ensuring that
PV installations can withstand the stressors of high temperatures and elevated humidity while
maintaining optimal efficiency. The followi ng subsections will discuss some of the best ap-
proaches for each of these optimisation strategies.
6.3.1 Site assessment
Site assessment and selection are critical steps in optimi sing photovoltaic (PV) systems for hot
and humid climates. This process involves evaluating several key factors specific to these chal-
lenging environments: solar resource and atmospheric conditions, temperature and humidity pat-
terns and environmental factors affecting system performance.

Solar resource and atmospheric conditions
In hot and humid climates, the assessment of solar resources must account for unique atmos-
pheric conditions that can affect PV performance. A previous study [199] showed that cloud cover
can significantly impact PV output. When planning large photovoltaic systems, the effects of cloud
cover and the resultant output loss can be mitigated by distributing the PV capacity across multi-
ple, spatially separated sites , so that localized cloud events are less likely to impact the entire
system simultaneously.
The following atmospheric conditions could be considered in the site assessment:
• Assess seasonal variations in atmospheric conditions: historical weather data should
be analysed to identify recurring patterns of dense cloud cover and heavy precipitation.

## Página 64

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

64
These. Understand how these seasonal variations in atmospheric conditions can affect
solar irradiance levels and cause fluctuations in PV system output over the course of a
year. Evaluate whether the site experiences prolonged periods of reduced solar resource
during certain seasons and assess the impact on overall energy yield.
• Air quality assessment: Assess the local and regional air quality data. Analyse how air
pollution levels can vary seasonally and the potential impact on solar irradiance reaching
the PV system. Prioriti se sites with relatively cleaner air, or identify potential mitigation
strategies, such as enhanced cleaning schedules, to address the effects of air pollution
on system performance
• Atmospheric aerosol monitoring: Assess long-term trends and seasonal patterns in at-
mospheric aerosol levels, as these can significantly affect solar radiation reaching PV
panels. This is particularly important in regions prone to biomass burning, dust storms, or
industrial emissions tha t can cause sudden or periodic increases in aerosol concentra-
tions. Monitoring long-term aerosol trends and seasonal variability can improve the accu-
racy of solar resource assessment and highlight periods of increased atmospheric atten-
uation

Temperature and humidity patterns
As discussed in Section 6.2.1, the combination of high temperature and high humidity presents
significant challenges for PV systems in tropical climates. High temperatures reduce voltage out-
put and overall power production, particularly in crystalline silicon modules, while high humidity
exacerbates these effects by hindering heat dissipation. The synergistic impact of heat and hu-
midity accelerates various d egradation mechanisms, including potential -induced degradation
(PID), corrosion, and encapsulant delamination. Additionally, high humidity environments can
lead to reduced insulation resistance, potentially causing safety issues and system startup delays,
especially in floating PV installations. Given these effects, the following recommendations could
be considered in the site assessment for high temperature and humidity environments.
• Microclimate analysis: Conduct detailed assessments of local microclimates, including
temperature and humidity patterns, seasonal variations, and any unique geographical fea-
tures that might influence these factors.
• Elevation and air circulation: Evaluate site elevation and natural air circulation patterns,
as higher elevations or areas with better air movement may offer slightly cooler tempera-
tures and reduced humidity.
• Extreme events: Pay attention to extreme weather events, monsoon patterns, and peri-
ods of exceptionally high temperature or humidity that could impact system performance
and durability, to guide decisions on structural robustness, component selection, and O&M
planning.
• Urban heat island effects:  For building-mounted systems in urban or industrial areas,
consider the potential impact of heat island effects on local temperatures, which may in-
fluence operating conditions and performance.
• Available space for optimal layout: Evaluate whether the site offers sufficient space for
an optimal system layout that maximises natural cooling and minimises the operating tem-
perature of the modules.
• Long-term climate projections: Consider long-term climate change projections to antic-
ipate potential increases in temperature, frequency of extreme weather events, or
changes in precipitation patterns . Such changes can provide important information to
guide site selection and system design.

## Página 65

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
65
Environmental Factors Affecting System Performance
As discussed in Sections  6.2.2 and 6.2.3, high humidity levels can contribute to enhanced dust
adhesion on PV module surfaces, leading to stubborn soiling that is harder to remove. The pres-
ence of dew can further exacerbate this issue by causing cementation of the dust particles. Addi-
tionally, the combination of hot and humid conditions can promote the development of biofilms
and other biological growths on PV modules, as well as on other system components, which can
significantly impact system performance. As such, the following considerations could be included
in the site assessment process.
• Consider the effects of vegetation growth:  Analyse the potential for vegetation, such
as trees or shrubs, to encroach on the PV system over time, leading to increased shading
or other issues. Incorporate vegetation management plans into the site assessment and
long-term maintenance strategy to ensure tha t the system's performance is not compro-
mised by environmental changes.
• Evaluate the risk of biological growth and biofouling: Assess the potential for the de-
velopment of biofilms, algae, or other biological contaminants on the PV modules and
other system components, and implement appropriate mitigation strategies , such as an
effective cleaning strategy.
6.3.2 Optimisation of module design and BOM
Like for hot & dry climates, the choice of solar cell technology significantly impacts the module's
performance under high temperatures typical of tropical climates. Cell technologies with lower
temperature coefficients minimi se efficiency losses as temperatures rise  [201]. But different ly
from hot & dry  climates, the solar cells have also to be resilient towards high humidity levels.
Conventional wafer-based mono-crystalline silicon solar cells, such as Aluminum Back Surface
Field (Al-BSF) and later Passivated Emitter and Rear Contact (PERC) cells, are g enerally not
highly susceptible to degradation caused by moisture exposure. However, the global solar market
is currently undergoing a rapid shift toward high-efficiency solar cells based on n-type silicon wa-
fers. Two primary solar cell architectures are driving this transition: (a) silicon heterojunction (SHJ)
and (b) tunnel oxide passivated contact (TOPCon). Among these, TOPCon appears poised to
become the dominant platform in the near future [202]. However, both technologies share a sig-
nificant vulnerability to moisture and water exposure, requiring careful module packaging consid-
erations to ensure durability and long-term performance [203], [204], [205], [206].
In SHJ modules, moisture -related issues can be mitigated or eliminated at the module level by
employing high-resistivity encapsulants with low water vapor transmission rates, such as polyole-
fins (POs). Alternatively, encapsulating SHJ solar cells in a water-impermeable double glass con-
figuration using an edge sealant combined can effectively address the problem [205], [206]. Also,
for TOPCon cells, the use of PO encapsulants is often recommended as the preferred choice.
However, as highlighted by [207], the compatibility of TOPCon cells with PO encapsulants from
various suppliers - and with differing formulations - requires careful evaluation. Issues can arise
from the improper selection of additives, emphasi sing the need for thorough testing to ensure
optimal performance and long-term reliability.
In general, all polymers used in PV modules for tropical regions should be moisture resistant and
show high UV stability. Similarly, the frame should be corrosion-resistant, using anodised alumi-
num or stainless steel to endure humid and salty air, especially in coastal regions. The junction
box, an integral part of the system, must have a high ingress protection (IP) rating, such as IP67
or IP68, to remain waterproof and dustproof  [208], [209]. Also, the other e lectrical components
must be adapted to the harsh conditions of tropical climates. Cables and connectors should be
moisture-proof to prevent insulation damage and corrosion.

## Página 66

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

66
The module components as well as cable and connectors should be made of UV-resistant mate-
rials. Measurement of UV radiation conducted in Singapore indicated that the annual UV radiation
is around 100 kWh/m 2 [210], greater than the 15 kWh/m 2 UV dosage typically tested following
IEC 61215 standard [32].
Self-cleaning glass surfaces can reduce the need for frequent manual cleaning, particularly in
areas with heavy rainfall and dust  [211], [212]. To ensure consistent energy output, protective
features such as hydrophobic and oleophobic coatings can minimise the accumulation of dust,
pollen, and organic debris. These must guarantee adequate durability to the harsh outdoor con-
ditions.
The module must possess mechanical strength to withstand strong winds and potential hurri-
canes. A robust frame and impact-resistant glass can ensure durability.
There have been efforts to produce modules optimised for hot and humid climate  [213]. The
frameless “Singapore module” is equipped with Albarino G textured glass to allow more diffuse
irradiance to reach the solar cells and humidity -resistant encapsulant and backsheet. Manufac-
turers – such as Hyundai [214], QW Solar [215] – have also introduced humidity-resistant modules
for floating PV applications. Nevertheless, PV module production is very competitive. As such,
customisation for specific climates may increase production cost more than it increases yield over
the lifetime of the system such that LCOE of the PV system may be higher.
6.3.3 System design
The design of PV systems in hot & humid locations must consider the characteristics of the stress-
ors typical of these climates.
For instance, the system must be designed to minimise the effect of soiling and to limit any bio-
logical growth. Soiling must be regularly monitored, as it may vary with the season and from year
to year. Rainfall is the dominant natural cleaning agent for soiling, but at the same time it might
interact with dust particles resulting in non-uniform, caked soiling buildup. Also, the presence of
frame can provide elevated boundaries above the glass where particles can collect. So, even if
particles are washed off by rain, they can still accumulate along the bottom frame. For this reason,
maximum power-based measurements should be preferred as non -uniform soiling might not be
measured by short-circuit current based methods.Figure 37 gives an example of how soil accu-
mulates over time at low tilt angles if no cleaning is performed.

## Página 67

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
67

Figure 37: Evolution of soiling on an unmaintained flat PV system in Singapore [216].

A regular cleaning schedule is recommended, especially during the dry periods, but care should
also be taken during rainy seasons, to remove any accumulation of soiling along the frame.  Be-
cause of the enhanced adhesion, contact-based cleaning procedures (such as dry brush or wet
sponge and rubber squeegee) should be preferred, even if they increase the risk of abrasion
[197]. If biological contamination is present, this often cannot be removed by natural agents alone,
and may require more frequent cleaning and, possibly, the employment of mild cleaning solutions
[198]. The use of anti-soiling coatings could be considered to improve the cleaning effect of rainfall
and dew, even their durability can be affected by factors such as the pH of rainwater or acidic
substances secreted by fungi.
Even if low tilts ensure a higher irradiation on the modules at low latitudes, designers should take
into account that lower tilts will favor soiling accumulation  [217]. For example, PV systems in
Singapore (located at 1°N latitude) are typically installed with tilt angle of 10° to facilitate the
cleaning effect of rain  [216]. Additionally, the optimal tilt direction (azimuth) is not necessarily
towards the equator. Tropical places are characterised by unique cloud behaviors and as a result,
the rule of thumb of facing the equator may not be accurate. For the case of Singapore where the
mornings tend to be sunnier than the afternoons, PV modules facing East received more irradi-
ance and generated 1–2% more energy than those facing North or South [218].
Additionally, the use of high IP rating equipment, including electrical boxes, is recommended as
it can help to avoid moisture ingress and reduce risks related to circuit breakers in conditions of
constant high humidity. Similarly, corrosion-resistant materials for all the PV system components
should be preferred.

## Página 68

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

68
6.4 Case Studies: Module Technology Selection
6.4.1 Case study 1: PV module degradation in tropical Singapore
The tropical rainforest climate (Af) of Singapore, a city-state in southeastern Asia, is characterised
by consistently high temperatures (monthly average of 26-28°C) and relative humidity levels (av-
erage 83.9%). In addition, it is subject to frequent rainfall, occurring averagely on 169 days a year,
and intense UV radiation year-round. These conditions, coupled with urban pollution, exacerbate
the degradation mechanisms of PV modules.
This case study summari ses the findings of an analysis conducted on PV modules after more
than 10 years of field operation [219]. The modules were randomly selected from a 10°-tilted roof-
mounted PV system, which was made of three different module technologies: multi -crystalline
(multi-Si), mono-crystalline silicon (mono-Si), and Copper indium selenide (CIS). Two modules
per technology were analysed.
Figure 38 summarises the Standard Test Condition (STC) performance degradation of the ana-
lysed PV modules compared to their initial ratings [219]. Among the multi-Si modules, causes of
the power loss were primarily due to reductions in fill factor (FF), while the short -circuit current
(Isc) and the open circuit voltage (Voc) were essentially unaffected. The power loss in the mono-
Si modules was driven by severe reductions in FF and Isc (~12-15%). The latter can be attributed
to encapsulant discolouration.
Encapsulant degradation, corrosion, and potential -induced degradation (PID) emerged as the
most critical issues. Multi-crystalline silicon (multi-Si) modules exhibited encapsulant discoloura-
tion (more pronounced near cell centres), corrosion near cell edges, and some power loss (~9%).
Mono-Si modules suffered catastrophic power losses (>40%), mainly due to severe encapsulant
discolouration, PID, and metallisation corrosion. The two silicon technologies were sourced from
the same manufacturer and showed different patterns in their degradation mechanisms. Multi-Si
modules exhibited discolouration concentrated in the centre of the cells, whereas mono-Si mod-
ules showed more intense browning uniformly across the entire cell surface. The more severe
loss in encapsulant transmission was also confirmed by the external quantum efficiency (EQE)
analysis, which showed, for the mono -Si modules, substantial EQE loss for the waveband from
400 to 1000 nm. Air bubbles were also found in the cell gaps of the mono-Si modules, which was
possibly attributed to a low-quality lamination process.
CIS modules showed two different degrees of degradation. In one case, encapsulant discoloura-
tion and corrosion caused a power loss of 15.7%, whereas in the second case, power losses
reached 45.3%, primarily attributed to PID. The latter was predominantly attributed to significant
reductions in Voc (~16%) and FF (~24%), consistent with the effects of PID.

## Página 69

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
69

Figure 38: Comparison of STC performance of the six modules investigated in [219], com-
pared to their initial ratings.
Some important lessons can be drawn from this analysis. Constant exposure to high humidity and
UV radiation likely accelerated encapsulant degradation and corrosion processes. Additionally,
the maritime environment introduced salt mist and haze, further exacerbating soiling and corro-
sion.
However, it should also be noted that the module technologies analysed in the aforementioned
study [219], and in similar long-term efforts [186], [220], such as the multi-crystalline Al-BSF and
PERC, are no longer dominant today. The industry has shifted towards n -type monocrystalline
TOPCon, heterojunction, and IBC technologies [221]. As module technologies change, the dom-
inant forms of degradation may also change. For example, recent modules (e.g.,  [222]) have an
“Anti-PID Guarantee” through optimisation of cell production technology and material control.
6.4.2 Case study 2: Soiling in Southern Brazil and the role of the PV module tech-
nology
Brazil is a country with generally favourable conditions for PV, although climates vary significantly
across its territory. The southern region is characteri sed by tropical and subtropical conditions,
with high humidity and precipitation levels.
Costa et al. [223] monitored soiling losses for over a year in the cities of Porto Alegre ( Southern
region, humid subtropical climate) and Belo Horizonte (Southeastern region, tropical wet and dry
climate). The authors deployed at each location a soiling monitoring system, composed of thin -
film CdTe and mc-Si soiling stations. Each system measured the I -V curves of two PV devices;
one kept regularly clean and the other left to naturally soil.
Over the investigated period, the authors found that both the CdTe and Si modules remained
consistently clean in Porto Alegre, thanks to the frequent year-round precipitation, even if losses
as high as 5-7% were observed after the longest 12-day dry period. Conversely, moderate soiling
was found in Belo Horizonte, with more severe accumulation during the dry summer months
(April-October). Over the longest 85-day dry period, losses as high as 27% were registered. The
authors also noted nonuniform soiling accumulating on the bottom frame of the Si modules, as
this provided an elevated boundary above the glass where the particulates collected during rain-
falls (Figure 39).

## Página 70

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

70
Precipitation was found to be the dominant natural cleaning factor  in both locations. Therefore,
regular cleaning was recommended in Belo Horizonte during the longer dry season, along with
additional extraordinary cleanings during the rainier seasons to remove soiling accumulated on
the frames. On the other hand, the year -round rainfall pattern in Porto Alegre was sufficient to
naturally keep the modules clean in that region.

Figure 39: The monocrystalline soiling station installed in Belo Horizonte. In (a), the nonu-
niform soiling accumulated on the bottom frame at the end of the 85-day dry period. In (b),
the clean module after a 20 mm rainfall [223].
In a subsequent work, Diniz et al. [224] evaluated the performance of the two PV technologies in
Belo Horizonte, taking into account the spectral effects of soiling as well as the spectral response
and the temperature coefficient of each material. Using approximately 4 years of experimental
data, the authors confirmed that the frameless CdTe modules were less prone to non -uniform
soiling distribution across their surface.
Soiling is known to have nonuniform spectral transmittance, with greater losses occurring in the
blue portion of the spectrum, due to Mie scattering, and higher transmittance in the infrared [225].
As a result, thin-film technologies with higher band gaps (i.e., lower-wavelength spectral regions)
are more impacted by soiling than, for instance, crystalline silicon technologies [226]. This could
suggest that silicon materials are always superior to wider band gap thin films in dust -prone re-
gions. However, this assumption is based on normali sed conditions and do not account for the
impact of additional variables, such as temperature. This is particularly important in hot climates,
where thermal losses can be significant, as CdTe is less sensitive to temperature than crystalline
silicon (i.e., it has temperature coefficients of lower absolute values).
For this reason, the authors of [227] specifically investigated the magnitudes of the soiling spectral
transmittance and temperature effects on the modules' performance . They identified the condi-
tions that, under Belo Horizonte's climate, would lead to either temperature losses or soiling
losses being dominant. As shown in Figure 40, they provided guidelines to determine, based on

## Página 71

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
71
these conditions, whether silicon modules could outperform CdTe modules, or vice versa , con-
cluding that temperature is the dominant parameter at temperatures beyond the 40o–50oC range.

Figure 40: Dominating factor and best performing modules, depending on soiling exposure
time and typical module temperature [227].

## Página 72

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

72
 CONCLUSIONS
As global capacity grows, PV systems are being deployed across diverse geographical regions,
each characterised by specific stressors, that in the case of harsher environments require tailored
solutions to optimise their long-term operation. The main challenges and mitigation solutions for
three common PV climates characterised by harsher environmental conditions are discussed in
this report. The level of field experience and readily available solutions differs significantly be-
tween the three. Challenges, available mitigation measures and needs for further development in
each of the three climates are here summarised.

• Cold & Snowy: These typically high-latitude or high-elevation sites are characterised by
consistently low, if not even freezing, temperatures and snowfalls. Low temperatures im-
prove the module's efficiency and slow down chemical material degradation reactions, but,
at the same time, expose PV modules and system components to additional physical and
thermomechanical degradation modes which can lead to catastrophic failures . Similarly,
snow ensures a high albedo but poses also potentially threatening load on the modules,
BOS components, and racking system, and shades the sunlight, reducing the intensity of
the irradiance reaching the PV cells. High-tilt systems with sufficient ground clearance as
well as fences for the avoidance of snow drifts help in minimising snow losses. Mounting
structures are reinforced and adapted to the diverse terrain’s morphologies and soil char-
acteristics. The mostly custom-designed solutions are often complex and cost intensive.
PV modules can be optimi sed through thicker glass, use of micro-crack tolerant cells,
special encapsulants and frames. Researc h on encapsulant properties, UV resistance,
and innovative snow-clearing methods shows promising results, but field experience with
climate-optimised PV modules and mounting structures is still very limited. Snow loss
modelling is increasingly used to predict and minimise energy losses, but the challenges
remain in accurately isolating snow effects.
• Hot & Dry: These high-solar irradiance locations are characterised by high temperatures,
arid climate and scarce rainfall. The main stressors are soiling, high temperatures, and
thermal cycling, while salty mist, intense UV irradiation, and strong winds affect only some
locations. These stressors can cause performance losses and accelerate degradation.
Low-temperature coefficient modules with alternative encapsulants, and UV - and heat-
resistant materials, are recommended to enhance durability.  Systems in these climates
must be designed to facilitate cleaning operations, whose requirements change depend-
ing on the selected business model. Further strategies include conducting soil studies to
mitigate corrosion, engineering systems to withstand wind loads, implementing smart
tracking solutions. Proposed cooling solutions, like heat spreading plates, air-cooled fins,
and phase change materials, remain largely uncommercialised. Continuous performance
and environmental monitoring through a combination of manual and automated methods
is crucial to address aging-related inefficiencies.
• Hot & Humid: These climates are characteri sed by consistently high temperatures and
elevated levels of moisture in the air, whose combination poses substantial risks, such as
corrosion, and material degradation, to PV modules and components. High humidity can
also lead to increased dust adhesion an d biological growth, with substantial impacts on
the energy yields. In equatorial locations, the losses induced by these phenomena can be
so significant that higher-than-optimal tilts and frameless configuration might be preferable
to limit the accumulation of soiling, even if they cause higher reflection and angular losses.
Designing PV modules for tropical regions includes moisture-resistant encapsulants, cor-
rosion-proof frames, and UV -stable components . Implementing regular cleaning

## Página 73

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
73
schedules, particularly during dry periods and for areas with frequent rainfall -induced
caked soiling or biological contamination, reduces soiling losses and prolongs lifetime.

Regardless of the location, the mitigation of climate -specific stressors starts with site selection
and continues throughout the lifetime of the systems. The identification of the stressors and their
impact must be conducted as early as possible to provide sufficient information for the subsequent
phases, i.e. module and component selection, and system design. Preventive and corrective mit-
igation strategies indeed influence both these phases and must be planned according to the ex-
pected stressors’ impact. Different approaches, each with its own advantages and limitations, are
available to choose the best PV modules for each climate . For example, the IEC 61853 Energy
Rating offers fast, repeatable results based on standard conditions and climate specific testing
procedures, described within a previously published IEA PVPS TASK 13 report [14], and the col-
lection of field data. Similarly, techno-economic models can be used to assess the viability of
different cleaning schedules and solutions, which differs in dependence of the climate zone and
type of soiling.
Overall, the design and operation of PV systems, as well as the selection of sites, modules, and
components, can be optimised to improve lifetime performance depending on the specific climate.
However, despite technological advancements, other constraints often prevent the adoption of
climate-specific PV modules. These include, for example, additional factors such as price, avail-
ability, and existing contracts that could also influence t he choice of modules and components
and the design of the system and which are discussed in more detail in a dedicated IEA PVPS
TASK 13 report [228].

## Página 74

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

74
REFERENCES
[1] P. S. Molina, “Global installed PV capacity tops 2 TW,” pv-magazine, Nov. 2024.
[2] IEA, “Tracking Clean Energy Progress 2023.” Accessed: Jan. 24, 2025. [Online]. Available:
https://www.iea.org/reports/tracking-clean-energy-progress-2023
[3] D. C. Jordan et al. , “Photovoltaic fleet degradation insights,” Prog. Photovoltaics Res.
Appl., vol. 30, no. 10, pp. 1166–1175, 2022, doi: 10.1002/pip.3566.
[4] S. Lindig et al., “International collaboration framework for the calculation of performance
loss rates: Data quality, benchmarks, and trends (towards a uniform methodology),” Prog.
Photovoltaics Res. Appl., no. iv, 2021, doi: 10.1002/pip.3397.
[5] M. Kottek, J. Grieser, C. Beck, B. Rudolf, and F. Rubel, “World map of the Köppen-Geiger
climate classification updated,” Meteorol. Zeitschrift, vol. 15, no. 3, pp. 259–263, 2006, doi:
10.1127/0941-2948/2006/0130.
[6] M. C. Peel, B. L. Finlayson, and T. A. McMahon, “Updated world map of the Köppen-Geiger
climate classification,” Hydrol. Earth Syst. Sci., vol. 11, no. 5, pp. 1633 –1644, Oct. 2007,
doi: 10.5194/hess-11-1633-2007.
[7] J. Ascencio -Vásquez, K. Brecl, and M. Topič, “Methodology of Köppen -Geiger-
Photovoltaic climate classification and implications to worldwide mapping of PV system
performance,” Sol. Energy , vol. 191, no. May, pp. 672 –685, 2019, doi:
10.1016/j.solener.2019.08.072.
[8] T. Karin, C. B. Jones, and A. Jain, “Photovoltaic Degradation Climate Zones,” Conf. Rec.
IEEE Photovolt. Spec. Conf. , no. 1, pp. 687 –694, 2019, doi:
10.1109/PVSC40753.2019.8980831.
[9] F. J. Triana de las Heras, O. Isabella, and M. R. Vogt, “A Machine Learning Approach to
Pv-Climate Classification,” SSRN, 2024, doi: 10.2139/ssrn.4905242.
[10] IEC, “Derisking photovoltaic modules - Sequential and combined accelerated stress testing
[IEC TR 63279:2020],” 2020. [Online]. Available:
https://webstore.iec.ch/en/publication/66173
[11] P. Hacke et al. , “Acceleration Factors for Combined ‐Accelerated Stress Testing of
Photovoltaic Modules,” Sol. RRL, vol. 7, no. 12, Jun. 2023, doi: 10.1002/solr.202300068.
[12] IEC, “Extended thermal cycling of PV modules - Test procedure [IEC 62892:2019],” 2019.
[Online]. Available: https://webstore.iec.ch/en/publication/29329
[13] International Electrotechnical Commission (IEC), “IEC 61853-1: Photovoltaic (PV) module
performance testing and energy rating - Part 1: Irradiance and temperature performance
measurements and power rating,” 2011.
[14] Johanna Bonilla Castro et al. , Climatic Rating of Photovoltaic Modules: Different
Technologies for Various Operating Conditions [IEA -PVPS T13-20:2020]. 2020. [Online].
Available: https://iea-pvps.org/key-topics/climatic-rating-of-photovoltaic-modules/
[15] M. R. Vogt, G. Pilis, M. Zeman, R. Santbergen, and O. Isabella, “Developing an energy
rating for bifacial photovoltaic modules,” Prog. Photovoltaics Res. Appl., vol. 31, no. 12, pp.
1466–1477, 2023, doi: 10.1002/pip.3678.

## Página 75

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
75
[16] CINEA, “Development of standardisation methods for eco -design and energy labelling of
photovoltaic products,” Service contract CINEA/2023/OP/0009/SI2.908958. Accessed:
May 31, 2024. [Online]. Available: https://ecodesign-pv-testing.eu/
[17] International Electrotechnical Commission (IEC), “IEC 61853-4: Photovoltaic (PV) module
performance testing and energy rating - Part 4: Standard reference climatic profiles,” 2018.
[18] T. Huld, E. Dunlop, H. G. Beyer, and R. Gottschalg, “Data sets for energy rating of
photovoltaic modules,” Sol. Energy , vol. 93, pp. 267 –279, 2013, doi:
10.1016/j.solener.2013.04.014.
[19] T. Huld and A. M. Gracia Amillo, “Estimating PV module performance over large
geographical regions: The role of irradiance, air temperature, wind speed and solar
spectrum,” Energies, vol. 8, no. 6, pp. 5159–5181, 2015, doi: 10.3390/en8065159.
[20] T. Huld, E. Salis, A. Pozza, W. Herrmann, and H. Müllejans, “Photovoltaic energy rating
data sets for Europe,” Sol. Energy , vol. 133, pp. 349 –362, 2016, doi:
10.1016/j.solener.2016.03.071.
[21] M. Ruben Vogt et al., “PV Module Energy Rating Standard IEC 61853 -3 Intercomparison
and Best Practice Guidelines for Implementation and Validation,” IEEE J. Photovoltaics,
vol. 12, no. 3, pp. 844–852, 2022, doi: 10.1109/JPHOTOV.2021.3135258.
[22] W. Herrmann, G. Bardizza, G. Friesen, S. Riechelmann, and H. Müllejans, “Uncertainty of
Climate Specific Energy Rating (CSER) of PV Modules in accordance with IEC 61853,”
Prog. Photovoltaics Res. Appl..
[23] J. C. Blakesley et al., “Accuracy, cost and sensitivity analysis of PV energy rating,” Sol.
Energy, vol. 203, no. April, pp. 91–100, 2020, doi: 10.1016/j.solener.2020.03.088.
[24] T. Huld, A. Gracia Amillo, T. Sample, E. D. Dunlop, E. Salis, and R. Kenny, “The completed
IEC 61853 Standard Series on PV module energy rating, overview, applications and
outlook,” in 35th European Photovoltaic Solar Energy Conference and Exhibition, Brussels,
Belgium, 2018.
[25] K. S. Anderson, J. S. Stein, and M. Theristis, “Variation in Photovoltaic Energy Rating and
Underlying Drivers Across Modules and Climates,” IEEE Access , vol. 13, pp. 21064 –
21073, 2025, doi: 10.1109/ACCESS.2025.3534678.
[26] European Parliament and Council of the European Union, “Directive 2009/125/EC of the
European Parliament and of the Council of 21 October 2009 establishing a framework for
the setting of ecodesign requirements for energy-related products.” 2009.
[27] European Parliament and Council of the European Union, “Regulation (EU) 2017/1369 of
the European Parliament and of the Council of 4 July 2017 setting a framework for energy
labelling and repealing Directive 2010/30/EU.” 2017.
[28] European Commission, “Solar Photovoltaics.” Accessed: Jan. 24, 2025. [Online].
Available: https://susproc.jrc.ec.europa.eu/product-bureau/product-groups/462/home
[29] N. Dodd, N. Espinosa, P. Van Tichelen, K. Peeters, and A. Soares, “Preparatory study for
solar photovoltaic modules, inverters and systems,” 2020. doi: 10.2760/852637.
[30] European Commission, “Ecodesign – European Commission to examine need for new
rules on environmental impact of photovoltaics.” Accessed: Jan. 24, 2025. [Online].
Available: https://ec.europa.eu/info/law/better -regulation/have-your-say/initiatives/12819-
Ecodesign-European-Commission-to-examine-need-for-new-rules-on-environmental-

## Página 76

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

76
impact-of-photovoltaics_en
[31] T. Lyubenova, E. Dunlop, T. Sample, N. Taylor, and D. Polverini, “Potential energy label
for monofacial and bifacial PV modules,” in 40th European Photovoltaic Solar Energy
Conference and Exhibition , Lisbon, Portugal, 2023. doi:
10.4229/EUPVSEC2023/5DV.3.10.
[32] International Electrotechnical Commission (IEC), “IEC 61215 -1: Terrestrial photovoltaic
(PV) modules - Design qualification and type approval - Part 1: Test requirements,” 2021.
[33] International Electrotechnical Commission (IEC), “IEC Technical Specification 60904-1-2:
Photovoltaic devices - Part 1-2: Measurement of current-voltage characteristics of bifacial
photovoltaic (PV) devices,” 2024.
[34] E. D. G. Dunlop, A. Amillo, and E. Salis, “Transitional method for PV modules, inverters,
components and systems (EUR 29513 EN),” Luxemburg, 2019. doi: 10.2760/496002.
[35] European Commission, “EPREL - European Product Registry for Energy Labelling.”
Accessed: Jan. 24, 2025. [Online]. Available: https://eprel.ec.europa.eu/screen/home
[36] M. Rivera and C. Reise, “Short Term Outdoor Energy Rating vs Climate Specific Energy
Rating (CSER),” in 40th European Photovoltaic Solar Energy Conference and Exhibition ,
Lisbon, Portugal, 2023.
[37] M. Rivera, C. Reise, and U. Kräling, “Representativeness of Energy Rating acc. to IEC
61853 for Different Locations in Middle and South Europe,” Energy Technol., vol. 11, no.
12, pp. 1–12, 2023, doi: 10.1002/ente.202300356.
[38] C. Monokroussos et al. , “Energy performance of commercial c -Si PV modules in
accordance with IEC 61853 -1, -2 and impact on the annual specific yield,” EPJ
Photovoltaics, vol. 14, pp. 1–9, 2023, doi: 10.1051/epjpv/2022032.
[39] S. Lindig et al., Best practice guidelines for the use of economic and technical KPIs [IEA -
PVPS T13 -28:2024]. 2024. [Online]. Available: https://iea -pvps.org/wp-
content/uploads/2024/12/IEA-PVPS-T13-28-2024-REPORT-Technical-and-Economic-
KPIs.pdf
[40] R. H. French et al., Assessment of Performance loss rate of PV Power systems [IEA-PVPS
T13-22:2021]. 2021. [Online]. Available: https://iea -pvps.org/key-topics/assessment-of-
performance-loss-rate-of-pv-power-systems/
[41] J. Ascencio-Vásquez, I. Kaaya, K. Brecl, K. A. Weiss, and M. Topič, “Global climate data
processing and mapping of degradation mechanisms and degradation rates of PV
modules,” Energies, vol. 12, no. 24, pp. 1–16, 2019, doi: 10.3390/en12244749.
[42] G. Friesen et al., Photovoltaic Module Energy Yield Measurements: Existing Approaches
and Best Practice [IEA ‐PVPS T13 ‐11:2018]. 2018. [Online]. Available: https://iea -
pvps.org/key-topics/photovoltaic-module-energy-yield-measurements-existing-
approaches-and-best-practice/
[43] N. Bogdanski, W. Herrmann, F. Reil, M. Köhl, K. -A. Weiss, and M. Heck, “Results of 3
years’ PV module weathering in various open -air climates,” in SPIE Solar Energy +
Technology, San Diego, California, 2010.
[44] C. Reise, U. Krälling, E. Schnabel, and K. Kiefer, “First Results from a High Precision
Indoor & Outdoor PV Module Monitoring Campaign,” in 36th European Photovoltaic Solar
Energy Conference and Exhibition, Marseille, France, 2019.

## Página 77

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
77
[45] I. Kaaya, M. Koehl, A. P. Mehilli, S. De Cardona Mariano, and K. A. Weiss, “Modeling
Outdoor Service Lifetime Prediction of PV Modules: Effects of Combined Climatic
Stressors on PV Module Power Degradation,” IEEE J. Photovoltaics , vol. 9, no. 4, pp.
1105–1112, 2019, doi: 10.1109/JPHOTOV.2019.2916197.
[46] L. Burnham et al. , “Dedicated cold -climate field laboratory for photovoltaic system and
component studies: the Michigan Regional Test Center as a case study,” in 2022 IEEE
49th Photovoltaics Specialists Conference (PVSC), IEEE, Jun. 2022, pp. 0333–0335. doi:
10.1109/PVSC48317.2022.9938861.
[47] U.S. Department of Energy, “Photovoltaic Collaborative to Advance Multi -climate
Performance and Energy Research (PV CAMPER).” Accessed: Jan. 31, 2025. [Online].
Available: https://energy.sandia.gov/programs/renewable -energy/photovoltaic-solar-
energy/projects/photovoltaic-collaborative-to-advance-multi-climate-performance-and-
energy-research-pv-camper/
[48] L. Burnham et al. , “Inside PV CAMPER: A global research collaborative to advance
photovoltaic performance across a range of operating climates,” PV-Tech.org, 2021.
[Online]. Available: https://www.pv -tech.org/technical-papers/inside-pv-camper-a-global-
research-collaborative-to-advance-photovoltaic-performance-across-a-range-of-
operating-climates/
[49] M. Theristis et al. , “Onymous early -life performance degradation analysis of recent
photovoltaic module technologies,” Prog. Photovoltaics Res. Appl., vol. 31, no. 2, pp. 149–
160, 2023, doi: 10.1002/pip.3615.
[50] E. Özkalay et al. , “Correlating long -term performance and aging behaviour of building
integrated PV modules,” Energy Build. , vol. 316, p. 114252, Aug. 2024, doi:
10.1016/j.enbuild.2024.114252.
[51] A. Protti, J. Shahid, M. Mittag, D. H. Neuhaus, U. Kräling, and M. Kaiser, “Virtual Energy
Rating: a Method for Optimizing Module Performance Through Cell -To-Module Analysis,”
in 8th World Conference on Photovoltaic Energy Conversion, Milan, Italy, 2022.
[52] S. Ramesh, G. Janssen, and B. B. Van Aken, “Improving the yield by designing the module
for a climatic region,” in 36th European Photovoltaic Solar Energy Conference and
Exhibition2, Marseille, France, 2019. doi: 10.4229/EUPVSEC20192019-4CO.2.3.
[53] M. Kumari, M. Theristis, and J. S. Stein, “Geographic Analysis for Determining the Value
of Different Photovoltaic Performance Factors,” Conf. Rec. IEEE Photovolt. Spec. Conf. ,
vol. 2022-June, pp. 888–892, 2022, doi: 10.1109/PVSC48317.2022.9938745.
[54] C. Monokroussos et al. , “ENERGY RATING OF C -SI AND MC -SI COMMERCIAL PV -
MODULES IN ACCORDANCE WITH IEC 61853-1,-2,-3 AND IMPACT ON THE ANNUAL
YIELD,” in 33rd European Photovoltaic Solar Energy Conference and Exhibition ,
Amsterdam, The Netherlands, 207AD.
[55] G. Friesen, M. Caccivio, E. Ozkalay, and F. Valoti, “Impact of Technological Trends in
Crystalline Silicon PV Modules on the Energy Yield Performance: Preliminary Result of the
14th SUPSI Outdoor Measurement Campaign,” in 8th World Conference on Photovoltaic
Energy Conversion, Milan, Italy, 2022.
[56] L. Micheli et al. , “The economic value of photovoltaic performance loss mitigation in
electricity spot markets,” Renew. Energy , vol. 199, pp. 486 –497, Nov. 2022, doi:
10.1016/j.renene.2022.08.149.

## Página 78

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

78
[57] Solar Energy Industries Association, “Alaska: State Overview.” Accessed: Jan. 24, 2025.
[Online]. Available: https://seia.org/state-solar-policy/alaska-solar/
[58] Swiss universities of applied sciences, “Alpine PV Competence.” Accessed: Jan. 24, 2025.
[Online]. Available: https://alpine-pv.ch/
[59] P. Croce, P. Formichi, and F. Landi, “Evaluation of current trends of climatic actions in
europe based on observations and regional reanalysis,” Remote Sens., vol. 13, no. 11,
2021, doi: 10.3390/rs13112025.
[60] D. C. Jordan, K. Perry, R. White, and C. Deline, “Extreme Weather and PV Performance,”
IEEE J. Photovoltaics , vol. 13, no. 6, pp. 830 –835, 2023, doi:
10.1109/JPHOTOV.2023.3304357.
[61] A. Virtuani et al. , “35 years of photovoltaics: Analysis of the TISO ‐10‐kW solar plant,
lessons learnt in safety and performance—Part 1,” Prog. Photovoltaics Res. Appl., vol. 27,
no. 4, pp. 328–339, Apr. 2019, doi: 10.1002/pip.3104.
[62] E. Özkalay, H. Quest, and A. Gassner, “Three Decades, Three Climates: Assessing
Environmental and Material Effects on PV Module Reliability,” Submitted.
[63] U. Muntwyler and T. Schott, “Degradation of photovoltaic systems based on long -term
measurements and laboratory tests,” in Proceedings of EuroSun 2018, Freiburg, Germany:
International Solar Energy Society, 2018, pp. 1–7. doi: 10.18086/eurosun2018.02.07.
[64] K. G. Libbrecht, “Toward a Comprehensive Model of Snow Crystal Growth Dynamics: 1.
Overarching Features and Physical Origins,” arXiv, pp. 1 –18, 2012, [Online]. Available:
http://arxiv.org/abs/1211.5555
[65] K. G. Libbrecht, “The physics of snow crystals,” Reports Prog. Phys. , vol. 68, no. 4, pp.
855–895, 2005, doi: 10.1088/0034-4885/68/4/R03.
[66] C. Fierz et al., “The international classification for seasonal snow on the ground,” UNESCO,
IHP–VII, Tech. Doc. Hydrol. No 83; IACS Contrib. No 1 , p. 80, 2009, [Online]. Available:
http://www.cryosphericsciences.org/snowClassification.html%5Cnhttp://www.unesco.org/
ulis/cgi-
bin/ulis.pl?catno=186462&set=4DB9AB33_0_160&gp=1&lin=1&ll=1%5Cnhttp://scholar.g
oogle.com/scholar?hl=en&btnG=Search&q=intitle:The+International+Classification+for+
[67] P.-O. A. Borrebæk, S. Rønneberg, B. P. Jelle, A. Klein -Paste, Z. Zhang, and J. He, “A
framework for classification of snow- and icephobicity,” J. Adhes. Sci. Technol., vol. 35, no.
10, pp. 1087–1098, May 2021, doi: 10.1080/01694243.2020.1834286.
[68] E. Xiao, S. Li, A. M. Nazar, R. Zhu, and Y. Wang, “Antarctic Snow Failure Mechanics:
Analysis, Simulations, and Applications,” Materials (Basel). , 2024, doi:
https://doi.org/10.3390/ma17071490.
[69] R. W. Andrews, A. Pollard, and J. M. Pearce, “The effects of snowfall on solar photovoltaic
performance,” Sol. Energy , vol. 92, pp. 84 –97, Jun. 2013, doi:
10.1016/j.solener.2013.02.014.
[70] U. Jahn et al., Guidelines for Operation and Maintenance of Photovoltaic Power Plants in
Different Climates [IEA -PVPS T13 -28:2024]. 2022. [Online]. Available: https://iea -
pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-systems/.
[71] D. K. Perovich, “Light Transmission Through Snow,” AGU, vol. 2002, pp. C11B -0990,
2002.

## Página 79

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
79
[72] C. Schill et al., Soiling Losses – Impact on the Performance of Photovoltaic Power Plants
[IEA-PVPS T13-21:2022]. 2022. [Online]. Available: https://iea-pvps.org/key-topics/soiling-
losses-impact-on-the-performance-of-photovoltaic-power-plants/
[73] A. Omazic et al., “Relation between degradation of polymeric components in crystalline
silicon PV module and climatic conditions: A literature review,” Sol. Energy Mater. Sol.
Cells, vol. 192, pp. 123–133, Apr. 2019, doi: 10.1016/J.SOLMAT.2018.12.027.
[74] G. W. Ehrenstein, “Polymeric Materials,” in Polymeric Materials, München: Carl Hanser
Verlag GmbH &amp; Co. KG, 2001, pp. i–xiv. doi: 10.3139/9783446434134.fm.
[75] N. Bosco, M. Springer, and X. He, “Viscoelastic Material Characterization and Modeling of
Photovoltaic Module Packaging Materials for Direct Finite-Element Method Input,” IEEE J.
Photovoltaics, vol. 10, no. 5, pp. 1424 –1440, Sep. 2020, doi:
10.1109/JPHOTOV.2020.3005086.
[76] G. Oreski and G. M. Wallner, “Damp heat induced physical aging of PV encapsulation
materials,” in 2010 12th IEEE Intersociety Conference on Thermal and Thermomechanical
Phenomena in Electronic Systems , IEEE, Jun. 2010, pp. 1 –6. doi:
10.1109/ITHERM.2010.5501297.
[77] M. Lang, G. Oreski, E. Helfer, A. Halm, M. Klenk, and P. Fuchs, “FEM simulation of
deformations and stresses in strings of shingled solar cells under mechanical and thermal
loading,” 2022, p. 020008. doi: 10.1063/5.0126221.
[78] M. Springer and N. Bosco, “Environmental influence on cracking and debonding of
electrically conductive adhesives,” Eng. Fract. Mech., vol. 241, p. 107398, Jan. 2021, doi:
10.1016/j.engfracmech.2020.107398.
[79] M. Springer, J. Hartley, and N. Bosco, “Multiscale Modeling of Shingled Cell Photovoltaic
Modules for Reliability Assessment of Electrically Conductive Adhesive Cell
Interconnects,” IEEE J. Photovoltaics , vol. 11, no. 4, pp. 1040 –1047, Jul. 2021, doi:
10.1109/JPHOTOV.2021.3066302.
[80] N. Klasen, P. Romer, A. Beinert, and A. Kraft, “FEM simulation of deformations in strings
of shingled solar cells subjected to mechanical reliability testing,” 2019, p. 020016. doi:
10.1063/1.5125881.
[81] J. Kettle et al., “Review of technology specific degradation in crystalline silicon, cadmium
telluride, copper indium gallium selenide, dye sensitised, organic and perovskite solar cells
in photovoltaic modules: Understanding how reliability improvements in mature technolog,”
Prog. Photovoltaics Res. Appl. , vol. 30, no. 12, pp. 1365 –1392, 2022, doi:
10.1002/pip.3577.
[82] M. Aghaei et al., “Review of degradation and failure phenomena in photovoltaic modules,”
Renew. Sustain. Energy Rev. , vol. 159, no. January, p. 112160, 2022, doi:
10.1016/j.rser.2022.112160.
[83] G. Oreski et al., “Performance of PV modules using co -extruded backsheets based on
polypropylene,” Sol. Energy Mater. Sol. Cells , vol. 223, p. 110976, May 2021, doi:
10.1016/j.solmat.2021.110976.
[84] M. P. Brennan, A. L. Abramase, R. W. Andrews, and J. M. Pearce, “Effects of spectral
albedo on solar photovoltaic devices,” Sol. Energy Mater. Sol. Cells, vol. 124, pp. 111–116,
May 2014, doi: 10.1016/j.solmat.2014.01.046.

## Página 80

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

80
[85] R. Chadyšienė and A. Girgždys, “ULTRAVIOLET RADIATION ALBEDO OF NATURAL
SURFACES/NATŪRALIŲ PAVIRŠIŲ ULTRAVIOLETINĖS SPINDULIUOTĖS
ALBEDAS/АЛЬБЕДО УЛЬТРАФИОЛЕТОВОГО ИЗЛУЧЕНИЯ НАТУРАЛЬНЫХ
ПОВЕРХНОСТЕЙ,” J. Environ. Eng. Landsc. Manag., vol. 16, no. 2, pp. 83–88, Jun. 2008,
doi: 10.3846/1648-6897.2008.16.83-88.
[86] World Health Organization, “Radiation: Ultraviolet (UV) radiation.” Accessed: Jan. 24,
2025. [Online]. Available: https://www.who.int/news -room/questions-and-
answers/item/radiation-ultraviolet-(uv)
[87] A. Kahl, J. Dujardin, and M. Lehning, “The bright side of PV production in snow -covered
mountains,” Proc. Natl. Acad. Sci. , vol. 116, no. 4, pp. 1162 –1167, Jan. 2019, doi:
10.1073/pnas.1720808116.
[88] K. Slamova, J. Wirth, C. Schill, and M. Koehl, “Ultraviolet radiation as a stress factor for the
PV-modules - Global approach,” Conf. Rec. IEEE Photovolt. Spec. Conf., pp. 1594–1599,
2013, doi: 10.1109/PVSC.2013.6744450.
[89] I. Frimannslund, T. Thiis, A. Aalberg, and B. Thorud, “Polar solar power plants –
Investigating the potential and the design challenges,” Sol. Energy, vol. 224, no. May, pp.
35–42, 2021, doi: 10.1016/j.solener.2021.05.069.
[90] P. Romer, K. B. Pethani, and A. J. Beinert, “Effects of Wind Load on the Mechanics of a
PV Power Plant,” in 8th World Conference on Photovoltaic Energy Conversion, 2022.
[91] A. Gabor, “Solar panel design factors to reduce the impact of cracked cells and the
tendency for crack propagation,” in NREL PV Module Reliability Workshop, Denver (CO),
2015.
[92] D. Riley, L. Burnham, B. Walker, and J. M. Pearce, “Differences in Snow Shedding in
Photovoltaic Systems with Framed and Frameless Modules,” Conf. Rec. IEEE Photovolt.
Spec. Conf., pp. 558–561, 2019, doi: 10.1109/PVSC40753.2019.8981389.
[93] U.S. Department of Energy, “Solar Photovoltaic Hardening for Resilience – Winter
Weather.” Accessed: Jan. 24, 2025. [Online]. Available:
https://www.energy.gov/femp/solar-photovoltaic-hardening-resilience-winter-weather
[94] P.-O. A. Borrebæk, B. P. Jelle, and Z. Zhang, “Avoiding snow and ice accretion on building
integrated photovoltaics – challenges, strategies, and opportunities,” Sol. Energy Mater.
Sol. Cells, vol. 206, p. 110306, Mar. 2020, doi: 10.1016/j.solmat.2019.110306.
[95] J. P. Aubell and A. Gebremedhin, “Framed -or Frameless Photovoltaic in Snow
Experiencing Climates,” Int. J. Innov. Technol. Interdiscip. Sci. www .IJITIS.org, vol. 4, no.
3, pp. 742 –753, 2021, [Online]. Available: https://doi.org/10.15157/IJITIS.2021.4.3.742 -
753
[96] ReneSola, “Subverting tradition and pioneering innovation--ReneSola’s high-strength alloy
steel frame photovoltaic modules open a new chapter.” Accessed: Jan. 24, 2025. [Online].
Available: https://www.renesola-energy.com/news_detail/1750789837987926016.html
[97] M. Köntges et al., Review of Failures of Photovoltaic Modules [IEA -PVPS T13-01:2014].
2024. [Online]. Available: https://iea-pvps.org/key-topics/review-of-failures-of-photovoltaic-
modules-final/
[98] P. Romer, K. B. Pethani, and A. J. Beinert, “Effect of inhomogeneous loads on the
mechanics of PV modules,” Prog. Photovoltaics Res. Appl., vol. 32, no. 2, pp. 84–101, Feb.

## Página 81

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
81
2024, doi: 10.1002/pip.3738.
[99] A. Gassner et al., “Accelerate Product Development for PV in Alpine Installations,” in 41st
European Photovoltaic Solar Energy Conference & Exhibition, Vienna, Austria, 2024.
[100] M. Köntges et al., Degradation and Failure Modes in New Photovol- taic Cell and Module
Technologies [IEA-PVPS T13-30:2025]. 2025. [Online]. Available: https://iea-pvps.org/key-
topics/degradation-failure-modes-new-cell-module-technologies/
[101] IEC, “Test methods for UV-induced power degradation - Part 1: Crystalline Silicon [IEC TS
63624-1 ED1],” Approved for Committee Draft (ACD) on 2025-01.
[102] K. S. Hayibo, A. Petsiuk, P. Mayville, L. Brown, and J. M. Pearce, “Monofacial vs bifacial
solar photovoltaic systems in snowy environments,” Renew. Energy, vol. 193, pp. 657 –
668, Jun. 2022, doi: 10.1016/j.renene.2022.05.050.
[103] A. Dhyani, C. Pike, J. L. Braid, E. Whitney, L. Burnham, and A. Tuteja, “Facilitating Large‐
Scale Snow Shedding from In ‐Field Solar Arrays using Icephobic Surfaces with Low ‐
Interfacial Toughness,” Adv. Mater. Technol. , vol. 7, no. 5, May 2022, doi:
10.1002/admt.202101032.
[104] Super PV, “Advanced functional nanocoatings to improve PV modules performance.”
[Online]. Available: https://www.superpv.eu/blog/Advanced -functional-nanocoatings-to-
improve-PV-modules-performance/
[105] A. Granlund, M. Lindh, T. Vikberg, and A. M. Petersson, “Evaluation of Snow Removal
Methods for Rooftop Photovoltaics,” in 8th World Conference on Photovoltaic Energy
Conversion, Milan, Italy, 2022.
[106] A. J. Barker et al., “Influence of chemical coatings on solar panel performance and snow
accumulation,” Cold Reg. Sci. Technol. , vol. 201, p. 103598, Sep. 2022, doi:
10.1016/j.coldregions.2022.103598.
[107] F. Lisco et al., “Degradation of Hydrophobic, Anti-Soiling Coatings for Solar Module Cover
Glass,” Energies, vol. 13, no. 15, p. 3811, Jul. 2020, doi: 10.3390/en13153811.
[108] D. K. Sarkar and M. Farzaneh, “Superhydrophobic Coatings with Reduced Ice Adhesion,”
J. Adhes. Sci. Technol. , vol. 23, no. 9, pp. 1215 –1237, Jan. 2009, doi:
10.1163/156856109X433964.
[109] S. A. Kulinich and M. Farzaneh, “Ice adhesion on super-hydrophobic surfaces,” Appl. Surf.
Sci., vol. 255, no. 18, pp. 8153–8157, Jun. 2009, doi: 10.1016/j.apsusc.2009.05.033.
[110] T. Verho, C. Bower, P. Andrew, S. Franssila, O. Ikkala, and R. H. A. Ras, “Mechanically
Durable Superhydrophobic Surfaces,” Adv. Mater., vol. 23, no. 5, pp. 673–678, Feb. 2011,
doi: 10.1002/adma.201003129.
[111] J. Chen et al., “Superhydrophobic surfaces cannot reduce ice adhesion,” Appl. Phys. Lett.,
vol. 101, no. 11, Sep. 2012, doi: 10.1063/1.4752436.
[112] N. Wang et al. , “Design and Fabrication of the Lyophobic Slippery Surface and Its
Application in Anti-Icing,” J. Phys. Chem. C, vol. 120, no. 20, pp. 11054–11059, May 2016,
doi: 10.1021/acs.jpcc.6b04778.
[113] H. Sojoudi, M. Wang, N. D. Boscher, G. H. McKinley, and K. K. Gleason, “Durable and
scalable icephobic surfaces: similarities and distinctions from superhydrophobic surfaces,”
Soft Matter, vol. 12, no. 7, pp. 1938–1963, 2016, doi: 10.1039/C5SM02295A.

## Página 82

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

82
[114] A. Rahmatmand, S. J. Harrison, and P. H. Oosthuizen, “An experimental investigation of
snow removal from photovoltaic solar panels by electrical heating,” Sol. Energy, vol. 171,
pp. 811–826, Sep. 2018, doi: 10.1016/j.solener.2018.07.015.
[115] A. Weiss and H. Weiss, “Photovoltaic cell electrical heating system for removing snow on
panel including verification,” in 2016 IEEE International Conference on Renewable Energy
Research and Applications (ICRERA) , IEEE, Nov. 2016, pp. 995 –1000. doi:
10.1109/ICRERA.2016.7884484.
[116] I. Frimannslund, T. Thiis, L. V. Skjøndal, and T. Marke, “Energy demand and yield
enhancement for roof mounted photovoltaic snow mitigation systems,” Energy Build., vol.
278, p. 112602, Jan. 2023, doi: 10.1016/j.enbuild.2022.112602.
[117] T. Tanahashi, T. Chiba, S. Adachi, Y. Tsuno, K. Ikeda, and T. Oozeki, “Mitigation of heavy
snow load on PV modules installed in a snowy region,” Shinjo, 2023.
[118] L. Li et al. , “Enabling Renewable Energy Technologies in Harsh Climates with Ultra ‐
Efficient Electro‐Thermal Desnowing, Defrosting, and Deicing,” Adv. Funct. Mater., vol. 32,
no. 31, Aug. 2022, doi: 10.1002/adfm.202201521.
[119] A. Granlund, J. Narvesjö, and A. M. Petersson, “The Influence of Module Tilt on Snow
Shadowing of Frameless Bifacial Modules,” in 36th European Photovoltaic Solar Energy
Conference and Exhibition, Marseille, France, 2019.
[120] F. Bockelmann, A. -K. Dreier, J. Zimmermann, and M. Peter, “Renewable energy in
Antarctica - Photovoltaic for Neumayer Station III,” Sol. Energy Adv. , vol. 2, p. 100026,
2022, doi: 10.1016/j.seja.2022.100026.
[121] F. P. Baumgartner, A. Büchel, and R. Bartholet, “Cable -Based Solar Wings Tracking
System: Two -Axis System and Progress of One -Axis System,” in 25th EU PVSEC /
WCPEC-5, 2010, pp. 2–5.
[122] M. Faraone, “Drilling down on frost heave in utility -scale PV Table of contents,” 2025.
[Online]. Available: https://discover.terrasmart.com/solid -foundation-strategies-for-
mitigating-frost-heave-in-the-northeast
[123] I. Frimannslund, T. Thiis, A. D. Ferreira, and B. Thorud, “Impact of solar power plant design
parameters on snowdrift accumulation and energy yield,” Cold Reg. Sci. Technol., vol. 201,
no. April, 2022, doi: 10.1016/j.coldregions.2022.103613.
[124] T. Townsend and L. Powers, “Photovoltaics and snow: An update from two winters of
measurements in the SIERRA,” Conf. Rec. IEEE Photovolt. Spec. Conf. , pp. 003231 –
003236, 2011, doi: 10.1109/PVSC.2011.6186627.
[125] R. E. Pawluk, Y. Chen, and Y. She, “Photovoltaic electricity generation loss due to snow –
A literature review on influence factors, estimation, and mitigation,” Renew. Sustain.
Energy Rev., vol. 107, pp. 171–182, Jun. 2019, doi: 10.1016/j.rser.2018.12.031.
[126] B. Marion, R. Schaefer, H. Caine, and G. Sanchez, “Measured and modeled photovoltaic
system energy losses from snow for Colorado and Wisconsin locations,” Sol. Energy, vol.
97, pp. 112–121, 2013, doi: 10.1016/j.solener.2013.07.029.
[127] M. B. Ogaard, I. Frimannslund, H. N. Riise, and J. Selj, “Snow Loss Modeling for Roof
Mounted Photovoltaic Systems: Improving the Marion Snow Loss Model,” IEEE J.
Photovoltaics, vol. 12, no. 4, pp. 1005 –1013, Jul. 2022, doi:
10.1109/JPHOTOV.2022.3166909.

## Página 83

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
83
[128] M. van Noord, T. Landelius, and S. Andersson, “Snow -Induced PV Loss Modeling Using
Production-Data Inferred PV System Models,” Energies, vol. 14, no. 6, p. 1574, Mar. 2021,
doi: 10.3390/en14061574.
[129] D. Gun, G. Kimball, and M. Anderson, “Dynamic snow loss model and validation,” in PV
Systems Symposium,
[130] Swiss universities of applied sciences, “Parametric study on a swiss location for alpine PV
systems.” Accessed: Jan. 24, 2025. [Online]. Available: https://alpine -pv.ch/wiki/energy-
yield-winter-yield/parametric-study-on-a-swiss-location-for-alpine-pv-systems/
[131] C. Pike, E. Whitney, M. Wilber, and J. S. Stein, “Field Performance of South -Facing and
East-West Facing Bifacial Modules in the Arctic,” Energies, vol. 14, no. 4, p. 1210, Feb.
2021, doi: 10.3390/en14041210.
[132] E. M. Tonita, A. C. J. Russell, C. E. Valdivia, and K. Hinzer, “Optimal ground coverage
ratios for tracked, fixed-tilt, and vertical photovoltaic systems for latitudes up to 75°N,” Sol.
Energy, vol. 258, pp. 8–15, Jul. 2023, doi: 10.1016/j.solener.2023.04.038.
[133] C. Schill, S. Brachmann, M. Heck, K.-A. Weiss, and M. Koehl, “Impact of heavy soiling on
the power output of PV modules,” Reliab. Photovolt. Cells, Modul. Components, Syst. IV,
vol. 8112, p. 811207, 2011, doi: 10.1117/12.893721.
[134] X. Li, D. L. Mauzerall, and M. H. Bergin, “Global reduction of solar power generation
efficiency due to aerosols and panel soiling,” Nat. Sustain., vol. 3, no. 9, pp. 720–727, Sep.
2020, doi: 10.1038/s41893-020-0553-2.
[135] A. Bhat and M. Perez, “Estimate PV soiling losses to reduce solar risk with SolarAnywhere.”
Accessed: Jan. 24, 2025. [Online]. Available:
https://www.solaranywhere.com/2022/estimate-pv-soiling-losses-with-solaranywhere/
[136] IRENA, “Renewable Power Generation Costs in 2020,” Abu Dhabi, 2021.
[137] B. Adothu et al., “Comprehensive review on performance, reliability, and roadmap of c -Si
PV modules in desert climates: A proposal for improved testing standard,” Prog.
Photovoltaics Res. Appl., vol. 32, no. 8, pp. 495–527, 2024, doi: 10.1002/pip.3827.
[138] N. Bosco, T. J. Silverman, and S. Kurtz, “Climate specific thermomechanical fatigue of flat
plate photovoltaic module solder joints,” Microelectron. Reliab., vol. 62, pp. 124–129, 2016,
doi: 10.1016/j.microrel.2016.03.024.
[139] J.-F. Lelièvre et al. , “Desert label development for improved reliability and durability of
photovoltaic modules in harsh desert conditions,” Sol. Energy Mater. Sol. Cells, vol. 236,
p. 111508, Mar. 2022, doi: 10.1016/j.solmat.2021.111508.
[140] S. Suzuki et al., “Acceleration of potential-induced degradation by salt-mist preconditioning
in crystalline silicon photovoltaic modules,” Jpn. J. Appl. Phys., vol. 54, no. 8S1, p. 08KG08,
Aug. 2015, doi: 10.7567/JJAP.54.08KG08.
[141] P. Hacke, P. Burton, A. Hendrickson, S. Spataru, S. Glick, and K. Terwilliger, “Effects of
photovoltaic module soiling on glass surface resistance and potential -induced
degradation,” in 2015 IEEE 42nd Photovoltaic Specialist Conference (PVSC) , IEEE, Jun.
2015, pp. 1–4. doi: 10.1109/PVSC.2015.7355711.
[142] H. A. Kazem and M. T. Chaichan, “The effect of dust accumulation and cleaning methods
on PV panels’ outcomes based on an experimental study of six locations in Northern
Oman,” Sol. Energy , vol. 187, no. May, pp. 30 –38, 2019, doi:

## Página 84

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

84
10.1016/j.solener.2019.05.036.
[143] G. Oreski, B. Ottersböck, and A. Omazic, “Degradation Processes and Mechanisms of
Encapsulants,” in Durability and Reliability of Polymers and Other Materials in Photovoltaic
Modules, Elsevier, 2019, pp. 135–152. doi: 10.1016/B978-0-12-811545-9.00006-9.
[144] A. Fairbrother, N. Phillips, and X. Gu, “Degradation Processes and Mechanisms of
Backsheets,” in Durability and Reliability of Polymers and Other Materials in Photovoltaic
Modules, Elsevier, 2019, pp. 153–174. doi: 10.1016/B978-0-12-811545-9.00007-0.
[145] S. Uličná et al., “Material characterization of seven photovoltaic backsheets using seven
accelerated test conditions,” Sol. Energy Mater. Sol. Cells, vol. 267, p. 112726, Apr. 2024,
doi: 10.1016/j.solmat.2024.112726.
[146] R. J. Wieser et al., “Field retrieved photovoltaic backsheet survey from diverse climate
zones: Analysis of degradation patterns and phenomena,” Sol. Energy, vol. 259, pp. 49 –
62, Jul. 2023, doi: 10.1016/j.solener.2023.04.061.
[147] S. Uličná, A. Sinha, D. C. Miller, B. M. Habersberger, L. T. Schelhas, and M. Owen-Bellini,
“PV encapsulant formulations and stress test conditions influence dominant degradation
mechanisms,” Sol. Energy Mater. Sol. Cells , vol. 255, p. 112319, Jun. 2023, doi:
10.1016/j.solmat.2023.112319.
[148] R. Heidrich, M. Lüdemann, A. Mordvinkin, and R. Gottschalg, “Diffusion of UV Additives in
Ethylene-Vinyl Acetate Copolymer Encapsulants and the Impact on Polymer Reliability,”
IEEE J. Photovoltaics , vol. 14, no. 1, pp. 131 –139, Jan. 2024, doi:
10.1109/JPHOTOV.2023.3333198.
[149] G. Oreski et al., Designing New Materials for Photovoltaics: Opportunities for Lowering
Cost and Increasing Performance through Advanced Material Innovations [IEA-PVPS T13-
13:2021]. 2021. [Online]. Available: https://iea -pvps.org/key-topics/designing-new-
materials-for-photovoltaics/
[150] S. Suzuki, T. Tanahashi, T. Doi, and A. Masuda, “Acceleration of degradation by highly
accelerated stress test and air-included highly accelerated stress test in crystalline silicon
photovoltaic modules,” Jpn. J. Appl. Phys. , vol. 55, no. 2, p. 022302, Feb. 2016, doi:
10.7567/JJAP.55.022302.
[151] A. Sinha et al., “UV‐induced degradation of high‐efficiency silicon PV modules with different
cell architectures,” Prog. Photovoltaics Res. Appl. , vol. 31, no. 1, pp. 36 –51, Jan. 2023,
doi: 10.1002/pip.3606.
[152] J. S. Stein et al. , Best Practices for the Optimization of Bifacial Photovoltaic Tracking
Systems [IEA -PVPS T13 -26:2024]. 2024. [Online]. Available: https://iea-pvps.org/key-
topics/best-practices-for-the-optimization-of-bifacial-photovoltaic-tracking-systems/
[153] P. G. Kosmopoulos et al., “Dust impact on surface solar irradiance assessed with model
simulations, satellite observations and ground -based measurements,” Atmos. Meas.
Tech., vol. 10, no. 7, pp. 2435–2453, 2017, doi: 10.5194/amt-10-2435-2017.
[154] L. Micheli, F. Almonacid, J. G. Bessa, Á. Fernández -Solas, and E. F. Fernández, “The
impact of extreme dust storms on the national photovoltaic energy supply,” Sustain. Energy
Technol. Assessments, vol. 62, p. 103607, Feb. 2024, doi: 10.1016/j.seta.2024.103607.
[155] F. Wiesinger, G. S. Vicente, A. Fernández-García, F. Sutter, Á. Morales, and R. Pitz-Paal,
“Sandstorm erosion testing of anti-reflective glass coatings for solar energy applications,”

## Página 85

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
85
Sol. Energy Mater. Sol. Cells , vol. 179, no. September 2017, pp. 10 –16, 2018, doi:
10.1016/j.solmat.2018.02.018.
[156] L. Micheli, M. G. Deceglie, and M. Muller, “Mapping Photovoltaic Soiling Using Spatial
Interpolation Techniques,” IEEE J. Photovoltaics , vol. 9, no. 1, pp. 272 –277, Jan. 2019,
doi: 10.1109/JPHOTOV.2018.2872548.
[157] L. Micheli and M. Muller, “On the uncertainty of estimating photovoltaic soiling using nearby
soiling data,” e-Prime - Adv. Electr. Eng. Electron. Energy, vol. 3, no. January, p. 100120,
2023, doi: 10.1016/j.prime.2023.100120.
[158] M. Coello and L. Boyle, “Simple Model for Predicting Time Series Soiling of Photovoltaic
Panels,” IEEE J. Photovoltaics , vol. 9, no. 5, pp. 1382 –1387, Sep. 2019, doi:
10.1109/JPHOTOV.2019.2919628.
[159] K. S. Anderson, C. W. Hansen, W. F. Holmgren, A. R. Jensen, M. A. Mikofski, and A.
Driesse, “Pvlib Python: 2023 Project Update,” J. Open Source Softw. , vol. 8, no. 92, p.
5994, 2023, doi: 10.21105/joss.05994.
[160] L. Micheli, G. P. Smestad, J. G. Bessa, M. Muller, E. F. Fernandez, and F. Almonacid,
“Tracking Soiling Losses: Assessment, Uncertainty, and Challenges in Mapping,” IEEE J.
Photovoltaics, vol. 12, no. 1, pp. 114 –118, Jan. 2022, doi:
10.1109/JPHOTOV.2021.3113858.
[161] K. Ilse et al., “Techno-Economic Assessment of Soiling Losses and Mitigation Strategies
for Solar Power Generation,” Joule, vol. 3, no. 10, pp. 2303 –2321, Oct. 2019, doi:
10.1016/j.joule.2019.08.019.
[162] International Electrotechnical Commission, “IEC 61724 -1 - Photovoltaic System
Performance Monitoring —Guidelines for Measurement, Data Exchange, and Analysis
(Part 1),” IEC, Geneva, Switzerland, 2017.
[163] I. Al Siyabi, S. Khanna, T. Mallick, and S. Sundaram, “Experimental and numerical study
on the effect of multiple phase change materials thermal energy storage system,” J. Energy
Storage, vol. 36, no. December 2020, p. 102226, 2021, doi: 10.1016/j.est.2020.102226.
[164] M. Halwachs et al. , “Statistical evaluation of PV system performance and failure data
among different climate zones,” Renew. Energy, vol. 139, pp. 1040–1060, Aug. 2019, doi:
10.1016/j.renene.2019.02.135.
[165] D. C. Jordan, T. J. Silverman, B. Sekulic, and S. R. Kurtz, “PV degradation curves: non -
linearities and failure modes,” Prog. Photovoltaics Res. Appl., vol. 25, no. 7, pp. 583–591,
2017, doi: 10.1002/pip.2835.
[166] G. C. Eder et al. , “Climate specific accelerated ageing tests and evaluation of ageing
induced electrical, physical, and chemical changes,” Prog. Photovoltaics Res. Appl. , vol.
27, no. 11, pp. 934–949, Nov. 2019, doi: 10.1002/pip.3090.
[167] B. Brune et al., “Connecting material degradation and power loss of PV modules using
advanced statistical methodology,” Sol. Energy Mater. Sol. Cells, vol. 260, p. 112485, Sep.
2023, doi: 10.1016/j.solmat.2023.112485.
[168] M. Owen-Bellini et al., “Towards validation of combined-accelerated stress testing through
failure analysis of polyamide-based photovoltaic backsheets,” Sci. Rep., vol. 11, no. 1, p.
2019, Jan. 2021, doi: 10.1038/s41598-021-81381-7.
[169] G. Eder et al., “COLOURED BIPV Market, research and development IEA PVPS Task 15,

## Página 86

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

86
Report IEA -PVPS T15 -07: 2019,” p. 57, 2019, [Online]. Available: http://iea -
pvps.org/index.php?id=task15
[170] G. C. Eder et al. , “Climate specific accelerated ageing tests,” in 2019 IEEE 46th
Photovoltaic Specialists Conference (PVSC) , IEEE, Jun. 2019, pp. 2398 –2405. doi:
10.1109/PVSC40753.2019.8981293.
[171] IEC, “Guidelines for qualifying PV modules, components and materials for operation at high
temperatures [IEC TS 63126:2020],” 2020. [Online]. Available:
https://webstore.iec.ch/en/publication/59551
[172] IEC, “Corrigendum 1 - Guidelines for qualifying PV modules, components and materials
for operation at high temperatures [IEC TS 63126:2020/COR1:2022],” 2022. doi:
https://webstore.iec.ch/en/publication/78434.
[173] IEC, “Photovoltaic (PV) module safety qualification - Part 1: Requirements for construction
[IEC 61730 -1:2023],” 2023. [Online]. Available:
https://webstore.iec.ch/en/publication/59803
[174] G. C. Eder, Y. Voronko, C. Hirschl, R. Ebner, G. Újvári, and W. Mühleisen, “Non -
Destructive Failure Detection and Visualization of Artificially and Naturally Aged PV
Modules,” Energies, vol. 11, no. 5, p. 1053, Apr. 2018, doi: 10.3390/en11051053.
[175] G. Oreski et al. , “Properties and degradation behaviour of polyolefin encapsulants for
photovoltaic modules,” Prog. Photovoltaics Res. Appl. , vol. 28, no. 12, pp. 1277 –1288,
Dec. 2020, doi: 10.1002/pip.3323.
[176] M. Koehl, D. Philipp, N. Lenck, and M. Zundel, “Development and application of a UV light
source for PV-module testing,” N. G. Dhere, J. H. Wohlgemuth, and D. T. Ton, Eds., Aug.
2009, p. 741202. doi: 10.1117/12.825939.
[177] H. X. Wang, M. A. Muñoz -García, G. P. Moreda, and M. C. Alonso -García, “Optimum
inverter sizing of grid -connected photovoltaic systems based on energetic and economic
considerations,” Renew. Energy , vol. 118, pp. 709 –717, 2018, doi:
10.1016/j.renene.2017.11.063.
[178] J. Balfour et al., “Masking of photovoltaic system performance problems by inverter clipping
and other design and operational practices,” Renew. Sustain. Energy Rev., vol. 145, no.
March, p. 111067, 2021, doi: 10.1016/j.rser.2021.111067.
[179] L. Micheli, M. Muller, M. Theristis, G. P. Smestad, F. Almonacid, and E. F. Fernández,
“Quantifying the impact of inverter clipping on photovoltaic performance and soiling losses,”
Renew. Energy, vol. 225, p. 120317, May 2024, doi: 10.1016/j.renene.2024.120317.
[180] M. Matam, R. M. Smith, and H. Seigneur, “PV Module Degradation Due to Frequent and
Prolonged Inverter Clipping: A Preliminary Study,” Conf. Rec. IEEE Photovolt. Spec. Conf.,
vol. 2022-June, pp. 596–603, 2022, doi: 10.1109/PVSC48317.2022.9938850.
[181] P. S. Molina, “Case study: When trackers are blown away, you can’t blame the wind,” pv
magazine. Accessed: Jan. 24, 2025. [Online]. Available: https://www.pv -
magazine.com/2022/08/18/case-study-when-trackers-are-blown-away-you-cant-blame-
the-wind/
[182] S. Mitterhofer et al., “Measurement and Simulation of Moisture Ingress in PV Modules in
Various Climates,” IEEE J. Photovoltaics , vol. 14, no. 1, pp. 140 –148, Jan. 2024, doi:
10.1109/JPHOTOV.2023.3323808.

## Página 87

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
87
[183] E. Simsek, M. J. Williams, and L. Pilon, “Effect of dew and rain on photovoltaic solar cell
performances,” Sol. Energy Mater. Sol. Cells , vol. 222, p. 110908, Apr. 2021, doi:
10.1016/j.solmat.2020.110908.
[184] P. Hacke et al., “Testing and analysis for lifetime prediction of crystalline silicon PV modules
undergoing degradation by system voltage stress,” in 2012 IEEE 38th Photovoltaic
Specialists Conference (PVSC) PART 2 , IEEE, Jun. 2012, pp. 1 –8. doi: 10.1109/PVSC-
Vol2.2012.6656746.
[185] Y. Chen et al., “Field Investigations of Potential-Induced Degradation (PID) for Crystalline
Silicon PV Panels in Different Climates,” in 2017 IEEE 44th Photovoltaic Specialist
Conference (PVSC), IEEE, Jun. 2017, pp. 1922–1926. doi: 10.1109/PVSC.2017.8366476.
[186] H. Han et al., “Degradation analysis of crystalline silicon photovoltaic modules exposed
over 30 years in hot -humid climate in China,” Sol. Energy, vol. 170, no. December 2017,
pp. 510–519, 2018, doi: 10.1016/j.solener.2018.05.027.
[187] A. Ndiaye, A. Charki, A. Kobi, C. M. F. Kébé, P. A. Ndiaye, and V. Sambou, “Degradations
of silicon photovoltaic modules: A literature review,” Sol. Energy, vol. 96, pp. 140 –151,
2013, doi: 10.1016/j.solener.2013.07.005.
[188] L. Vinayagam, “Cable reliability considerations and electrical issues in Floating Solar –
Experiences from 5 years’ of operation of the FPV testbed in Singapore,” in PV Magazine
Webinar - Waterproofed: new cable testing, standard for Floating PV, 2021.
[189] H. Liu, A. Kumar, and T. Reindl, “The Dawn of Floating Solar—Technology, Benefits, and
Challenges,” in Lecture Notes in Civil Engineering , Singapore, 2020, pp. 373 –383. doi:
10.1007/978-981-13-8743-2_21.
[190] H. Liu, V. Krishna, J. Lun Leung, T. Reindl, and L. Zhao, “Field experience and performance
analysis of floating PV technologies in the tropics,” Prog. Photovoltaics Res. Appl., vol. 26,
no. 12, pp. 957–967, Dec. 2018, doi: 10.1002/pip.3039.
[191] S. Ghazi and K. Ip, “The effect of weather conditions on the efficiency of PV panels in the
southeast of UK,” Renew. Energy , vol. 69, pp. 50 –59, Sep. 2014, doi:
10.1016/j.renene.2014.03.018.
[192] M. Piliougine et al., “Comparative analysis of energy produced by photovoltaic modules
with anti-soiling coated surface in arid climates,” Appl. Energy, vol. 112, pp. 626–634, Dec.
2013, doi: 10.1016/j.apenergy.2013.01.048.
[193] K. K. Ilse, B. W. Figgis, V. Naumann, C. Hagendorf, and J. Bagdahn, “Fundamentals of
soiling processes on photovoltaic modules,” Renew. Sustain. Energy Rev. , vol. 98, no.
September, pp. 239–254, Dec. 2018, doi: 10.1016/j.rser.2018.09.015.
[194] M. Köntges et al., Assessment of photovoltaic module failures in the field [IEA-PVPS T13-
09:2017]. 2017. [Online]. Available: https://iea -pvps.org/key-topics/report-assessment-of-
photovoltaic-module-failures-in-the-field-2017/
[195] B. Figgis and M. Helal, “Condensation Characterization for PV Soiling,” IEEE J.
Photovoltaics, vol. 12, no. 6, pp. 1522 –1526, 2022, doi:
10.1109/JPHOTOV.2022.3202087.
[196] M. A. Shirakawa et al., “Microbial colonization affects the efficiency of photovoltaic panels
in a tropical environment,” J. Environ. Manage. , vol. 157, pp. 160 –167, 2015, doi:
10.1016/j.jenvman.2015.03.050.

## Página 88

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

88
[197] A. Eihorn et al., “Evaluation of soiling and potential mitigation approaches on photovoltaic
glass,” IEEE J. Photovoltaics, vol. 9, no. 1, 2019, doi: 10.1109/JPHOTOV.2018.2878286.
[198] S. Toth et al., “Soiling and cleaning: Initial observations from 5 -year photovoltaic glass
coating durability study,” Sol. Energy Mater. Sol. Cells , vol. 185, no. May, pp. 375 –384,
2018, doi: 10.1016/j.solmat.2018.05.039.
[199] A. Bonkaney, S. Madougou, and R. Adamou, “Impacts of Cloud Cover and Dust on the
Performance of Photovoltaic Module in Niamey,” J. Renew. Energy , vol. 2017, pp. 1 –8,
Sep. 2017, doi: 10.1155/2017/9107502.
[200] B. Sweerts, S. Pfenninger, S. Yang, D. Folini, B. van der Zwaan, and M. Wild, “Estimation
of losses in solar energy production from air pollution in China since 1960 using surface
radiation data,” Nat. Energy, vol. 4, no. 8, pp. 657 –663, Jul. 2019, doi: 10.1038/s41560 -
019-0412-4.
[201] D. Atsu, I. Seres, M. Aghaei, and I. Farkas, “Analysis of long -term performance and
reliability of PV modules under tropical climatic conditions in sub -Saharan,” Renew.
Energy, vol. 162, pp. 285–295, 2020, doi: 10.1016/j.renene.2020.08.021.
[202] VDMA, “International Technology Roadmap for Photovoltaic (Results 2023),” Frankfurt am
Main, Germany, 2024.
[203] X. Wu et al., “Enhancing the reliability of TOPCon technology by laser -enhanced contact
firing,” Sol. Energy Mater. Sol. Cells , vol. 271, p. 112846, Jul. 2024, doi:
10.1016/j.solmat.2024.112846.
[204] P. M. Sommeling, J. Liu, and J. M. Kroon, “Corrosion effects in bifacial crystalline silicon
PV modules; interactions between metallization and encapsulation,” Sol. Energy Mater.
Sol. Cells, vol. 256, p. 112321, Jul. 2023, doi: 10.1016/j.solmat.2023.112321.
[205] L. Gnocchi, O. A. Arruti, C. Ballif, and A. Virtuani, “A comprehensive physical model for the
sensitivity of silicon heterojunction photovoltaic modules to water ingress,” Cell Reports
Phys. Sci., vol. 5, no. 1, p. 101751, Jan. 2024, doi: 10.1016/j.xcrp.2023.101751.
[206] O. Arriaga Arruti, L. Gnocchi, Q. Jeangros, C. Ballif, and A. Virtuani, “Potential ‐induced
degradation in bifacial silicon heterojunction solar modules: Insights and mitigation
strategies,” Prog. Photovoltaics Res. Appl. , vol. 32, no. 5, pp. 304 –316, May 2024, doi:
10.1002/pip.3765.
[207] C. Sen et al., “Buyer aware: Three new failure modes in TOPCon modules absent from
PERC technology,” Sol. Energy Mater. Sol. Cells , vol. 272, p. 112877, Aug. 2024, doi:
10.1016/j.solmat.2024.112877.
[208] K. Whitfield, “Degradation Processes and Mechanisms of PV System Adhesives/Sealants
and Junction Boxes,” in Durability and Reliability of Polymers and Other Materials in
Photovoltaic Modules , Elsevier, 2019, pp. 235 –254. doi: 10.1016/B978 -0-12-811545-
9.00010-0.
[209] International Electrotechnical Commission (IEC), “IEC 529 (BSEN60529:1991),” 1991.
[210] W. Luo et al., “Performance loss rates of floating photovoltaic installations in the tropics,”
Sol. Energy , vol. 219, no. December 2020, pp. 58 –64, 2021, doi:
10.1016/j.solener.2020.12.019.
[211] A. Ayaz et al., “Self-cleaning of glass surface to maximize the PV cell efficiency,” IOP Conf.
Ser. Mater. Sci. Eng. , vol. 899, no. 1, p. 012006, Jul. 2020, doi: 10.1088/1757 -

## Página 89

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates
89
899X/899/1/012006.
[212] A. Syafiq et al., “Application of transparent self -cleaning coating for photovoltaic panel: a
review,” Curr. Opin. Chem. Eng. , vol. 36, p. 100801, Jun. 2022, doi:
10.1016/j.coche.2022.100801.
[213] T. M. Walsh, Z. Xiong, Y. S. Khoo, A. A. O. Tay, and A. G. Aberle, “Singapore Modules -
Optimised PV Modules for the Tropics,” Energy Procedia, vol. 15, pp. 388–395, 2012, doi:
10.1016/j.egypro.2012.02.047.
[214] E. Bellini, “Solar module for floating PV from Hyundai,” pv magazine, Jul. 2021. [Online].
Available: https://www.pv -magazine.com/2021/07/19/solar-module-for-floating-pv-from-
hyundai/
[215] R. Sengupta, “HJT Module For Floating PV Application At SNEC 2024,” Taiyang News.
Accessed: Jan. 24, 2025. [Online]. Available: https://taiyangnews.info/technology/hjt -
module-for-floating-pv-application-at-snec-2024
[216] A. M. Nobre, “Short -term solar irradiance forecasting and photovoltaic systems
performance in a tropical climate in Singapore,” Universidade Federal de Santa Catarina,
2015.
[217] M. Mani and R. Pillai, “Impact of dust on solar photovoltaic (PV) performance: Research
status, challenges and recommendations,” Renew. Sustain. Energy Rev. , vol. 14, no. 9,
pp. 3124–3131, 2010, doi: 10.1016/j.rser.2010.07.065.
[218] Y. S. Khoo et al., “Optimal orientation and tilt angle for maximizing in-plane solar irradiation
for PV applications in Singapore,” IEEE J. Photovoltaics, vol. 4, no. 2, pp. 647–653, 2014,
doi: 10.1109/JPHOTOV.2013.2292743.
[219] W. Luo et al., “Photovoltaic module failures after 10 years of operation in the tropics,”
Renew. Energy, vol. 177, pp. 327–335, 2021, doi: 10.1016/j.renene.2021.05.145.
[220] W. Luo et al., “Analysis of the Long-Term Performance Degradation of Crystalline Silicon
Photovoltaic Modules in Tropical Climates,” IEEE J. Photovoltaics, vol. 9, no. 1, pp. 266 –
271, 2019, doi: 10.1109/JPHOTOV.2018.2877007.
[221] VDMA, “International Technology Roadmap for Photovoltaic (Results 2023),” Frankfurt am
Main, Germany, 2024. [Online]. Available: https://itrpv.vdma.org/en/
[222] JinkoSolar, “TigerNeo 66HL4M -BDV.” Accessed: Jan. 24, 2025. [Online]. Available:
https://jinkosolarcdn.shwebspace.com/uploads/JKM605-630N-66HL4M-BDV-F3-EN.pdf
[223] S. C. S. Costa, L. L. Kazmerski, and A. S. A. C. Diniz, “Impact of soiling on Si and CdTe
PV modules: Case study in different Brazil climate zones,” Energy Convers. Manag. X, vol.
10, 2021, doi: 10.1016/j.ecmx.2021.100084.
[224] S. C. Silva Costa, A. S. A. C. Diniz, T. Duarte, S. Bhaduri, V. C. Santana, and L. L.
Kazmerski, “Performance of Soiled PV Module Technologies: Behavior Based on
Controverted Parameters,” Conf. Rec. IEEE Photovolt. Spec. Conf. , vol. 540, pp. 1 –5,
2019, doi: 10.1109/PVSC40753.2019.8980675.
[225] H. Qasem, T. R. Betts, H. Müllejans, H. Albusairi, and R. Gottschalg, “Dust -induced
shading on photovoltaic modules,” 2012, doi: 10.1002/pip.
[226] L. Micheli, E. F. Fernández, M. Muller, G. P. Smestad, and F. Almonacid, “Selection of
optimal wavelengths for optical soiling modelling and detection in photovoltaic modules,”

## Página 90

Task 13 Reliability and Performance of Photovoltaic Systems – Optimization of Photovoltaic Systems for Different Climates

90
Sol. Energy Mater. Sol. Cells , vol. 212, no. January, p. 110539, Aug. 2020, doi:
10.1016/j.solmat.2020.110539.
[227] A. S. A. C. Diniz, T. P. Duarte, S. A. C. Costa, D. S. Braga, V. C. Santana, and L. L.
Kazmerski, “Soiling Spectral and Module Temperature Effects: Comparisons of Competing
Operating Parameters for Four Commercial PV Module Technologies,” Energies, vol. 15,
no. 15, p. 5415, Jul. 2022, doi: 10.3390/en15155415.
[228] IEA PVPS Task 13, “Impact of Decisions on Economic KPIs [IEA-PVPS T13-34:2025].”

## Página 91

91
UNCLASSIFIED - NON CLASSIFIÉ
