# IEA-PVPS-T13-31-2025-REPORT-Floating-PV-Plants

Fonte original: `IEA-PVPS-T13-31-2025-REPORT-Floating-PV-Plants.pdf`

## Página 1

carlos

© BayWa r.e.
Task 13  Reliability and Performance of Photovoltaic Systems

Floating Photovoltaic Power
Plants: A Review of Energy
Yield, Reliability, and
Maintenance
2025
PVPS
Report IEA-PVPS T13-31:2025

## Página 2

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance

What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organization for Ec onomic
Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with a belief that the future of energy
security and sustainability starts with global collaboration. The programmes are made up of 6,000 experts across government, academia,
and industry dedicated to advancing common research and the application of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCPs within the IEA and was established in 1993. The mission
of the programme is to “enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone
in the transition to sustainable energy systems.” To achieve this, the Programme’s participants have undertaken a variety of joint research
projects in PV power systems applications. The overall programme is headed by an Executive Commit tee, comprised of one delegate from
each country or organisation member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.
The IEA PVPS participating countries are Australia, Austria, Belgium, Canada, China, Denmark, Finland, France, Germany,  India, Israel,
Italy, Japan, Korea, Malaysia, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain, Sweden, Switzerland, Thailand, Turkey, the
United Kingdom, and the United States of America. The European Commission, Solar Power Europe and the Solar Energy Research Institute
of Singapore are also members.
Visit us at: www.iea-pvps.org
What is IEA PVPS Task 13?
Within the framework of IEA PVPS, Task 13 aims to provide support to market actors working to improve the operation, the reliability and the
quality of PV components and systems. Operational data from PV systems in different climate zones compiled within t he project will help
provide the basis for estimates of the current situation regarding PV reliability and performance.
The general setting of Task 13 provides a common platform to summarize and report on technical aspects affecting the quality, performance,
reliability and lifetime of PV systems in a wide variety of environments and applications. By working together across national boundaries, we
can all take advantage of research and experience from each member country and combine and i ntegrate this knowledge into valuable
summaries of best practices and methods for ensuring PV systems perform at their optimum and continue to provide competitive return on
investment.
Task 13 has so far managed to create the right framework for the calculations of various parameters that can give an indication of the quality
of PV components and systems. The framework is now there and can be used by the industry who has expressed appreciation towards the
results included in the high-quality reports.
The IEA PVPS countries participating in Task 13 are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany,
Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand, and the United States of America.

DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and
publications of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual  member countries.
COPYRIGHT STATEMENT
This content may be freely used, copied and redistributed, provided appropriate credit is given (please refer to the ‘Suggested Citation’). The exception is that
some licensed images may not be copied, as specified in the individual image captions.
SUGGESTED CITATION
Selj, J., Wieland, S., Tsanakas, I. (2025). Selj, J., Jahn, U., Maugeri, G. (Eds.), Floating Photovoltaic Power Plants: A Review of Energy Yield, Reliability, and
Maintenance (Report No. T13-31:2025). IEA PVPS Task 13. https://iea-pvps.org/key-topics/floating-pv-plants/
COVER PICTURE
PV Floating System in Zwolle, Netherlands. Copyright BayWa r.e.

## Página 3

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance

3

INTERNATIONAL ENERGY AGENCY
PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

IEA PVPS Task 13
Reliability and Performance
of Photovoltaic Systems

Floating Photovoltaic Power Plants: A Review of
Energy Yield, Reliability, and Maintenance

Report IEA-PVPS T13-31:2025
April 2025

## Página 4

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
4

AUTHORS
Main Authors
 Josefine Selj, IFE, Kjeller, Norway
Stefan Wieland, Fraunhofer ISE, Freiburg, Germany
Ioannis Tsanakas, CEA INES, Le Bourget-du-Lac, France

Contributing Authors

Wilfried van Sark, Utrecht University, Utrecht, the Netherlands
Nathan Roosloot, IFE, Kjeller, Norway
Gaute Otnes, IFE, Kjeller, Norway
Vilde S. Nysted, IFE, Kjeller, Norway
Minne de Jong, TNO, Eindhoven, the Netherlands
Jan Kroon, TNO, Petten, the Netherlands
Leonardo Micheli, Sapienza University of Rome, Italy
Sara Golroodbari, Utrecht University, Utrecht, the Netherlands
Christian Reise, Fraunhofer ISE, Freiburg, Germany
Anna Heimsath, Fraunhofer ISE, Freiburg, Germany
Andreas Beinert, Fraunhofer ISE, Freiburg, Germany
Christian Gertig, Everoze, Bristol, United Kingdom
Josh Stein, Sandia, Albuquerque, United States of America
Kevin Anderson, Sandia, Albuquerque, United States of America
Emilio Muñoz, University of Jaén, Jaén, Spain
Matthew Berwind, Fraunhofer ISE, Freiburg, Germany
Adam R. Jensen, Technical University of Denmark, Copenhagen, Denmark
Carlos D. Rodríguez-Gallegos, RINA Consulting, Australia
Oktoviano Gandhi, Solar Energy Research Institute of Singapore, Singapore
Lokesh Vinayagam, Solar Energy Research Institute of Singapore, Singapore
Theodoros Makris, RWE, Germany
Ingrid Hädrich, Fraunhofer ISE, Freiburg, Germany
Christian Reichel, Fraunhofer ISE, Freiburg, Germany
Suraj Ravindrababu, Fraunhofer ISE, Freiburg, Germany

Editors
 Josefine Selj, IFE, Kjeller, Norway
Giosuè Maugeri, RSE, Italy
Ulrike Jahn, Fraunhofer CSP, Halle, Germany

## Página 5

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
5

TABLE OF CONTENTS
Acknowledgements ................................ ................................ ................................ .. 6
List of abbreviations ................................ ................................ ................................ . 7
Executive summary ................................ ................................ ................................ .. 9
 Introduction ................................ ................................ ................................ ...... 12
 FPV Energy Yield ................................ ................................ ............................ 16
2.1 Meteorological input data for FPV ................................ ........................... 17
2.2 FPV technology overview ................................ ................................ ....... 17
2.3 Energy production estimates for FPV ................................ ..................... 20
2.4 Modelling yield for FPV systems ................................ ............................. 32
2.5 Uncertainty analysis ................................ ................................ ............... 35
 Reliability of Floating PV ................................ ................................ .................. 37
3.1 Defining degradation ................................ ................................ .............. 38
3.2 Driving degradation – describing FPV specific stressors ........................ 39
3.3 Understanding and quantifying degradation – sources of information ..... 41
 Operation and Maintenance of Floating PV ................................ ..................... 49
4.1 Instrumentation ................................ ................................ ....................... 49
4.2 Main O&M actions, importance and best practices ................................ . 50
4.3 Failure modes and effects analysis in O&M: example for FPV ................ 54
4.4 O&M budgeting – Cost aspects ................................ ..............................  57
4.5 Outlook: O&M challenges and opportunities ................................ ........... 58
 Conclusion................................ ................................ ................................ ....... 60
References ................................ ................................ ................................ ............. 61

## Página 6

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
6

ACKNOWLEDGEMENTS
This report received valuable contributions from several IEA -PVPS Task 13 members and
other international experts.
The contributors to the report have received funding of their work through several projects and
funding bodies, as listed below.
This report is supported by the German Federal Ministry for Economic Affairs and Climate
Action (BMWK) under contract no. 03EE1120B.
This report is supported by the Research Council of Norway, through the projects HydroSun
328642 and Predict 344524.
This report is supported by the Danish Energy Agency through grant no. 134223-496801.
This report was supported by the U.S. Department of Energy’s Office of Energy Efficiency and
Renewable Energy (EERE) under the Solar Energy Technologies Office Award Number
52788. Sandia National Laboratories is a multimission laboratory managed and operat ed by
National Technology & Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of
Honeywell International Inc., for the U.S. Department of Energy’s National Nuclear Security
Administration under contract DE-NA0003525.

## Página 7

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
7

LIST OF ABBREVIATIONS
BOS Balance of system
CAPEX Capital Expenditures
CFD Computational Fluid Dynamics
EU European Union
EYA Energy yield assessment
FEM Finite element method
FMEA Failure modes and effects analysis
FPV Floating photovoltaics
FRP  Fiber-reinforced plastic
GPV
HDPE
Ground-based photovoltaics
High-density polyethylene
HJT Heterojunction
IAV Inter-annual variability
IEA
IEC
I-V
International Energy Agency
International Electrotechnical Commission
Current-Voltage
LCOE
LeTiD
LSLR
Levelized cost of electricity
Light and elevated temperature induced degradation
Least squares linear regression
MPPT Maximum power point tracker
NIR Near infrared
OLS Ordinary least squares
O&M Operation and Maintenance
PERC Passivated emitted and rear contact
PID Potential induced degradation
PLR Performance loss rate
POA Plane-of-Array irradiance
PV Photovoltaics
RH Relative humidity
ROV Remotely operated vehicles
RPN Risk priority number
SC Short circuit
SCADA Supervisory Control and Data Acquisition
SR Shading ratio
SSC Sea State Codes
STL
STC
Seasonal and trend decomposition
Standard test conditions
TopCON Tunnel oxide passivated contact
TRL Technology readiness level
UAV Unmanned Aerial Vehicle
UV Ultraviolet
VIS Visible

## Página 8

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
8

WIL Wave-induced losses
WIML Wave-induced mismatch losses
WVTR Water vapor transmission rate
WS Wind speed
YoY Year-on-Year

## Página 9

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
9

EXECUTIVE SUMMARY
Photovoltaic (PV) systems are essential for the transition to sustainable energy, reducing fossil
fuel dependence and mitigating climate change. Although PV requires minimal land area  —
PV can meet the European Union's energy needs using only 0.26% of its land  — space for
deployment is often scarce in densely populated regions. Floating photovoltaics (FPV) offer an
effective solution to land-use challenges by installing PV systems on floating structures in water
bodies. FPV is a growing niche within PV with a cumulative installed capacity reaching 7.7 GW
globally by 2023. Almost 90% of the installed FPV capacity is in Asia, with close to 50% of in
China alone, while the Netherlands and France are the largest markets outside Asia [3]. FPV
shows strong potential to support climate targets, but still faces challenges like regulatory
barriers, cost competitiveness compared to ground-based PV (GPV), and uncertainties about
environmental impacts and system reliability.  FPV systems are currently installed mainly on
sheltered inland waters, such as quarry lakes, irrigation ponds and reservoirs.
FPV technical standards are still being developed. Guidelines have been published by the
World Bank, DNV, and Solar Power Europe,  and emerging national standards from South
Korea, China, and Singapore address design, components, and safety. The International
Electrotechnical Commission (IEC) is working on formal standards for floats, mooring systems,
and electrical connect ors. However, the published best practices lack quantitative guidance
for yield modelling and reliability, which this report aims to address. It provides data -driven
insights, models, and parameters  essential for accurate energy yield, reliability, and
maintenance predictions over FPV systems' lifetimes.
ENERGY YIELD ASSESSMENT
The report provides guidelines and quantitative recommendations for the accurate energy yield
assessment (EYA) of FPV systems, a key factor for determining the levelized cost of electricity
and project profitability. Current models for EYA are insufficient, lacking reliable data for critical
parameters like module temperature, wave -induced losses, soiling losses, and performance
loss rates. Standard modelling tools do not adequately cover FPV-specific needs, and existing
meteorological databases often exclu de sea and coastal areas, which limits FPV yield
estimation. This chapter identifies essential parameters and highlights knowledge gaps in
meteorological data, energy production modelling, and uncertainty analysis that distinguish
FPV EYA from that of GPV.
1. Meteorological Data Requirements : The report highlights the need for improved
meteorological data tailored to FPV, as the water-based environment affects variables
like irradiance, wind, and temperature. It is uncertain how this affects  prediction
accuracy for FPV.
2. Thermal Losses: Thermal performance depends on the FPV system design. Modelling
tools, such as PVsyst and pvlib, need to incorporate these specifics for more accurate
yield estimates.
3. Wave-Induced Losses: Wave motion affects irradiance by altering module tilt and
creating irradiance non -uniformity. No complete model for wave -induced losses
currently exists and the report encourages field data collection to improve accuracy in
yield modelling.
4. Soiling Losses: FPV systems may experience unique soiling challenges, including
bird droppings and other debris from surrounding ecosystems.

## Página 10

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
10

The report underscores that FPV yield estimation tools and methods are still evolving, and it
encourages improved empirical studies and data-sharing to refine modelling approaches and
align them with the distinctive characteristics of FPV installations.
RELIABILITY
When assessing the reliability of an FPV system, one faces important knowledge gaps and
challenges. First, the stress profiles  experienced by components in a FPV installation are
neither well understood nor quantified and will vary a lot depending on float technology and
water body conditions. Second, open information and systematic studies on observed
degradation and field failures remain scarce, as are studies of performance loss rates (PLR).
And third, as a result of the first two points, there is no accelerated stress testing protocol
developed for component reliability evaluation. In the following, each of these three topics will
be further discussed.
The term degradation denotes the gradual process of change in characteristics with
operational time of a material / component / system triggered by stress impact. Typical ly, we
distinguish between three types of degradation: reversible degradation, irreversible
degradation, and failures. For FPV, the balance of system  components may be even more
critical than the PV modules. Junction boxes, cables, connectors, and related protecting
materials may suffer from additional stress compared to GPV systems. The report provides an
overview of environmental stressors in the operating environment of FPV systems, and finally
discusses three different sources for quantification of degradation effects:
1. Field data: collection of long-term field data is indispensable for accurate identification of
failure modes and the design of appropriate testing protocols . As the available field data
on failures and degradation is very limited, performance stability is measured through long-
term trends in historical production data . Three commonly used statistical methods are
deployed to calculate the PLR through historical PV performance and climatic data:
Ordinary Least Squares (OLS), seasonal and trend decomposition using locally weighted
scatterplot smoothing (STL), as well as Year-on-Year (YoY). These methods are based on
determining trends in the historical data. The major drawback of statistical methods is that
they do not trace the correlation of the evaluated degradation rates with the climatic
variables and degradation processes. Despite the significant number of FPV systems that
have now been operating for several years, long-term FPV performance studies are rare.
A study by SERIS using three years of data from a large FPV test bed found PLRs between
-0.7% and -0.5% per year, like those of nearby rooftop PV.
2. Laboratory: in the lab environment, accelerated stress tests enable reliability screening of
key components in short timeframes, to identify and mitigate quality issues before they
manifest as problems in actual installations. A challenge with laboratory testing for FPV is
that there are no  standards on reliability testing of FPV components,  and few field
measurements of stressors and field degradation. IEC standards that can be relevant for
FPV components are summarized in this section.
3. Simulation Models: simulations are one convenient option to overcome the lack of
experimental (long-term) data, and to capture the correlations between the degradation
rates and the stressors/climatic variables. However, we emphasize the importance of using
validated simulation models to obtain reliable results.  For FPV, four types of simulations
are of particular interest to study the influence of single stressors: a) Wind loads through
Computational Fluid Dynamics (CFD) and mechanical simulations , b) Moisture ingress
through mass transport simulations , c) Hotspot formation through electrical and thermal
simulations, d) Thermally Induced Stress through thermal and mechanical simulations.

## Página 11

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
11

OPERATIONS & MAINTENANCE
There are currently no standards available that describe the recommended sensors and
procedures for monitoring of FPV power plants. Instrumentation requirements for GPV power
plants, including requirements with respect to accuracy and number according to the size of
the plant, can be found in IEC 61724-1.
The report  introduces a preliminary failure mode and effects analysis of technical and
operational challenges, and how these impact operation and maintenance (O&M).  Available
data is limited, and one can only anticipate that the occurrence and degree of severity for the
different events may change as more data is collected. A list of key aspects and considerations
when budgeting for FPV O&M projects is also provided.
FPV technology faces key R&D challenges, especially as installations scale up and offshore
projects expand. Major areas include:
• Monitoring and Remote Sensing: Remote FPV sites, especially offshore, struggle with
data transmission reliability and high communication costs. Advanced solutions using
drones and satellites can enhance monitoring and reduce O&M costs.
• Expert Dependence: FPV's complexity requires specialized experts (e.g., divers,
marine engineers) for maintenance and inspections, increasing costs and time. AI -
driven data analytics, Unmanned Aerial Vehicle ( UAV) based inspections, and
autonomous systems offer potential to reduce human intervention.
• Extreme Weather and Degradation: Marine environments introduce severe stressors
like corrosion and UV exposure, accelerating FPV component degradation. R&D in
advanced materials, protective designs, and robust emergency -response plans is
crucial to improve FPV durability.
• Environmental Impact and Regulations: Concerns on FPV effects on aquatic
ecosystems, such as water quality and habitat shading, call for eco -friendly designs
and regulatory standards that minimize harm and adapt O&M practices for
sustainability.

CONCLUSIONS
FPV offers a promising solution for expanding renewable energy without increasing land -use
pressures. However, the absence of regulatory frameworks and limited long-term data creates
uncertainty for developers, regulators, and investors, slowing FPV adoption. Rapid innovation
in the field often prioritizes confidentiality, even though the industry would benefit from open
data sharing. This report aims to support FPV development by building a knowledge base on
energy yield, reliability, and O&M  — areas where  FPV diverges from GPV. Key research
priorities include understanding FPV -specific stressors, improving predictive models,
automating O&M, and assessing environmental impacts. Addressing these gaps can lead to a
more mature, sustainable FPV industry, ready for broader deployment.

## Página 12

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
12

 INTRODUCTION
PV is a cornerstone in the transition to sustainable energy, and accelerated deployment is
essential to reduce reliance on fossil fuels and mitigate global warming. While PV systems
occupy relatively small amounts of land  — for instance, meeting the current energy demand
of the European Union (EU) with PV would require only 0.26% of its total land area [1] – land
availability for solar deployment is often limited in densely populated areas. One solution is to
deploy PV systems on water bodies. Floating Photovoltaics refers to mounting solar
photovoltaic systems on structures  that float on water. It is a relatively novel , but rapidly
growing technology,  exhibiting promising synergies with other usage of water bodies.

Figure 1. Annual and cumulative growth in deployment of FPV by installed capacity (MWp) and by percentage of
total global PV installations (%).
Figure 1 shows the cumulative and annual installed capacity of FPV since the first deployment
in 2007. The deployment has grown from just above 1.6 GW at the end of 2018 to 7.7 GW by
the end of 2023 [2]. Almost 90% of the installed FPV capacity is in Asia, with close to 50% of
in China alone [3], followed by Taiwan, India, Israel, Japan and South Korea. However, FPV
also holds potential to support the EU’s climate neutrality goals , with t he Netherlands and
France currently hosting the 7th and 10th largest FPV capacities [3]. As the technology matures,
Figure 2. Categorization of FPV as suggested by Solar Power Europe [1] and the WMO sea state codes [4].

## Página 13

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
13

FPV deployment is expected to accelerate further, but several barriers persist. Legislative
hurdles, cost competitiveness relative to ground -based PV, and uncertainties surrounding
environmental impact and reliability could impede global adoption.
The commercial
deployment of FPV
systems today is on
sheltered waters.
However, t here is
currently no  consensus
regarding how
deployment on different
types of water bodies
should be classified . Solar
Power Europe [1] suggests
a division between onshore
(or inland) FPV and marine
FPV, where onshore is
further separated into static
freshwater bodies, inner
waters, and larger inner
waters, while marine FPV is
separated into nearshore
FPV and offshore FPV, as
shown in  Figure 2 .
Another option is to use
the Sea State Codes
(SSC) of the World
Meteorological
Organization
(WMO). This scale
spans from no waves
(SSC 0) to wave
height > 14 m (SSC 9). The two may also be used in combination, although the suggested
wave height in [1] must be modified to fit with established WMO SSC codes. In this report, we
use the term inland FPV for deployment of FPV on freshwater bodies, while the term nearshore
FPV is used for deployment of FPV at sea, but close to the coastline.
This report is limited to address  inland and nearshore FPV, as some technologies may be
suited for both applications. The report does not cover offshore FPV applications, as both the
challenges it faces, and the FPV technologies under development for these conditions differ
significantly from inland and nearshore FPV.  The majority of current FPV installations in
Europe are deployed on quarry lakes, sandpit lakes, irrigation ponds and other man -made
water bodies. Figure 3 shows installations on a) a mining a nd quarry lake, b) a sandpit lake
and c) a hydropower dam.
The installation and operational costs will depend significantly on the category of application,
but focusing on sheltered waters (corresponding to FPV deployed at Static Freshwater bodies
and Inner waters), a cost premium of 20 -25% in Europe and USA respe ctively is estimated
compared to GPV [4], [5]. The CAPEX is highly affected by float costs, which are influenced
by wind and snow loads, as well as the efficiency of the PV modules. The CAPEX estimates
Figure 3. Installation of FPV on quarry lake, sandpit, and hydropower dam in Europe.

## Página 14

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
14

are also in line with a median CAPEX cost of 1.18 USD/W (2022), recently reported by SERIS
based on their comprehensive FPV database [3]. Of all projects installed in 2022 or earlier, 30
projects have reported CAPEX lower than 1 USD/W  and the lowest CAPEX reported for any
FPV project is 0.41 USD/W for 36 MW FPV in India [6].
The development of technical standards for (any type of) FPV systems is currently limited but
actively pursued by various  national and  international organi sations. These efforts aim to
address the unique challenges associated with deploying solar PV systems on water bodies.
The first comprehensive guideline was the ‘Floating Solar Handbook for Practitioners ’
published in 2019  [7]. The technical considerations covered by the handbook include site
selection and assessment, FPV system design and components, electrical safety measures,
as well as operation and maintenance procedures. Also published in 2019 were national
standards for PV modules in FPV applications by South Korea  [8] and for the high-density
polyethylene (HDPE) floats and structures by China [9], [10], [11], [12].
While the ‘Floating Solar Handbook for Practitioners ’ is targeted towards a more general
audience and includes non-technical aspects, more normative standards are provided by the
DNVGL-RP-0584 Recommended Practice  [13] and the Singapore Technical Reference TR
100:2022 [14]. DNVGL -RP-0584 was developed in a joint industry project with FPV
developers, investors, installers, and equipment suppliers. Meanwhile, Singapore's
TR 100:2022 modifie d the GPV standard IEC TS 62738:2018  [15] for FPV contexts  by
addressing the specific nature of FPV systems over water; also referencing other existing
standards from adjacent technologies such as the marine industry.
Efforts are ongoing in the IEC Technical Committee 82, Working Group 3 (TC82 WG3) to
formalise an international standard for FPV systems. This standard will also have links to two
other Recommended Practice s by DNV, which are currently underway to develop better
guidance on the floats (various types) and the anchoring & mooring systems. Similarly, IEC
TC82 WG2 plans to develop a standard for PV modules when deployed in FPV applications.
Generally, the key focus areas addressed in the technical standards include proper design,
component selection and implementation of FPV systems to ensure long-term durability and
reliability, including (but not limited to)  cables, floats, anchors, and mooring systems , taking
into account the exposure of components to high humidity, their possible submergence into
the water and the dynamic environmental conditions (combined wind, wave, and possibly tidal
forces). Ultimately, clear and comprehensive guidelines will boost FPV system design and
installation quality, as well as investor’s confidence and bankability.
While the published best practice reports from DNV [13], the World Bank [7], and Solar Power
Europe [1] provide valuable contributions to different areas within FPV, they fall short of offering
quantitative recommendations for energy yield modelling or addressing reliability and field
failures. The aim of this report is to address these gaps by focusing on topics at the forefront
of FPV research. Specifically, we provide observations, models, and quantitative parameters
to support the efficient and economically viable deployment of FPV systems. The report
examines factors influencing the energy yield over th e lifetime of FPV plants, along with the
associated O&M requirements, incorporating quantitative values where available.
Sustainability of  FPV power plants  represents a very wide and multifaceted topic,
encompassing everything from environmental impacts, carbon footprints, and recycling,  to
socio-economic and socio-cultural impacts.
With respect to environmental impacts, a wide range of both potential benefits and potential
adverse impacts have been discussed in  the scientific literature. Case  studies detailing the

## Página 15

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
15

impact of FPV power plants at specified sites are starting to appear  [16], [17], [18] as are
guidelines for monitoring [19] and impact assessment [20]. However, the impact depends on
the sensitivity of the water body itself, local climate, and FPV design and coverage, making it
is difficult to generalize the findings. Overall, the knowledge base on the environmental impact
of FPV power plants remains limited, and more research is needed.
IEA PVPS Task 12 published a report on Carbon Footprint Analysis of FPV in 2024  [21],
concluding that the two studied FPV technologies had a slightly greater carbon footprint than
the GPV references, but seven times lower than that of the grid mix in the countries where they
were installed (Germany and the Netherlands). The largest contribution to the carbon footprints
is from the manufacturing of the PV module (60% to 70%, depending on the system).
The scientific literature provides very little information on social impacts , and acceptance, of
FPV. Most large waterbodies provide extensive ecosystem services to local  communities
including fishery, irrigation water, recreation , tourism and transportation. While it is often
claimed that installing FPV instead of GPV will reduce the level of conflict for space, there are
few studies that can support these arguments [22].
A detailed discusson on sustainability of FPV is comprehensive and beyond the scope of this
report. We recommend that these aspects are dealt with in a separate report.

## Página 16

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
16

 FPV ENERGY YIELD
The purpose of this chapter is to provide concrete guidelines and quantitative
recommendations for a selection of parameters essential for accurate energy yield assessment
(EYA) of various FPV technologies. EYA, or modelling of the average yearly expected energy
production, is crucial for determining the levelized cost of electricity (LCOE) and, consequently,
the profitability of a project. The absence of published and validated values for parameters
used in EYA for FPV can hinder the development and investment in new FPV projects.
The toolbox for EYA of FPV is currently inadequate. Models that accurately estimate module
temperature and wave-induced losses (WIL) are not available in standard modelling software.
Soiling losses and performance loss rates (PLR) should ideally be based on published and
validated empirical values, but such values are currently unavailable. The validation of models
and empirical values is challenging due to the scarcity of h igh-quality data series that include
both production and weather data. Additionally, while meteorological data suitable for energy
production estimates for PV is readily available, coverage of sea and coastal areas is missing
from many databases and PV modelling tools. An important effort in this report is hence to
provide an overview of both what is known and current gaps in knowledge needed for accurate
EYA of FPV.
EYA can be divided into three components: meteorological input data, energy production
estimates, and uncertainty analysis. As good procedures for EYA exists for GPV, the focus in
this chapter is on the topics that separate EYA for FPV from GPV.
Section 2.1 provides a brief overview of current knowledge and knowledge gaps related to
meteorological data sets above water bodies.
Sections 2.2, 2.3, and 2.4 are concerned with energy production estimates. A challenge for
energy production estimates for FPV is the diversity of FPV technology. In Section 2.2, we give
a brief introduction  to FPV technologies and classification  schemes for the different
technologies. The quantitative losses and the models to describe them will depend on both
FPV technology and site/sea state, inferring that a broad set of data series spanning different
type of technologies and sites will be necessary to gai n a good understanding and validate
models and values in different conditions. We also address t he impact of technology design
choices on various losses. In S ection 2.3, we describe three loss mechanisms that are
important input to energy production estimates, and which differ from their GPV counterparts
in terms of value and/or origin: Thermal losses, WIL, and soiling losses. The impact of these
losses on different types of FPV technologies is, to the extent possible, quantified. The PLR is
also an important input to energy production estimates. However, as it represents a sum of
various degradation mechanisms, it is covered in Chapter 3 on Reliability. Section 2.4 provides
an overview of modelling options for FPV in the industry standard modelling software, PVsyst,
and in pvlib, commonly used in research and development.
The third part of an EYA is uncertainty analysis. To date, no published efforts are known for
quantifying uncertainties in crucial FPV modelling steps such as soiling or WIL. Section 2.5
summarizes the main methods to model uncertainty and provides advice on how to deal with
uncertainty analysis for EYA of FPV.

## Página 17

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
17

2.1 Meteorological input data for FPV
The long-term and short -term solar resource variability  represents the single greatest
uncertainty in a solar power plant’s predicted performance. Satellite-derived, and high-quality
historical solar radiation data sets covering at least 10 years are usually considered necessary
for the site selection of large solar energy systems [23].
Solar resource data above water  bodies has not been of interest to the providers of
meteorological data for solar power plants until recently.
There are currently no dedicated measures undertaken to ensure that the meteorological
parameters used in PV yield assessments are accurate above inland water bodies. For
nearshore- and offshore locations, the meteorological parameters are lacking in several of the
databases commonly used for solar power plants, including SARAH2 -PVGIS and ERA5 -
PVGIS. Meteorological parameters for nearshore locations  have recently been i mplemented
in Meteonorm (8) for PVsyst. In the new release of PVGIS, the databases will b e updated to
cover nearshore – 25 km towards the sea - to enable assessment of FPV close to the
coastlines. The spatial resolution for the coastal areas will be the same as for inland areas,
SARAH3’s native resolution at 0.05° x 0.05°, and ERA5 interpolated to the resolution of ERA5-
Land at 0.1° x 0.1° (A. Martinez, personal communication, May 17, 2024).
Historical data based on satellite imagery of meteorological data above sea can be obtained
from the NASA POWER service [24]. Comparing the irradiance on land with irradiance ~57 km
offshore, Golroodbari et al. [25] finds that in 70% of the locations, the average value for
irradiation at the offshore site is higher than at the land-based site.
For inland water bodies, it will also be of interest to evaluate, and likely improve, the accuracy
of temperature and wind data, as this will be affected by the water body. It is also worth noting
that easier access to data assessing the sea states of water bodies would facilitate planning
and implementation of FPV.
2.2 FPV technology overview
The term FPV encompasses a wide
range of technologies, with a broad
range of different FPV floating system
manufacturers currently in operation.
Figure 4 provides an overview of the
major FPV technolog y manufacturers
and th eir market share measured by
installed capacity . Each manufacturer
naturally aims to differentiate their
products with unique characteristics,
making any categorization scheme
prone to inaccuracies and
oversimplifications. This diversity poses
a challenge when modelling EYA for
FPV. Early reviews and reports often
overlooked this critical information,
leading to confusion about the expected
performance of various FPV
technologies.However, to address the
Figure 4. Market share of FPV technologies by installed capacity.
Data based on [3].

## Página 18

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
18

different types of FPV technologies
efficiently without delving into
specifics, we find it beneficial to use
the categorization shown in Figure 5.
Category 1  is pure-floats, which, as
the name indicates, are solutions fully
composed of floats, typically made of
high-density polyethylene (HDPE).
Category 2 combines metal or fiber -
reinforced plastic (FRP) with floats or
pipes, with Z IM Float being a well -
known European example. Category
3 encompass other types of FPV
technologies such as platforms, ferro-
cement structures , and membrane
technology. The latter is  patented by
the company Ocean Sun.
Technologies submerged in water
and FPV systems that utili ze active
water cooling (water is pumped and
sprayed onto the modules) are not
specifically addressed in this report.
2.2.1 Pure pontoon-based
float technology (pure-floats)
Pure-float FPV technology was the
first to gain commercial traction, and
the three  dominating FPV
technologies world -wide, developed
by Sungrow , Ciel & Terre, and
Northman Energy Technologies  are
all pure-floats. According to SERIES
FPV database, these technology
providers have a market share  of
more than 50%  (27%, 12,7% and
14,9% respectively) [3]. The category
also encompasses many other,
smaller technology providers,
covering a range of different float
designs. The development of the float
technologies over time can also be
substantial, as an example, Figure 6
shows the iterative development of
Ciel & Terre’s Hydrelio® technology.
Naturally, the properties of the floats
will change with the design, but also with choices made with respect to tilt angle and electrical
configuration.
Figure 5. Categorization of FPV system based on float type.
Illustration based on [3], [8], [121].

## Página 19

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
19

Figure 6. Development of Ciel & Terre Hydrelio® technology. The numbers refer to accumulated installed capacity
for Ciel & Terre up until the given year. Copyright: Ciel & Terre International.
2.2.2 Pontoon floats + metal or FRP structures
Another type of structure that is utilized as mounting for FPV is based on a combination of
floats (or pipes) and metal or FRP structures. Here, the floats do not support the individual PV
modules directly, as with the pure-float technology, but instead support the metal or FRP
structure that the PV modules are in turn mounted on to. Examples of this type of FPV
technology include the European ZIM Float by Zimmermann PV-Steel Group and the Korean
Scotra. The ZIM Float technolo gy is currently the most widely deployed FPV technology in
Europe with more than 250 MW installed predominantly in Germany and the Netherlands.
There are currently two versions of the ZIM Float technology, ZIM Float1 and the second-
generation ZIM Float2. The South-Korean company Scotra has developed FPV systems for
more than a decade and installed their first commercial FPV plant (500 kW) in 2012. There
exist many generations of the float with quite substantial developments over the years.  ZIM
Float and Scotra have world -wide market shares (by the end of 2022) of 3. 6% and 3.4%
respectively [3]. An FPV power plant with ZIM Float technology is depicted in Figure 7.

## Página 20

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
20

Figure 7. FPV power plant with ZIM Float technology installed in 2021 with a capacity of 13.7 MW at Lippe
Gabrielsplas in the Netherlands.
2.2.3 Non-pontoon-based floats
One alternative technology involves deploying PV modules on a thin membrane that floats
directly on the water's surface. This solution patented by the company Ocean Sun [26], [27],
uses a ring of HDPE material to provide buoyancy, with the PV panels fastened using keders
welded onto the membrane. PV modules deployed with this technology experience different
environmental impacts compared to pure-floats. Irradiance conditions and wave movement
effects vary, the dominant heat dissipation mechanism is different, and soiling and cleaning
will be influenced by the horizontal mounting solution. Consequently, the models and
parameters used to describe the yield must also be adapted.
2.3 Energy production estimates for FPV
Estimating the energy production of FPV systems introduces additional challenges and
complexities compared to GPV. This section delves into three loss mechanisms that differ
significantly from their GPV counterparts.  For a comprehensive overview of PV yield and
associated losses, refer to the  IEA-PVPS Task 13 Report “Performance Modelling Methods
and Practices” [28].
Section 2.3.1 introduces the most relevant parameters for describing the heat exchange
between an FPV system and its environment. Section 2.3.2 examines the effects of irradiance
non-uniformity caused by wave -induced dynamic tilt variations. Section 2.3.3 explores the
issue of soiling in FPV systems. In each section the loss mechanism is described in general,
before quantitative values for different FPV technologies are discussed. The maturity and
understanding of these topics vary significantly, which is also reflected in the text.
2.3.1 Thermal losses
Temperature impacts both the instantaneous and long -term performance of PV modules. As
cell temperature increases, PV efficiency decreases. Additionally, high temperatures and
© BayWa r.e.

## Página 21

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
21

frequent temperature cycles can accelerate various degradation mechanisms. Therefore,
minimizing operating temperature and thermal cycling can enhance power generation and
potentially extend the lifetime of a PV system [29].
The operating temperature of PV modules mounted in various FPV systems has been widely
discussed. Several studies indicate that FPV systems often operate at lower temperatures
compared to co-located GPV installations [30], [31]. However, other studies report similar or
even higher operating temperatures for FPV compared to GPV [32]. Thus, improved thermal
performance is not an inherent advantage of all FPV installations; it depends critically on
system design and local climate conditions.
The temperature of a PV module in the field depends on numerous factors, including
irradiance, ambient and sky temperature, circulation and humidity of the surrounding medium,
mounting structure, and materials. To (try to) differentiate the impact of all these local climatic
conditions from the impact of the technical installation itself, it is convenient to use so -called
heat loss coefficients, or U -values. Th ese coefficients measure a system's capacity to
exchange heat with the environment. Higher U-values indicate better heat exchange and thus
leading to cooling and, therefore, lower operating temperatures.
Forced convection increases heat transfer between the module and ambient medium
compared to free convection, both because a greater temperature difference is maintained and
because the heat transfer coefficient increase with turbulence . Hence, wind will have a
significant effect on the cooling and therefore an explicit dependence on wind is often
introduced by splitting the U-value into a constant term Uc and a windspeed (WS) dependent
term Uv: U = Uc +  UvWS. In a meteorological context, and hence in most databases that
include wind measurements, wind velocity is provided at 10 m above land, in a free
environment. These will not be representative values for the wind experienced by a PV system,
and it is therefore common to neglect wind effects in EYA of PV. U-values reported as a single
constant is also default in PVsyst. However, reporting a single U -value inhibits the possibility
of finding the explicit dependency of wind. Single U-values are therefore less useful to describe
the thermal properties of a specific design than U -values with an explicit term for the wind
dependency.
Although U -values are convenient, both when modelling energy yield and comparing the
thermal properties of different technologies and PV mounting solutions, they also introduce a
wide range of potential pitfalls. The most serious pitfall, perhaps, is that while U -values are
often perceived to describe a property of the (F)PV system, there is still a significant
dependency on several environmental parameters that are not accounted for in the equations.
In addition, a U -value is not uniquely defined. To understand why one U -value may not be
directly comparable to another, and why the equations describing module temperature as a
function of U -values take different forms, it is illustrative to look at how the most common
models are derived.
The U-value – how it is derived and why it is not uniquely defined
The commonly used models to estimate PV module temperatures are based on a steady-state
thermal balance:
 qsun −  qelec − qrad −  qconv − qcond = 0 (1)

where qsun is the energy flux from the sun, qelec is the energy flux extracted as electrical power,
and the remaining three terms are the heat losses by radiation, convection and conduction (all

## Página 22

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
22

in W/m2). Often, both the radiative and conductive heat loss are assumed to be negligible, and
the convective heat loss is a function of the difference in temperature (T) between the module
(m) and its surroundings (a, ambient), hence
 qsun −  qelec − Uconv(Tm − Ta) = 0 (2)

Rearranging to calculate the module temperature Tm Eq. (2) becomes
 Tm =  Ta + qsun − qelec
Uconv
 (3)

The U-values in the literature referenced in this section are derived with models based on Eq.
(3). Another simplification that is often implemented, is that the electrical output power scales
with the energy flux from the sun. The simplest way to express the scaling would be
 qelec =  qsun η, (4)
where η is the module efficiency. Note that inaccuracies are introduced with this scaling,
because the module efficiency is temperature dependent and because qsun is defined as the
energy flux entering the module, while the module efficiency is normally defined as a fraction
of the incoming irradiance, including light reflected from the surface of the module.
It is convenient to use variables that are commonly measured in the field or that are known
from module data sheets. In PVsyst, qsun is expressed as GPOAα, i.e. the incoming radiation
GPOA, multiplied by the absorption coefficient, α (defined as 1 − r, where r is reflection). qelec
can then be expressed as
 qelec = qsun η =  GPOAαη  (5)
Inserting this expression for qelec and qsun in Eq. (3) we get
 Tm =  Ta + GPOAα(1 −  η)
Uconv
 (6)

This equation, with the choice of using either a single U value or the Uc +  UvWS term, is used
in PVsyst. Note that in the PVsyst manual the cell temperature, Tc, is used in this equation,
while in the Faiman model [33], and in IEC 61853-2 [34], module temperature Tm is used.
An alternative to expressing qelec as a function of  qsun is to express both qsun and qelec as
functions of GPOA
 qsun =  GPOA α
qelec =  GPOA η
(7)
(8)
Inserted in Eq. (3) this gives
 Tm =  Ta + GPOAα −  GPOAη
Uconv
=  Ta + GPOA(α −  η)
Uconv
 (9)

In this version of the equation the use of the module efficiency is in accordance with the
standards for measuring module efficiencies (i.e. reflection is included).
There are also other ways of expressing qsun and qelec which lead to small variations in the
equations used (such as in Liu et al. [35], where qsun is expressed as qsun = ατGPOA, where
τ is the transmittance of the glass and α is the absorption of the PV layer). These nuances in
the equations will generally lead to negligible differences in the resulting temperature or U -
values. However, it must be noted that U-values derived using Faiman or IEC 61853-2 will not

## Página 23

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
23

be directly comparable to U-values derived using Eq. (6) and Eq. (9). In Faiman/IEC 61853-2
nomenclature,
 Tm =  Ta + GPOA
U0
ηO −  ηe
+ U1
ηO − ηe
WS
=  Ta + GPOA
U′0 + U′1WS (10)

the optical losses and electrical efficiency of the module are integrated in the U-values. This is
easily overlooked. None of the U -values cited in Table 1 have the module efficiency term
included in the U-values.
Finally, there are also models that include the radiative term in Eq. (1). This could be of
relevance to improving the accuracy of the temperature models in general, and of particular
relevance if night-time temperature effects are of interest, e.g. for degradation models. Driesse
et al. [36] have suggested how the equations above can be altered to include a radiative term.
Eq. 6, 9, or 10 can be used to derive U -values based on field measurements and module
parameters.
Air-cooled FPV systems
Most FPV systems installed so far can be called Air -cooled FPV systems, meaning designs
where the modules are not in direct contact with water and their only ambient medium is air .
In this configuration the thermal behaviour of the FPV system is influenced by the same
parameters as a GPV system: irradiance, air temperature, wind speed, humidity, and mounting
design. Such FPV systems are predominantly cooled by air. The water temperature does not
have a direct effect on the operating temperature of the module, but can influence the ambient
air temperature, and hence indirectly the operating temperature of the module. The mounting
structure and the local wind conditions are therefore the most critical parameters to determine
the cooling efficiency of air-cooled FPV systems.

Figure 8. Heat loss coefficients (U-values) based on the different PV structures. Source: Liu et al. 2018 [35]

## Página 24

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
24

As illustrated in Figure 8, mounting structures that obstruct the rear surface of the modules (i.e.
they have a “large footprint” on the water surface) will also usually lead to less efficient cooling
by the wind and greater operating temperatures than mounting structures that are more open
(i.e. they have a “ small footprint” on the water surface ). In large footprint configurations, the
operating temperatures of FPV may exceed those of well -ventilated GPV installations [29],
[32], [37] . Liu et al. published one of the first papers quantifying U -values for systems
categorized as free-standing, small-footprint, and large-footprint [37].

Figure 9. The wind direction impacts the best fit U -value. The graph is based on measurements performed on a
Ciel & Terre FPV system in Marlenique, South Africa [38]. Given the same wind velocity, it is evident that the FPV
modules are more efficiently cooled by wind coming from the rear than from the front.
Local wind conditions are affected by topography, vegetation, and infrastructure. Generally,
the wind speed will increase over open areas, such as water bodies. The size of the water
body, vegetation/buildings on the shore, and the placement of the FPV system on the water
body, will influence the wind conditions experienced by the system. The wind direction may
also be of importance for the operating temperature of the PV modules . Figure 9 illustrates
how wind direction impacts the U -value (and hence operating temperature) of a Ciel & Terre
system deployed in Marlenique, South Africa. In this system, the wind cools the modules more
efficiently when coming in from the rear side of the modules (which are all oriented in the same
direction) [38].
Water-cooled FPV systems
FPV designs where the modules can be mounted horizontally, directly in contact with the water
surface, also exists. We will denote these systems as water -cooled. In this configuration, the
modules can benefit from the higher heat transfer coefficient of wa ter compared to air and of
the more limited thermal cycles water basins experience. In this configuration, the water
temperature becomes the dominant parameter affecting the cell temperature. Water -cooled
FPV systems are likely to achieve lower operating t emperatures, compared to air -cooled
installations. The circulation of the ambient water significantly influences the operating
temperature of such FPV systems, with increasing water velocities leading to more efficient
heat transport, equivalent to the effect of wind velocity.

## Página 25

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
25

Pure-floats
An FPV module mounted on a pure-float structure will be cooled by the ambient air and wind,
fundamentally like a module mounted on a GPV system. The most important feature of the
pure-float with respect to thermal losses, is therefore to what extent it exposes the PV module
to wind. Even within the individual categories introduced by SERIS, there will be substantial
differences in the thermal properties of the individual floating structures.
Even though FPV systems consisting of a version of pure-float technology is dominating on
the world market, remarkably, only a few publications with quantitative assessment of U-values
from such systems exist. In the categorization by Liu et al. the pure-float belongs to the large
footprint tag and has a reported U-value of around 30 W/m2K [37], similar to a well-ventilated
rooftop system. The pure-float systems in reference [37] is the Hydrelio® Classic FPV
technology from Ciel & Terre. Another analysis performed on unspecified large footprint
systems in the Netherlands and in Singapore reports median U -values of 37 W/m 2K and 36
W/m2K respectively [29]. The wind-dependent U-values of the same systems are U = 24.4 +
6.5WS and U = 34.8 + 0.8 WS. From a Ciel & Terre pure-float system in Marlenique in South
Africa, U-values of U = 19.3 + 6.2 WS  and U = 20.2 + 3.0 WS are reported [38], depending on
the prevailing wind direction.
Note that the floats in the pure-float category have been continuously developed. The footprint
of the floats has decreased and the accessibility of wind underneath the mounted module has
increased with development of the pontoons, as exemplified in Figure 6. No absolute criterions
for the footprint classification have been published, but it may well be that the most recent
pure-float models no longer fit in the large footprint classification. In much of the scientific
literature available today, only the type/category the FPV system belongs to is provided, while
the specific technology and producer is not detailed. With respect to accessibil ity and
transparency of information it would be beneficial to report the specific FPV technologies
tested, rather than only the type/classification.
Metal or FRP structures + floats/pipes
As with the pure-floats, the metal/FRP structure mounted on floats or pipes will be cooled by
the ambient air and wind. This type of structure will usually allow more air to flow beneath the
PV modules and will often be categorized as a medium footprint structure. In [29] data from
this type of structure is fitted to provide a median (single) U -value of 41 W/m 2K, or, with the
wind term included, U = 18.9 + 8.9 WS. The single U-value is 5 W/m2K greater than the median
U-value of the large footprint system in the same study (see Table 1). However, comparing the
U-values with explicit wind  terms, the wind dependent term is significantly greater for the
Metal/FRP structure, implying that a greater differences in the operating temperature of these
two technologies will be expected at windy sites.
ZIM Float, the FPV technology with the highest installed capacity in Europe, is Category 2, but
there are also several other technologies in this category. There is ongoing work to publish
performance analysis of FPV power plants with ZIM Float technology, but the only work
currently published with a confirmed Category 2 FPV technology is [29] (O. Gandhi, SERIS,
personal communication, August 6, 2024).
Membrane FPV technology
When PV modules are installed on a thin membrane directly floating on the water surface, it
alters the dominating heat dissipation mechanism . While PV modules mounted on pontoons
will be predominantly cooled by air convection, PV modules mounted in thermal contact with a
thin membrane will predominantly release heat through the membrane. The membrane in turn

## Página 26

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
26

is cooled by water convection. The circulation of water underneath the membrane is therefore
important for efficient cooling of the membrane and modules.
For water bodies with significant circulation, a simplified Computational Fluid Dynamics (CFD)
calculation suggests that almost all heat absorbed by the  PV module is conducted down into
the water [39]. Measurements performed at a pilot site in Skaftå, Norway, show that U-values
are in the range of 70 -80 W/m 2K for this technology [31]. The modules in this technology
effectively have air as ambient medium on their front side and water as ambient medium on
their rear side (assuming that the membrane is thin). Hence, the model for heat dissipation
should not use only air as ambient. Currently, only air is available as ambient medium in the
commercial modelling tools. It is recommended to include water temperature data to accurately
calculate module operating temperatures or U -values for FPV technologies where the PV
modules are in contact with water. Figure 10 shows an installation with Ocean Sun technology
at the Magat dam in the Philippines.

Figure 10. Ocean Sun FPV system in Magat in the Philippines. Copyright: Ocean Sun

## Página 27

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
27

Table 1: Summary of U-values reported in literature.
Cooling
mechanism
Configuration Location U
W/m2K
Uc + UvWS
W/m2K
Ref
Air-cooled Free standing GPV array  Default, PVsyst 29 29.0 + 0 WS [40]
Air-cooled Free standing GPV array PVUSA  25.0 + 1.2 WS [40]
Air-cooled Hydrelio Classic, Ciel & Terre Tengeh Reservoir, in
Singapore, near the
sea
~ 30 NA [37]
Air-cooled Tracked, small footprint and
open structure
Inland lake (NL), near
the sea
57 24.4 + 6.5 WS [29]
Air-cooled 17◦-tilted, East-West oriented,
large footprint and closed
structure
Inland lake (NL), near
the sea
37 25.2 + 3.7 WS [29]
Air-cooled 7◦-tilted east, Large footprint and
close structure, SG
Tengeh Reservoir, in
Singapore, near the
sea
36 34.8 + 0.8 WS [29]
Air-cooled 12◦-tilted east, medium footprint
and close structure, SG
Tengeh Reservoir, in
Singapore, near the
sea
41 18.9 + 8.9 WS [29]
Air-cooled 10◦-tilted east, free standing and
open structure, SG
Tengeh Reservoir, in
Singapore, near the
sea
55 35.3 + 8.9 WS [29]
Air-cooled Horizontal module, 3.2-cm off a
floating membrane
Fjord’s Inner branch
on (NO) west coast
46 NA [31]
Air-cooled SolarisFloat
azimuthal tracking FPV system
Lake Oostvoorne (NL) 39.5 24.7 + 3.9 WS [30]
Air-cooled Current Solar
15°-tilted modules mounted on
high-density PE pipes
Small pond,
Kilinochchi, Sri Lanka
33.2 25.7 + 2.8 WS [30]
Air-cooled  15°-tilted modules mounted with
Ciel & Terre FPV system
Small pond,
Marlenique (SA)
NA 20.2 + 3.0 WS [38]
Air-cooled 15°-tilted modules mounted with
Ciel & Terre FPV system
Small pond,
Marlenique (SA)
NA 19.3 + 6.2 WS [38]
Water-cooled Horizontal module on a floating
membrane
Fjord’s Inner branch
on Norwegian west
coast
711 NA [31]

1 As the cooling mechanism infers, this U -value has been calculated using water temperature, and not
air temperature, as ambient medium temperature.

## Página 28

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
28

2.3.2 Wave-induced losses
FPV systems are floating structures that move with wind and waves, causing fluctuations in
the effective tilt angle and orientation of the PV modules. This movement affects the incident
irradiance on the modules and gives rise to wave -induced losses (WIL). The WIL of an FPV
system encompass an irradiance loss (or gain) due to a difference in average tilt of all the
modules compared to a static system with the same tilt, and a mismatch los s due to different
irradiance conditions on the individual modules.
Currently, only a limited number of studies have been published on this topic, and terminology
is still evolving. Dörenkämper et al. introduced the term "wave-induced mismatch loss" (WIML),
defining it as the difference in power output between a system wit h fixed tilt and one with tilt
that varies due to wave motions [41]. In this definition, WIML consists of two components: one
due to different irradiance conditions on the individual modules (mismatch loss), and one due
to a difference in average tilt of all the modules (irradiance loss or gain). Chen et al. [42] use
the terms mismatch induced loss and insolation induced loss to address the two components
separately.
For practical purposes, modelling software like PVsyst may treat WIL as a combined “effective”
mismatch value. However, to fully understand WIL, it is helpful to address the mismatch and
irradiance components separately and use the term "wave -induced losses" (WIL) to
encompass both.
All PV systems are affected by mismatch losses. Mismatch losses within a string of series
connected PV modules are caused either by differences in the experienced conditions or in
the rated power of the individual modules. The output of the string will be limited by the module
with the lowest current. A wave-induced mismatch loss will come in addition to the mismatch
loss induced by differences in rated power (or degradation).
The WIL depends significantly on a large set of parameters, including both environmental
parameters and the FPV structure itself. Currently, measured values for WIL are not
accessible. Model ling of WIL requires three basic mode lling steps: 1) model ling of the
interaction between the FPV structure and waves, 2) modelling of the irradiance on the array,
and 3) modelling the electrical response to the irradiance. Results from modelling approaches
are scarce and only validated to a limited extent, and complete validation requires high
resolution measurements of (at least) sea state/waves, module/float movement, design plane-
of-array (POA), and irradiance at module -level. There are, however, mode lling efforts
published that provide insight to the sensitivity of WIL to different parameters.
In DNVs recommended practice [13] the current recommendation is to use one of three
methods to estimate WIL: wave tank measurements, numerical analysis or engineering
judgement. It may not be feasible to model WIL in detail for each new FPV project, but with
increasing number of publicati ons and experience, the engineering judgements will become
more precise. Providing generic values for WIL is not possible due to the significant technology
dependence. However, a table with WIL values for the most established FPV technologies for
different sea states would be useful, but this information is not currently available.
Impact of FPV technology on WIL
Different aspects of FPV technology will be decisive for various loss mechanisms.
• Number of modules per float. Intuitively, the number of modules per float impacts WIL
significantly. When all modules that are connected to the same maximum power point
tracker (MPPT) are situated on the same rigid float, they all have the same orientation

## Página 29

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
29

and do not experience wave-induced mismatch losses. Note that the system can still
experience changes in the effective tilt, and hence irradiance and production, due to
waves. Systems with one or a few modules per float experience different orientations
due to wave motion, leading to increased mismatch losses (if connected to the same
MPPT).
• The extent to which floats follow wave movement also affects WIL. Designs like
membrane-based systems, which move freely with waves, are expected to experience
higher mismatch losses. Pure-float systems are somewhat more resistant to wave
influence (depending on how they are connected), while semi-closed structures or
systems using rigid materials (metal or FRP with floats/pipes) show lower mismatch due
to a more rigid structure.
• The electrical configuration and the length of the PV string has also been shown to affect
the mismatch loss. For commercial size FPV systems with more than 20 PV modules in
a string, the mismatch loss will saturate [41], [43]. It can be understood by looking at the
probability of (at least) one module positioned in the “worst” possible angle towards the
sun.
Impact of environmental parameters on WIL
The severity of WIL also depends heavily on environmental parameters such as the sea state
and the irradiance angle of incidence [13], [41]. There is currently no published literature with
measured values for WIL. A few papers publish modeled values of WIL [41], [42], [43]  that
explore the effects of the sea state (wave period, wave height, wave direction), latitude and
time of year on the resulting WIL.
The impact of the sea state and latitude is summarized below.
• Sea state. The combination of wave height and wave period is important for the
magnitude of the WIL [41], [42], [43]. Steep waves will induce larger differences in tilt
between the modules and hence larger mismatch losses. The shorter the wave period
for a specific wave height, the higher the power loss of the system influenced by waves
compared with the static system. In addition, increasing wave height will also lead to
greater WIL. An important conclusion from this is that the effect of WIL on FPV systems
deployed at lakes, dams and reservoirs with calm water is small or moderate even for
the most affected, one-module-per-float or membrane systems.
• Latitude and seasonal dependence. Reflection increases nonlinearly with angle of
incidence. Therefore, larger angles of incidence infer both a greater irradiance loss and
greater differences between the irradiance absorbed by modules (at a given absolute
difference in tilt). FPV designs with non-optimal tilt for a given latitude will therefore
experience higher WIL (everything else being equal). For the typical, relatively horizontal
FPV system, this implies that WIL is greater at higher latitudes, and that it has a
seasonal dependence, with the highest relative yield losses when the tilt angle is least
optimal (i.e. winter for Europe) [41], [43].
The simplest approach to model the sensitivity of different parameters (environmental and
technology specific) on WIL is to assume that the floats are “slave-to-the-waves”, i.e. that the
floats do not dampen the waves, and that each individual float is not  constrained in its
movements. In Figure 11 and Figure 12, this approach has been taken to model the sensitivity
of a one-module-per-float technology, based on Nysted et al. [43].

## Página 30

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
30

Figure 11. Modelling of the sensitivity of WIL for a) significant wave height, b) peak period and c) string length for a
one-module-per-float type technology, based on [43].
Figure 12. Modelling of WIL for different times of year for two latitudes, 0°N and 50° N for a system with a design
tilt of a) 0° and b) 15°, based on the modelling method in [43].

Pure-floats
With respect to WIL, the most important adaptation to account for different FPV technologies
will be in the wave-float interaction. The mismatch model published by Dörenkämper et al. [41]
represents a floating structure that resembles the pure-floats. The tilt angle is 12°, and the float
is according to the paper “in-line with commercial products of single floats on the market today”.
Two different movement models were used, the first assumes that the PV modules perfectly
follow the waves and tha t the floats do not dampen the waves. These are the same basic
assumptions as in the paper by Nysted et al. [43]. The other movement model is a mechanical
simulation of movements of interconnected floats on the water surface. The model accounts
for gravity, buoyancy, wave forces, interconnection forces and inertia. A comparison of both
models confirms the expectatio n that with the mechanical simulation, the movements are
dampened compared to the wave-following model, and therefore the calculated wave-induced
losses are lower.
Metal or FRP structures + floats/pipes
There is currently no published literature reporting on modeled or measured WIL for a
metal/FRP type of structure. For this type of structure, the PV modules mounted on the same
rigid float will have the same orientation, reducing or eliminating mismatch losses between the

## Página 31

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
31

modules on the same float. The changes in irradiance compared to a fixed-tilt system will also
likely be reduced (which may be a loss or a gain). In sum, it is expected that FPV systems with
rigid materials (metal or FRP with floats/pipes) will be less affected by WIL than pure-floats
given the same sea state.

Membrane FPV technology
As previously mentioned, in the membrane FPV technology the PV modules are expected to
follow the local wave motion, with only limited damping. Therefore, although the impact of the
membrane size and the fasting mechanism of the modules are not known, it c an be argued
that the slave -to-the-waves approach is a good starting point to model WIL for this FPV
Category. Nysted et al. [43] use linear irregular waves and a response model where the PV
modules are assumed to follow the local wave motions exactly and not dampen the energy of
the incoming waves. Using these assumptions, in addition to the more general modelling steps
for mismatch described in section 2.3.2, the dependency of WIL on a combination of significant
wave height and peak period is shown in Figure 11.
In this section, Figure 11 is used to illustrate general trends for the sensitivity of WIL to different
parameters. The values can also be interpreted as a worst -case scenario for WIL for
membrane FPV technology, and one-module-per-float technologies.
2.3.3 Soiling losses
Although FPV has the potential to provide numerous advantages, it can also lead to new
challenges, such as potentially more severe soiling losses. These losses are produced by
particles or objects that accumulate on top of the solar panel, which block the irradiance
reaching the solar cells, and thus reducing their power output. Furthermore, if the soiling is
concentrated in a particular area of the solar panel, e.g. soiling due to bird droppings, this can
produce hotspots, as seen in Figure 13, which can accelerate the panel degradation and result
in higher O&M costs. Pre -construction bird surveys may help to identify such possible issue
during the project development phase.
To reduce the soiling losses, studies have shown that a higher panel tilt is advantageous [44].
FPV systems, however, are typically kept with a tilt below 20°, regardless of the geographical
location. This typically low tilt is a trade -off between optimizing POA irradiance and keeping
capital expenditure (CAPEX) low and power density high. CAPEX will increase with increasing
tilt due to increased requirements for the float, mooring and anchoring system, while the power
density will reduce due to interrow shading. In addition, numerous FPV systems are installed
at locations surrounded by diverse fauna and as a result, bird droppings can become a
challenge due to local (nesting) and migratory birds. Potential solutions to tackle this challenge
are bird deterrents such as shiny reflective surfaces, ultrasound devices, lasers and scare
techniques like water sprayers, scarecrows and fake falcons. However, the use of bird
deterrents should be evaluated with respect to sustainability, and the use of such systems may
be regulated.
On the other hand, as these systems are not installed on land, they are expected to experience
lower soiling from dust in comparison to GPV systems. Moreover, the water required to clean
them is directly available (although it needs to be assured that clea n fresh water is used). In
addition, there may be more water reaching the solar panel’s surface, e.g. via waves and wind
influence, thus potentially reducing soiling losses.
If the soiling effect is considerable for a particular project, manual or automatic cleaning using
robots might have to be done periodically. Nevertheless, as these systems are surrounded by

## Página 32

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
32

water, cleaning can be challenging and thus, the FPV system needs to be properly designed
to allow for these O&M tasks to take place in an adequate way.
Too little open information is currently available to establish a span of expected soiling rates
for various FPV technologies in different climates. Expected FPV soiling losses of 1-3% has
been reported by [7], while it is also noted that this depend on the site and cleaning schedule.
Scientific reports on soiling rates for FPV systems would be of importance to improve accuracy
of EYAs.

Figure 13: Higher local temperature due to hotspot induced by bird dropping.
2.4 Modelling yield for FPV systems
There is a range of tools capable of modelling, with different degrees of accuracy, the energy
yield for GPV. The list includes, but is not limited to, PVsyst, SAM, PV*Sol, Homer, PVGIS,
PVWatts, PVCase, and pvlib. To our knowledge, none of these modelling tools have
implemented features to deal specifically with the loss factors of FPV. One could also imagine
that other FPV related features such as modelling of evaporation or irradiance reaching the
water surface could be included in the same modelling tool. This, however, is not within the
scope of this report to discuss. In the following section, we will focus on the modelling
capabilities and shortcomings of two important modelling tools, pvlib and PVsyst, with respect
to FPV losses and yield. pvlib and PVsyst are chosen because they are widely used for
research and development of PV projects.
Modelling the performance of any PV system follows certain predefined steps regardless of
what software is used. These steps include calculation of: POA irradiance, effective irradiance,
module (and cell) temperature, array IV curve (or P mp), and inverter efficiency . For an FPV
system, some of these steps need to be adjusted to account for system and site -specific
conditions. For example, FPV arrays are not fixed and can move as waves pass through the
array, therefore, calculation of POA irradiance needs to account for a moving array and may
require wave conditions as input. Another example is module and cell temperature modelling.
As discussed in Section 2.3.1, FPV systems are affected by irradiance, air temperature and
wind speed, as are terrestrial systems. However, the effects of water temperature, relative
humidity and direct splashing of water onto the modules may also need to be
considered.Furthermore, FPV systems where the modules are mounted on a membrane that
floats directly on the water will have a much different thermal signature than modules
suspended over the water surface.

## Página 33

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
33

2.4.1 FPV modelling in PVsyst
The solar industry’s most widely used software simulation tool for assessment of a PV system’s
bankability is PVsyst. This is in part due to the actual modelling capabilities, interface and
databases of PVsyst, and in part due to the relatively long trustworthy history of the software.
Temperature modelling in PVsyst
Numerous models have been proposed for simulation of the module temperature. In PVsyst,
module temperature is estimated using the Faiman model (Eq. (11)) [33].
 Tc = Ta + GPOA ∙ α ∙ (1 − η)
Uc + Uv ∙ ws   (11)
where Ta is the ambient temperature, GPOA is the plane-of-array irradiance, α is the absorption
coefficient, η is the electrical efficiency of the module and WS is the wind speed. Uc and Uv are
the constant and convective heat transfer components, with unit W/ (m2K) and W/(m2Km/s),
respectively. Often, a simplified version of the equation with a lumped heat loss factor, U, is
used: U =  Uc + Uvws. Note that IEC 61853 -2 [34] also recommends the Faiman model for
yield assessment.
PVsyst recommends U -values of Uc  = 29 W/(m2K), Uv = 0 W/(m2Km/s) for free standing
(open-rack) systems. For modules with a fully insulated back side, PVsyst recommends a value
of Uc  = 15 W/(m2K), Uv  = 0 W/(m2Km/s) with the argument that only the front side contributes
to the convective heat exchange. The default value proposed by PVsyst for new projects lies
between these two, Uc  = 20 W/(m2K), Uv  = 0 W/(m2Km/s), which is considered representative
for typical rooftop systems. For utility scale PV plants, single U-values are also commonly used
as input, and wind data is not taken into account.
Fundamentally, the Faiman equation will be adequate to model temperatures of FPV systems
when the main heat exchange mechanism is convective heat transfer to the ambient air, as it
is for GPV. For membrane floats (Category 3 in Figure 5) given that they are in thermal contact
with the membrane (negligible air gaps), and other FPV technologies where the PV panels are
in contact with water, the modelling of heat transfer should consider that the ambient on the
rear side of the module effectively is water. This results in a new expression for the heat
balance, and hence an altered equation to calculate cell temperature [31], [39]. PVsyst does
not provide the possibility to change the model for the cell temperature calculations, and hence
cannot accurately model the temperature of this type of FPV technology. If PVsyst, or similar,
is used for EYA of this type of FPV, it is shown t hat using water temperature as the ambient
temperature will improve the module temperature model [31].
Mismatch modelling in PVsyst
In PVsyst, mismatch is treated as a constant loss factor, valid for the whole simulation. Hence,
it is not a detailed model of the mismatch under the simulated conditions, simply an estimate
of the total effect of non -identical module and string parameters . The value will usually be
dominated by the dispersion of the module efficiencies (power class for new modules, power
class + degradation for older modules). According to PVsyst, the mismatch value for GPV
systems is usually set to 2%. The origin of the mismatch for FPV is discussed in Section 2.3.2.
As there is no actual modelling of mismatch performed in PVsyst, such modelling must be
performed outside of PVsyst, and the aggregated result must subsequently be input to the
PVsyst model.

## Página 34

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
34

2.4.2 FPV modelling in pvlib
pvlib python is a community-developed open source toolbox for simulating the performance of
PV systems [45]. The python library contains more than 100 PV performance modelling
functions, which aligns with the core mission of providing open, reliable, and reference
implementations of PV system models. The functions cover all the modelling steps for
estimating energy yield. The current version of pvlib (v0.11. 2) does not feature major FPV-
specific capabilities, however, due to pvlib’s flexible design, it is possible to account for many
of the modelling aspects specific to FPV.
Temperature modelling in pvlib
pvlib python supports several PV temperature models developed for GPV, including Fuentes,
SAPM, NOCT SAM, Faiman, PVsyst, Ross, and a generic linear heat loss factor model. As
reported in Section 2.3.1, most FPV systems are predominantly air -cooled with a thermal
behaviour similar to GPV systems. For such systems, the existing models in pvlib are
straightforward to use for modelling PV module and cell temperature. Similar to PVsyst, it is
possible to use water temperature instead of air temperature as the heat sink temperature
used by the aforementioned temperature models. In any case, appropriate heat loss
coefficients should be used, as discussed in Section 2.3.1. The pvlib documentation contains
an example of how to calculate FPV module temperature.
Mismatch modelling in pvlib
Although constant loss factors are easily applied in pvlib as well, pvlib also offers functionality
needed for modelling electrical mismatch in full fidelity. This is made possible by two main
capabilities: no limitation on the maximum number of module orientations, and no fixed or
minimum simulation time interval. This is particularly beneficial for FPV systems, as variati on
in module orientation caused by waves occurs on a short time scale on the order of seconds
[43]. Given module orientation values from an external wave model, pvlib can simulate the
incident irradiance and temperature of each module individually. These module -specific
operating conditions can then be passed into pvlib's electrical functions (e.g. the C EC and
PVsyst single-diode models) to simulate I-V curves for each module.
The user can then process these I-V curves using general-purpose numerical python packages
to combine the module-level I-V curves into string- and array-level curves, allowing calculation
of the wave -induced electrical mismatch loss. Alternatively, streaml ined simulation of array -
level I-V curves is possible using SunPower's Python package PVMismatch [46]. The string-
or array-level curves can then be passed into any of pvlib’s existing inverter models.  Note that
some of pvlib’s inverter models are capable of accounting for multiple maximum power point
tracking (MPPT) inputs, a required consideration when simulating multi -MPPT inverters
connected to mismatched strings.
Possibilities and shortcomings
As with existing commercial PV simulation software, pvlib lacks dedicated capabilities for
modelling FPV systems. To achieve more accurate yield simulations, FPV -specific
temperature models should be added, particularly temperature models which are capable of
accounting for heat transfer to both air and water. Auxiliary functions for determining the inputs
to these FPV models, such as module orientation variation due to wave action and wind speed
adjustments, may also be added. Information on water albedo was added in the latest release
of the software.

## Página 35

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
35

In terms of mismatch modelling, it should be noted that PVMismatch is not actively
developed/maintained.  Additionally, its simulation functionality relies on a particular electrical
model for which PV module parameters are not readily available. For these reasons, it is
desirable that pvlib’s own electrical simulation capabilities be extended to facilitate the process
of combining mismatched I-V curves.
2.5 Uncertainty analysis
Uncertainty in annual EYA arises from two main categories of uncertainty: random (aleatory)
uncertainty and lack of knowledge (epistemic) uncertainty. On the one hand,  random
uncertainty is inherent in annual energy estimates, with the inter-annual variability of the solar
resource being one of the largest sources of uncertainty in annual energy modelling [47]. The
latter is for example quantified in [47] as the coefficient of variation  of the annual GHI, and
given a range of 2% to 6%. On the other hand, e pistemic uncertainty includes uncertainty in
all data measurements, modelling parameters, and models that are imperfect representations
of the physical system. In theory, this uncertainty, could be reduced through improved data
measurement and accurate performance models [48].
Literature mainly considers uncertainty propagation in models of generic PV systems [48], [49],
[50], [51]. This usually entails identifying the main loss factors in the PV model chain, together
with their underlying uncertainty - either through measurement or educated guesses. The first
steps are often to distinguish the involved type(s) of uncertainty, the a ffected model input
(parameter or variable) and settle on an uncertainty measure, such as standard deviation. With
that at hand, mainly three approaches are commonly pursued, and combined if needed:
i) Independent input variables . For simple models, such as linear combinations of input
variables or products of independent input variables, uncertainty propagation from input to
output can be done analytically by calculating variances. Even though there are
interdependencies in the PV modelling process, standard literature [48], [50] often represent
the annual PV yield as a product of independent loss factors to be able to utilize this relatively
simple, analytical model to calculate the output averages and variances [48]. However, it shifts
the challenge towards interpreting and determining the uncertainties of the loss factors.
ii) Small and uncorrelated input uncertainties. The so-called Gaussian law of error propagation
relates the variances of a model’s input and output when the model can be represented by an
analytical equation. It simplifies uncertainty propagation by assuming small and uncorrelated
input uncertainties 2. Additionally, this approach provides a more accurate calculation of
average output values for nonlinear models, where the average output generally differs from
the result obtained by merely averaging the inputs.
iii) Correlated input variables. One can use Monte-Carlo simulations that stochastically sample
input uncertainty to calculate uncertainty in important output variables such as the annual yield.
The advantage of this strategy is that it can trace uncertainty propagation along the full PV
simulation chain, and in doing so can also account for correlated input variables. This,
however, comes at a cost, most notably the need for a lot of sampling of input statistics to
obtain reliable output statistics. Also, it is difficult to draw analytic conclusions from computed
output statistics.
To address the uncertainty with respect to the selection of competing component models in
the PV chain (accounting for the variability in predictions of, e.g., the Faiman and Sandia

2 However, input covariances can easily be incorporated. Note also that, despite the name, Gaussianity
of input probability distributions is no prerequisite.

## Página 36

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
36

module temperature model), an ensemble of model chains can be utilized, with each ensemble
member being a sequence of different component models. This so called  “poor man’s
ensemble” approach can also mimic epistemic uncertainties by assigning respective standard
values to the parameters of each considered component model.
To date, no published efforts are known for quantifying uncertainties in crucial FPV modelling
steps such as soiling, fluctuating POA irradiance or mismatch losses. For best results,
modelers are advised to combine educated guesses with a critical reading of existing literature
on uncertainty propagation.

## Página 37

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
37

 RELIABILITY OF FLOATING PV
The economic viability of PV power plants is fundamentally linked to their lifetime energy yield.
Factors such as degradation effects and the overall lifespan of the power plant directly impact
electricity production and the levelized cost of energy (LCOE) , consequently influencing
profitability [45, p. 11]. In Section 3.1, we begin by defining degradation and exploring methods
to quantify it.
Conducting an effective reliability analysis is essential for minimizing failures and ensuring a
stable power supply [52]. However, while evaluating the reliability of an FPV system, several
significant knowledge gaps and challenges arise, which will be addressed in this chapter.
Firstly, climatic and environmental factors play a major role in degradation and are by nature
location specific. The stress profiles experienced by components in an FPV installation are
neither well understood nor quantified and will vary a lot depending on float technology and
water body conditions. An overview of what is currently known regarding climatic stressors for
FPV is provided in Section 3.2. The second knowledge gap relates to the scarcity of information
on and systematic studies of observed field failures as well as of degradation/performance loss
rates and is addressed in Section 3.3.1. And third, as a result of the first two points, there is no
accelerated stress testing protocol developed for component reliability evaluation, complicating
the process of gaining relevant insight from indoor testing.  Existing knowledge and current
efforts are summarized in Section 3.3.2. A final source of insight into FPV degradation effects
is simulations, which will be discussed in Section  3.3.4. The correlations between the main
topics of the Chapter are illustrated in Figure 14.

Figure 14. Figure adapted and reprinted under under a CC BY 4.0 license from [53].

## Página 38

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
38

3.1 Defining degradation
3.1.1 Definitions
The term degradation denotes the gradual process of change in characteristics with
operational time of a material, component, and/or system triggered by stress impact. Typically
for PV, this aging process causes a decrease in performance, and hence a power loss [54, p.
15]. Degradation is caused by stressors, such as physical, chemical, or mechanical stress
acting on a material, component or system. Examples include temperature, irradiation
[ultraviolet (UV), visible (VIS), near infrared (NIR)], water/moisture, electrical potential as well
as mechanical stresses such as compressive or tensile impact. The sum of the local stressors
that a PV module experiences during operation is specific to its design and exact location and
surrounding, e.g., stress induced from mounting or variations in temperature and shading. The
microclimate can be inhomogeneous even within a PV module (different humidity or cell
temperature) [54, pp. 16, 17].
Typically, three different kinds of degradation are distinguished: reversible degradation,
irreversible degradation, and failures.
Reversible degradation is either related to accumulated soiling, including the growth of algae
and loot, which will not be removed by natural rainfall, but may be removed with dedicated
cleaning actions. Other effects of reversible degradation include elec tric phenomena like
polarization (potential induced degradation, PID) or light and elevated temperature induced
degradation (LeTiD), from which PV modules may (partly) recover naturally, e.g. during
nighttime, or driven by specific electrical devices during nighttime.
Irreversible degradation is mostly related to material ageing both within the solar cell and with
the embedding materials. Solar cells may degrade by a variety of diffusion and corrosion
processes, which again may be related to changing properties of the e mbedding materials.
Moisture ingress through the back sheet or the edge seal may increase with time, and
embedding polymers may change their transparency with time. Mechanical stress may lead to
an increasing number of micro-cracks in solar cells which can lead to a reduced power output.
Based on IEC 60050-191 [55], the definition of failure is the termination of the ability of an item
to perform a required function . For a PV module, this means that the module needs to be
replaced. While that  is relatively clear from a safety perspective, it is less so from a
performance perspective. However, a performance of 80% of the initial value is often used as
a threshold for failure. Failures are commonly subdivided into early life (1-2 years) failures,
often related to poor design or manufacturing errors, failures during the steady-state life, often
either random or the result of technology limitations, and wear-out failures, caused by
mechanisms that degrade the performance gradually until the device does not function
anymore. Ideally, wear-out failure only occurs after the warranty period expires [56].
Regarding FPV, the balance of system (BOS) components may be even more critical than the
PV modules. Junction boxes, cables, connectors, and related protecting materials may suffer
from additional stress compared to GPV systems , while additionally, there are FPV -specific
BOS components like anchors and floats whose reliability also needs to be considered.
3.1.2 Quantification of degradation
PV module and system degradation may be detected in several ways. Some of them are
preventive and should be part of standard O&M procedures ( see Chapter 4), others are
retrospective and related to the fulfilment of contractual obligations. Standard evaluations rely

## Página 39

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
39

on yield data and meteorological data only. More advanced assessments look for specific data
signatures and are combined with onsite visual and infrared inspections and sometimes even
with lab testing of selected components.
As a typical degradation measure, the performance loss rate (PLR) is often used. It is stated
in percentage per year and quantifies the temporal decline of a PV system’s power output in
relation to its irradiation input. Accurate long -term PLR information is vital for predicting
electricity output, improving system reliability and anticipating maintenance requirements. On
the economic side, PLR has been shown to be one of the most influential factors of LCOE.
Beyond the irreversible physical degradation of PV modules, the PLR also captures
performance-reducing events, which may be reversible or even preventable through good
operations and maintenance (O&M) practices [57], [58], [59], [60].
3.1.3 Distinction of degradation effects
As mentioned above, observed degradation effects may be divided into component failures,
reversible degradation, and irreversible degradation. To evaluate irreversible degradation in a
correct manner, most or all reversible effects must be known (and ideally repaired or removed).
In the process, also shading losses must be accounted for, which may increase with time when
caused by vegetation, decreasing the overall system yield.
As degradation assessments typically deal with long -term observations, i.e. large sets of
operational data, methods of automated failure detection may play an important role. These
algorithms, often run concurrently, are generally grounded in expert knowle dge, assisted by
statistical and machine learning methods, validated with field data, and designed to be flexible
and adaptable to the characteristics of PV systems and O&M service providers. They can
include communication faults, inverter outage and inverter late wake up, check on open-circuit
conditions, several relative comparisons between individual strings and inverters, and all kinds
of sudden changes in performance indicators [61].
Beside the distinction of “real” degradation from failures or reversible effects, further (algorithm-
driven) differentiation between degradation mechanisms is desirable. This, however, needs
further research, as “real” degradation is often related with very small changes of performance
with time, and as new cell and module technologies may even show - previously unknown
degradation modes.
3.2 Driving degradation – describing FPV specific stressors
A PV system will experience a combined effect of multiple stressors over its lifetime in the
outdoor environment. Knowledge about the se stressors is a precondition for the creation of
meaningful predictions of degradation and service life . The stressors include temperature,
humidity, UV radiation, wave and wind loads, tidal variations, temperature fluctuations [62],
[63], high voltages, corrosive compounds, soiling, abrasive loads, shading, and flora & fauna.
The stressors are design- and water body-dependent and, when co-occurring, can attenuate
or have amplified effects.
When comparing FPV to conventional GPV, one might intuitively expect some of these
stressors (e.g., humidity and mechanical loads) to have more significant differences in stress
profiles than others (e.g., UV radiation). For example, the design and placement of a mooring
system for FPV platforms must account for water-level variations, soil conditions, bathymetry,
and location. In deep water, the construction of a mooring system can consequently present
significant challenges and incur substantial costs [64], [65]. For components common to both

## Página 40

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
40

GPV and FPV systems, there is however little openly available quantitative information on FPV
specific stress profiles. If available, such stress profiles could be compared with available
stress profiles from GPV environments, to assess to which extent, e. g., qualification testing
and module design considerations originating from the conventional GPV industry are
applicable or in need of modification.
Biofouling and soiling
Biofouling is an often discussed problem for FPV installations [66] and can act as a stressor
by affecting corrosion processes or inducing weight and stability issues for the floating
structure. Biofouling removal will lead to increased O&M costs but can also in itself act as a
stressor by increasing wear on various components.
Soiling can block incoming light and thus decrease the performance of PV modules [67]. FPV
installations have been seen to attract birdlife [37], and bird droppings impact the short -term
performance of FPV systems more than for GPV [68] and lead to hotspots.
Bird droppings is an example of FPV stress profiles having a major dependence on both float
technology (e.g., plastic pontoon versus membrane versus metal platforms, see Figure 5) and
water body (e.g., of different Sea State Codes as discussed in the Introduction). Different float
technologies will also yield significant differences in, e.g., wave -induced mechanical loads or
the exposure to water for various components. While stress profiles on calm inland water
bodies will likely not be too different from a conventional GPV system, the differences are
expected to increase when going to larger water  bodies and eventually to near -shore or
offshore conditions. In case of high winds and wave forces, the floating structure may
experience drifting or deformation, and materials may leach into the water because of damage
[69]. Waves can also affect the electrical components of FPV systems, leading to
disconnections or damage, which impacts the system’s electrical integrity and performance.
Humidity
A few reports have compared humidity measurements from meteorological stations at FPV
systems on inland and nearshore water bodies and found modest differences in average
relative humidity; on the order of 0 -10 percentage points higher relative humidity for  average
daily values [37], [70], [71] . However, these results are hard to generalize. Further, relative
humidity values aggregated to a daily timescale carry limited relevant information in this
context, as the coupling of humidity and temperature is of central importance for moisture
ingress and related degradation phenomena. In addition to the sources of mechanical loads
present for GPV, FPV has waves as an additional factor, including potential wave -slamming
and -breaking. An FPV system typically involves more complex and dynamic structures than a
GPV system to provide mechanical support for electrical components, making it essential to
assess factors such as fatigue. Some reports exist in the literature examining FPV specific
mechanical loads, so far mostly focused on the mechanical integri ty of the float system [72],
and less on the PV module and other electrical components. Lower module operating
temperatures for FPV have been widely discussed in the context of increased module
efficiency (Section 2.3.1), but also has the potential to significantly influence reliability. Most
degradation processes are thermally activated; thus, a lower operating temperature will
dampen the effect of other stressors such as UV and humidity. How significant such an effect
might be has so far not been properly studied.
Salt
When deployed in nearshore or offshore waters, the presence of salt will present a significant
reliability concern. The level of salt exposure will far exceed levels in most GPV systems, again

## Página 41

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
41

depending strongly on float design and water body characteristics. This will  potentially drive
corrosion on various components and pose risks to supporting devices [73]. It can also pose
significant stress and enhance problems with PID [74] (see Figure 13).
3.3 Understanding and quantifying degradation  – sources of
information
Ensuring FPV reliability alongside the rapid growth of cumulative installed capacity and fast
technology development and diversification is a major challenge. However, it is a challenge
that needs to be resolved to take down real and perceived reliability risks and ensure the
bankability of FPV technology. To meet the challenge, it will be of central importance that field
failure observations and quantified stress profiles be collected to develop accelerated stress
test regimes.
3.3.1 Field data on degradation and failure s – overview of observed and
potential failures
Learning from observed field degradation and failure s has been an indispensable part of
reliability development for conventional GPV [75]. For FPV, projects are still relatively young,
and public literature on degradation and failure modes specific for an FPV environment is very
limited. This holds true both for the structural (floats, connectors, anchors, mooring) and
electrical (PV modules, cables, inverters etc.) parts of the system.
Collection of long-term field data is indispensable for accurate identification of failure modes
and the design of appropriate testing protocols.
Table 2: Overview of potential failures of FPV systems. compiles a non-comprehensive list of
potential failures of the FPV system and single mechanical and/or electronic components that
might be caused by (a) the altered stress profiles experienced in FPV compared to GPV and
(b) the fact that FPV introduces new components compared to GPV (e.g., anchoring, hinging
between floats) resulting in new reliability challenges. Examples of early reliability concerns or
failures that have been observed in pilot and/or commercial FPV projects are shown in Figure
15.

## Página 42

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
42

Table 2: Overview of potential failures of FPV systems.
Environmental
stressors specific,
more pronounced, or
with more severe
impact for FPV
System or component Potential events and failures
Mechanical
movements due to
wave and wind
actions, ice, water
currents and/or
water level variations
Mooring, anchoring, float and
mechanical support system
Failures in the mechanical integrity of the
system and/or the mooring of the system
Mechanical interconnectors
between subsystems
Accelerated materials fatigue, breakage
of connectors
Plastic parts in the system Rubbing damage
PV modules Glass cracking or deformation by wave
slamming
PV cell cracking
Interconnect breakage
Frame deformation or breakage
BOS components (inverters,
cables, connectors)
Internal electrical disconnect (“electrical
open”) induced by continuous
movements
Accelerated wear of cable mantles
induced by continuous
movements leading to shunts, arcs
Humid and corrosive
environment
Steel and aluminium parts in
mechanical connectors and
mounting systems
Accelerated corrosion
PV modules (1) Corrosion of cell metal contacts, (2)
delamination, (3) accelerated PID, (4)
frame and glass corrosion, (5) Junction
box failure
BOS components (inverters,
cables, connectors)
Degradation of insulation material, cable
and connector corrosion leading to
increased leakage currents, inverter
shutdown
Specific forms of
pollution and fouling
(bird droppings,
biofouling, salt and
limescale
deposition)
Floats, submerged
components
Can add extra weight and drag,
potentially altering the buoyancy and
balance of the system
PV modules  Hotspot-induced failures (diode failures,
local melting, microcracks)
Increased soiling losses due to organic or
inorganic fouling
Exposure to UV
radiation
Plastic parts (floats, float
connectors, cables)
Embrittlement and cracking, reducing the
structural integrity of the plastic parts

## Página 43

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
43

a) Rubbing damage on an HDPE part

b) Rubbing and stress damage on an HDPE part

c) Torsion damage on an aluminium part

d) Loss of mechanical integrity due to wave forces

e) Damage on PV modules due to wave slamming

f) Biofouling of underwater component [76]

g) Corroded junction box

h) Partly delaminated edge seal [77]
Figure 15. Examples of early failures or reliability concerns observed in pilot and commercial FPV systems. For
15a, b, c, d, e, and g, the source of the images is TNO.

## Página 44

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
44

3.3.2 Degradation measured through performance loss rates
Data on the accumulated long -term effects of various degradation mechanisms on
performance stability is quantified through the PLR, as illustrated in Figure 16

Figure 16. Figure adapted and reprinted under under a CC BY 4.0 license from [53].
Three commonly used statistical methods are deployed to calculate the PLR through historical
PV performance and climatic data: Ordinary Least Squares (OLS), seasonal and trend
decomposition using locally weighted scatterplot smoothing (STL), as well as Yea r-on-Year
(YoY).
Least squares linear regression (LSLR) is the most popular type of linear regression, and it is
based on the minimization of the squared error of residuals. The idea behind Seasonal and
Trend Decomposition Procedure Based on Locally Weighted Regression (Lo ess), commonly
referred to as STL, is to decompose the PR or predicted power time -series into a seasonal
part, a remainder and a trend using locally weighted, non-parametric regression. The YoY is a
method for PLR assessment which, instead of calculating one value for the loss rate, provides
a distribution of rates of which the median represents the overall long -term PLR [78]. The
distribution is obtained by calculating the loss in performance between all pairs of datapoints
that are exactly one year apart.
Based on the current practices, the statistical PLR calculation pipeline can be divided into the
following steps: (a) initial data quality assessment, (b) data filtering, (c) performance metric
calculation and data aggregation, (d) possible performance tim e-series feature corrections,
and (e) the calculation of the actual PLR using a statistical model. Although the general pipeline
from step (a) to (e) is well established [79], the PLR estimation is nontrivial because the
selection of each individual step as well as the interplay between these steps determines the
final value. Numerous studies [78], [79], [80], [81], [82] have been conducted to find the optimal
pathway for calculating PLR, especially focusing on (b), (c) and (e).
The various methods to quantify PLR differ in their accuracy but are all based on similar
principles; to determine the trends in the historical data. The major drawback of these statistical
methods is that they do not trace the correlation of the evaluated  degradation rates with the
climatic variables and degradation processes. To capture these correlations, physical models
can be utilized, and different physical models have been proposed for different degradation
mechanisms [54, p. 14].
Despite the significant number of FPV systems that have now been operating for several years,
long-term FPV performance studies are rare . Some of the comparative PLR calculation
studies, such as [58], [60], [79], [83], [84], compare methods by using data from different FPV
sites in temperate climate. SERIS has published two studies in tropical climates [37], [70], with
one and three years of field data.
Data on the performance stability of FPV systems is still sparse. A systematic and detailed
analysis of the performance stability of FPV systems was published by SERIS [70]. Using three

## Página 45

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
45

years of data from a FPV test bed, PLRs were calculated for eight FPV strings. Three different
statistical methods (OLS, STL and YoY) were used to calculate PLRs, yielding values between
-0.7 and -0.5%/year, similar to PLR values of a nearby PV -rooftop system. It was however
highlighted that some failure modes specific for FPV could manifest at a later stage.
3.3.3 Indoor stress testing
Lab testing is used to study, in a controlled environment, the impact of stressors on various
PV components. In the lab environment, accelerated stress tests enable reliability screening
of key components in short timeframes to identify and mitigate qualit y issues before they
manifest as problems in actual installations. The IEC certification sets respective test
standards for GPV systems. The certificates generally do not certify different quality and
performance levels, but rather the required basic functionality and safety. The certification thus
guarantees the essential operating requirements. The use of accelerated stress to qualify PV
modules are covered in IEC 61215 [85] including stressors such as temperature, humidity,
snow, wind and hail. The IEC 61730 [86] standard deals with the certification for mechanically
and electrically safe operation of PV modules over the expected service life of PV modules.
In FPV systems, it is important to test the mechanical strength of the modules under real
installation situations. As dynamic loads through wave and wind are to be expected, it is
recommended to request a Dynamic Mechanical Load Test in accordance with IEC TS 62782
[87]. Furthermore, if the system is designed for environments close to the sea , a Salt Mist
Corrosion Test following IEC 61701 [88] is applicable to all critical components.
In the FPV context, pre-normative work on accelerated stress testing will lay the foundation for
qualification standards for critical components such as floats, connectors, anchoring system,
PV modules and cabling. It is important that the developed stress testing regimes are founded
as much as possible in existing standard s for GPV and other relevant industries, to ensure
efficient and rapid implementation. At the same time, FPV-specific stressors as laid out in Table
2 shall be accounted for. It will thus take time to depart from the current situation without FPV-
specific standards towards a situation with an established certification framework leading to a
safer and more mature industry. Each step taken in this process  increases confidence and
reduces risk perception for bankers/investors. Due to some reported issues with insulation
resistance in FPV systems and the general risk of long-term exposure of electrical components
to water, sealing and galvanic corrosion and increased water ingress protection beyond the
IEC 62852 [89] standards are necessary. While DC cables for GPV installations are typically
qualified according to IEC 62930 [90], and EN 50618 [91] respectively, cables for FPV
applications are not designed for longer-term submersion in water and may hence have issues
in permanently moist environments. Combiner boxes and inverters are typically designed as
fixed/non-moving parts and if installed on t he floating bodies certainly also need to be tested
such that they withstand the potentially higher humidity and dynamic load associated with FPV
projects.
DNV is currently working together with the FPV community by creating recommended practice
documents as a technical reference for inland FPV in all its aspects covering the floats,
anchoring & mooring, design, energy yield analysis and electrical components . As an early
result, the world’s first recommended practice on the design, development, and operation of
FPV systems (DNV -RP-0584) was successfully introduced in 2021 [13]. Next steps are
currently taken to expand this reference into design standards for floats, anchoring and
mooring.

## Página 46

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
46

For the electrical aspects of FPV, modification of current IEC standards is under discussion in
the IEC TC82 working groups [92]. These standardization activities are so far focusing on
inland water FPV where the technology readiness level (TRL) is larger than 8.  Offshore FPV
is still in an experimental stage with only a few pilot and demo projects with TRL levels between
3 and 5. A lot of data collection and learnings from pilots , demos and scientific research is
required to progress towards full maturity and design guidelines for large scale, low cost, and
reliable offshore FPV farms. The goal is that technical standards adequate ly capture, among
others, mechanical stress at the joints of rigid structures and testing of marine conditions like
corrosive environment, tides, waves, biofouling of floats and parts in contact with water.
3.3.4 Simulations
Simulations are one convenient option to overcome the lack of experimental (long term) data.
The advantage of simulations is that virtually every operating condition can be simulated and
long-term behavior investigated. Also, simulations enable an in-depth analysis of phenomena
of interest, unhindered by measuring devices of limited precision. The drawback is that each
simulation is only a model of reality using certain simplifications and assumptions, which must
be drawn wisely. Therefore, it is important to use validated simulation models to obtain reliable
data. Typically, a combination of experiments and simulations yields the most accurate results,
and experiments can often be performed on scaled or simplified samples.
Stressors may be amplified or altere d in FPV applications , and simulations are of particular
interest to study the influence of:
1. Wind loads through Computational Fluid Dynamics (CFD) and mechanical simulations
2. Moisture ingress through mass transport simulations
3. Hotspot formation through electrical and thermal simulations
4. Thermally induced stress through thermal and mechanical simulations
To all, the finite element method (FEM) can be applied, which is a method to model complex
geometries in detail by splitting it into smaller fragments. But also, other appropriate methods
can be used. In the following, a fitting simulation method is briefly introduced for each of the
four stressors. To study superposition of the stressors, the models could be combined.
Simulation Models: mechanical loads
For GPV systems, the primary environmental sources of mechanical loading are snow and
wind, in addition to impacts from hail. These systems are typically mounted on rigid, ground -
fixed structures, where the modules and electrical components are either static or moved in a
controlled manner by motorized mechanics, usually along one axis to track the sun. In
comparison, FPV systems face a more complex set of environmental conditions. In addition to
wind, snow, and hail, FPV systems must also withstand waves, currents, and water level
variations. To manage these forces, FPV support structures are generally more dynamic. At
larger scales, the entire system may have freedom of movement depending on the anchoring
and mooring design. At smaller scales, different su bparts of the system, such as individual
floats, can move relative to each other, although restricted by hinges or other mechanical
connectors. Modelling these dynamics accurately is a challenging task. The modelling
approach depends heavily on the specifi c problem and may require multi -scale modelling
techniques and the integration of various modelling tools
If looking at the PV module specifically, it was not until recently that CFD was coupled to FEM
simulations for GPV to translate CFD -computed wind pressure distributions on the module
exterior computed into FEM-computed detailed stress levels in the module interior [93]. To do

## Página 47

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
47

a similar exercise for a FPV structure would additionally require coupling to modelling tools
capable of handling both the hydrodynamics of the system and the flexibility of its components,
such as 3DFloat [94] or Orcaflex [95]. The complexity of the hydrodynamic situation requires
additional input from potential flow multi -body solvers (e.g., WAMIT [96]), input from similar
mid-fidelity fluid simulation software or the development of new engineering models. This holds
especially for large arrays of connected units where interaction and damping effects become
important. Another challenge is being able to use the high-level structural loads as computed
by these modelling tools to obtain the previously discussed detailed stress distributions interior
to the modules, which would be required to fully understand the implications of the floating
environment on the structural performance of these units. Modelling the wind loads could also
be a challenge for some systems as the local flow field becomes complex close to the water
surface and when there are many units close together. The motion of the floating units due to
the waves also means that dynamic coupled si mulations of this issue is necessary, i.e., CFD
simulations with the PV units standing still will not be sufficient. Wind loads are likely significant
when a large number of tilted panels are exposed to th e wind, the total load being potentially
design-driving for, e.g., the mooring system. Simpler approaches within only one modelling
tool might be sufficient to address more narrowly defined problems; an example is the effect
of O&M personnel walking on modules in a membrane FPV concept [97]. The sheer variety of
studied FPV concepts makes developing relevant modelling tools challenging. This is further
exacerbated by the fact that most concepts have significant differences compared to more
established floating technologies, such as, e.g., floating offshore wind [98], for which current
modelling tools and mechanical design guidelines for floating structures were developed.
Simulation Models: moisture ingress
Moisture ingress in PV modules is the origin of a range of degradation effects, including
metallization corrosion, discoloration of polymers and PID. This is detailed and illustrated in
[99]. Thus, s imulating moisture ingress in PV modules using FEM is critical to gauge the
performance of a PV module design and its constituents during long-term outdoor exposure.
Moisture ingress modelling for FPV is critical since the modules can be exposed to higher
relative humidity due to proximity to water, as mentioned in Section 3.3.1. PV modules are
generally exposed to moisture in the form of water vapor. The water molecules are adsorbed
onto the surface of diffusing elements (backsheet, encapsulant and/or edge sealant,
depending on the module design) and then diffuse into the bulk material.
The commercially available finite element simulation package, COMSOL Multiphysics is
generally used for simulating moisture ingress in the PV industry. The diffusion is modeled by
using the Transport of Diluted Species (TDS) physics interface in COMSOL.
To model the moisture ingress in PV modules exposed outdoors, the diffusion coefficient is
modeled as a function of temperature using the Arrhenius equation, while the saturation
concentation is computed for varying temperature and relative humidity using the Arden Buck
equation [100] as reported in [101].
In some cases, Fickian diffusion cannot accurately describe measured moisture ingress or
egress. The Fickian model assumes that water molecules diffuse evenly though the material.
However, there can be states where the water molecules bond at certain sorption sites while
diffusing [102]. T herefore, other non -Fickian models, such as Langmuir and dual -diffusion
models, are used to model the diffusion behavior of water inside PV constituents [103], [104].

## Página 48

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
48

Simulation Models: hotspot formation
Hotspots may occur in any type of PV system. Although there is little published material
quantifying the losses due to bird droppings (and other soiling) on FPV systems, images and
anecdotal evidence strongly suggest that FPV systems are particularly exposed to this type of
soiling. Bird droppings can significantly reduce the irradiance reaching the cells in a PV system,
but also constitute hard shade, known to induce high temperatures in the cell. The dissipated
heat of a partially shaded solar cell in rev erse bias can lead to high temperatures that can
degrade the encapsulation and backsheet materials but also the solar cells in the module,
especially for heterojunction (HJT) solar cells which are known to be more sensitive to
temperature than Passivated Emitted and Rear Contact (PERC) or Tunnel Oxide Passivated
Contact (TOPCon) solar cells. Numerical tools such as SPICE [105] are used to compute the
dissipated heat.
Simulation Models: outlook
There are other FPV -relevant phenomena worth exploring numerically, such as thermally
induced stresses, which occur whenever there are high temperature gradients. For brittle
materials, such as glass or silicon solar cells, high tensile stresses can lead to fracture. In FPV
applications, wave slamming can exert both mechanical and thermal stress simultaneously.
Beinert et al. [106] developed a coupled thermal and mechanical FEM model, which takes real
weather data into account to simulate the PV module temperature and from this the stress and
fracture probability of mainly the PV module glass. This method could be extended to take the
cooling by water and waves into account.
Even with all sub models of relevant FPV degradation processes in place, the actual challenge
consists of coupling them to account for co-occuring stressors on interacting FPV components,
also comprising feedback loops that are hard to capture through modelling single processes.
Some of the underlying interdependencies between mechanical loads are briefly laid out in the
respective section on simulation models but have not yet been captured in their entirety.
Moreover, relevant interdependencies stretch to other stressor domains, e.g., moisture ingress
and corrosion also depend on the position of affected components above water, which in turn
is affected by mechanical loads on and within the FPV system. To identify, prioritize and
subsequently model these interdependencies is essen tial for obtaining a proper multiphysics
model of FPV degradation.

## Página 49

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
49

 OPERATION AND MAINTENANCE OF FLOATING PV
This chapter highlights new monitoring equipment and O&M actions that must be performed
for FPV systems compared to the existing, well -established standards and best practices for
GPV. The chapter details observed challenges within O&M of FPV power plants and discusses
FPV specific cost of O&M. Finally, we p rovide our prespective on  areas where new O&M
technology and solutions can be of significant value for FPV.
4.1 Instrumentation
There are currently no standards available that describe the recommended sensors and
procedures for monitoring of FPV power plants. Instrumentation requirements for GPV power
plants, including requirements with respect to accuracy can be found in IEC 61724 -1 [107].
Requirements related to the number of sensors, also according to IEC 61724 , is included in
Table 3. For recommendations regarding FPV systems, DNVs recommended practice
published in 2021 [13] can provide guidance until a standard is published.
The purpose of the monitoring is essential to establish which parameters should be monitored,
and with what accuracy. IEC 61724-1 defines two classes of monitoring systems, Class A ,
intended for large PV systems (large commercial or utility)  and Class B, for smaller systems
(rooftop to medium commercial) . Table 4 provides an overview of parameters needed for
monitoring of FPV systems (Class A in IEC 61724-1). The overview is compiled based on IEC
61724-1 and DNVs recommended practice.
Table 3. Multiplier table for sensors according to 61724-1 [107]. Referenced in Table 4.
System Size (AC) MW Multiplier
< 40 2
≥ 40 < 100 3
≥ 100 to < 300  4
≥ 300 to < 500 5
≥ 500 to < 700 6
≥ 700  7, plus 1 for each additional 200 MW

Table 4. Compressed overview of parameters needed for monitoring of FPV systems
(Compiled based on Class A systems in IEC 61724-1 [107] and DNV’s recommended
practice [13]. Electrical parameters are not included).
Parameter Class A Number of sensors Sensor requirements Reference
In-plane irradiance X 1 x Table 3 Pyranometer: Class A per
ISO 9060:2018. PV
reference devices:
conform to IEC 60904-2
IEC 61724-1
Global Horizontal
Irradiance
X 1 x Table 3 IEC 61724-1
PV module
temperature
X 3 x Table 3 Resolution ≤ 0.1 °C
Uncertainty ≤ 1 oC

IEC 61724-1

## Página 50

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
50

Ambient air
temperature
X 1 x Table 3 Resolution ≤ 0.1°C,
Uncertainty ≤ 1°C

IEC 61724-1

Rainfall/precipitation X 1 x Table 3 Resolution 0.3 mm
Uncertainty < 5%
DNV RP/
IEC 61724-1
Wind speed X 1 x Table 3 Resolution: 0.1 m/s
Uncertainty ≤ 3%
DNV RP/
IEC 61724-1
Wind direction X 1 x Table 3 Uncertainty ≤ 3% DNV RP/
IEC 61724-1
Relative humidity NA Not included in IEC
61724-1
Uncertainty ≤ 3% DNV RP
Soiling ratio X 1 x Table 3 Local measurements of
soiling may not be
representative.
IEC 61724-1
Water temperature NA Not included in IEC
61724-1
Uncertainty ≤ 0.15 ̊C DNV RP
Waves NA Not included in IEC
61724-1
 DNV RP
Water current NA Not included in IEC
61724-1
Recommended methods:
Velocity-area and Acoustic
Doppler Current Profiler
DNV RP

The light green marked rows in Table 4 indicate the minimum requirement of a meteorological
monitoring station for yield assessment of FPV according to DNV RP. The only additional
parameter in the minimum requirement compared to IEC 61724-1 is relative humidity. For
ambient- and module temperature, wind speed and wind direction, DNV RP recommends
higher quality measurements than IEC 61724-1. For wind parameters, the recommendations
from DNV RP are used as these parameters may be more critical for an FPV system than a
GPV system, which the IEC 61724-1 is designed for. For ambient and module temperature ,
Table 4 refers to the values in IEC 61724 -1. The importance of the different environmental
parameters, such as water temperature, current and waves will vary with FPV technology,
while the impact of humidity on yield is not determined. The term accuracy, used in DNV RP,
is here replace by the term uncertainty. More details can be found in the references.
4.2 Main O&M actions, importance and best practices
O&M for FPV systems encompasses a combination of routine (preventive and corrective)
maintenance tasks, continuous monitoring  & predictive maintenance tasks, as illustrated in
Figure 17, in addition to risk preparedness (or emergency-response) plans. Streamlined O&M
practices are indispensable to ensure the long -term performance, reliability, safety, and
environmental sustainability of these systems, through a twofold mission: i) efficient mitigation
of potential technical risks (hence, downtime), ii) maximized long-term PV energy yield, with a
direct positive impact on LCOE and the payback time.

## Página 51

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
51

Figure 17. O&M approach for PV systems [7].
The main O&M challenges for FPV systems can be summarized as follows:
1. To address additional risks associated with the water-based working environment.
2. To e nsure accessibility and reachability for all maintenance activities across all
components.
3. To provide safe and cost -effective access to the floating platform, which is inherently
more complex, risky, and time-consuming than accessing ground-mounted plants.
4. To establish clear requirements for cleaning and maintenance, as poor accessibility
can lead to a high number of person -hours for O&M activities, potentially resulting in
longer downtime.

The inclusion of the water/marine dimension in O&M, for the case of FPV systems, implies
additional considerations and requirements necessary for ensuring minimal impact from and
to the environment, as well as efficient mitigation of FPV -specific safety and technical risks.
This can be related to key new (as compared to conventional PV) components such as floats,
anchors and mooring systems, as well as electrical components.
Table 5 summarizes the main O&M actions and their rationale, importance, and best practices.
The table includes information from the Best Practice Guidelines from Solar Power Europe [1],
Recommended Practice from DNV GL [13], results from the TRUSTPV and SerendiPV
projects [108], [109], [110]  and the IEC standard for operations and maintenance of GPV
systems [111].

## Página 52

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
52

Table 5: Main actions, their rationale, importance and best practices specific to FPV
O&M.
Action Rationale/Importance and overview of best practices
Anchoring/
mooring
systems
inspection
Anchoring and mooring systems are critical to maintain the stability of the FPV
installation and limit mechanical stresses (e.g. due to strong winds, wave forces,
etc.). Therefore, it is imperative for FPV asset managers to establish a
comprehensive O&M pl an dedicated to anchoring and mooring, covering
inspections, maintenance, and spare components scheduling and budgeting.
Although, normally, FPV-site specific risk assessments dictate the frequency and
level of detail of anchoring/mooring inspections, incr eased attention is given to
critical parts (e.g. those receiving relatively higher stresses or having sustained
previous failures) and in special cases e.g. following extreme weather events.
Regular (typically visual) inspections facilitated by trained specialized personnel
(divers) or remotely operated vehicles (ROVs) are imperative to assess issues
related to wear, fatigue, corrosion, chafing, marine growth, bio -fouling including
vegetation/algae growth and other forms of degradation or damage in the
anchoring and mooring systems. Key areas targeted for mooring inspections are
the mooring lines (continuous integrity checks and tension measurements). On
the other hand, anchor inspections focus – at minimum – on identifying physical
degradation of the anchor or its pad eye [13].
Floats
inspection
Buoyancy inspections are crucial in the FPV O&M agenda, aiming at identifying
any leaks, wear, fatigue or failure in the floating platforms. As in the case of
anchoring/mooring systems, more rigorous inspections of the floats are focused
on critical parts and in cases following extreme weather events. Potential
damages detectable from such inspections may include leaks due to punctures
and cracks, loss of buoyancy/stability, loosening of connection pins and corrosion
of metallic components [13].
FPV arrays
inspection
FPV arrays inspections are essential part of the FPV O&M and, as in the case of
GPV systems, are carried out according to the guidelines and requirements in IEC
62446-1 [112], IEC 62446-2 (maintenance procedures) [111] and IEC TS 62446-
3 (infrared imaging)  [113]. Such inspections, apart from detecting/diagnosing
common PV failures, are crucial for FPV systems to reveal and track degradation
mechanisms prominent in such marine environments, such as corrosion, moisture
ingress and UV degradation. Besides, due to th e typically limited accessibility of
FPV arrays, inspections by means of airborne equipment (e.g. drones) and remote
sensing technologies are favoured.

## Página 53

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
53

Action Rationale/Importance and overview of best practices
Soiling (and
snow) mitigation
Soiling mitigation plans in FPV O&M should ideally consider FPV -specific factors
such as the combined impact of humidity, water/salt spray, organic matter and
seasonal effects such as pollen and airborne sand. In practice, the severity of
soiling is difficult to predict, and it is normally determined either by measurements
on site or prior experience from the same area.
In areas where resident or migratory birds are present, significant soiling levels
may be encountered in the form of bird droppings. In such cases, monitoring of
bird population and historical records of bird presence and migrations can be
employed to iden tify the “high soiling risk” periods, in order to schedule (or
intensify) cleaning interventions, whereas measures to repel birds may be also
taken into account [1], [13]. Besides, aerial imagery (IR and RGB) inspections can
help detect and quantify soiling on FPV arrays caused by bird droppings [110],
which can be used to frame the frequency of the cleaning schedule. For FPV
projects in tropical areas or waters with high nutrients, such as irrigation ponds,
runoff from farmland, or areas with surrounding forests, biofouling is a potential
concern, as it can contribute to soiling losses or near-shading losses when plants
grow on the FPV arrays.
Cleaning interventions may also be important in the case of FPV installations in
snow-prone regions, where snowfalls and snow built -up on the FPV arrays can
result in significant losses, as well as excessive mechanical loads on key
components such as the floats and the FPV arrays.
The cleaning schedule of FPV systems can usually be tuned after sufficient
operational experience from a specific site.
Corrosion and
moisture ingress
FPV installations are characteristically prone to moisture ingress and corrosion
effects. Protecting metal components from corrosion is vital for the longevity of the
FPV system. On -site measures for corrosion protection, such as the application
of retrofit coatings, help maint ain the structural integrity of the different FPV
components. Attention is also given at monitoring (and mitigating, where
applicable) moisture ingress and humidity levels inside enclosures, whereas
diligent measures are necessary for certain FPV components exposed to UV, due
to the adverse effects of combined UV and humidity/corrosion stresses, that
accelerate physical, electrical and chemical degradation.
Circuitry and
cabling checks
The electrical circuitry equipment of FPV, including primarily cables and
connectors, requires periodic inspections and maintenance, in compliance with
IEC 60364, IEC 62446-2 and OEM manuals [111], [114]. Inspections are further
scrutinized for specific cases in FPV systems such as cables and connectors
inadvertently in contact with water, areas with potential insulation faults and
submerged cables which are often subject to marine organisms and buildup o f
organic matter. Finally,  an additional point of inspection for cables in FPV
installations is on cable runs to ensure that the appropriate amount of slackness
is present to prevent stress.

## Página 54

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
54

Action Rationale/Importance and overview of best practices
Earthing,
equipotential
bonding and
lightning
protection
system
Earthing is the main factor which needs regular inspection to ensure the safety of
O&M personnel. Earthing standards vary from country to country. It is necessary
to make sure the earthing resistance requirements as per the designed standard
are not compromised. Regular checking of earthing resistance value should be
inspected. If the system has been e arthed to water, then periodic checks of the
conductor (rod/tape) ensures that it has not been etched or corroded. Verification
is required to ensure that the cabling for equipotential bonding is still in good
condition.
Inverters
maintenance
Inverters’ maintenance procedures follow the technical specifications and
guidelines of the OEM manuals. Inverter inspections are triggered when
deviations in FPV performance are identified through the SCADA or monitoring
systems, as well as in follow-up of extreme weather events.
Monitoring &
Upkeep of
instrumentation
Monitoring should be implemented according to IEC 61724 -1 [107] and best
practices commonly applied to GPV systems, providing real -time data analytics
and feedback for early detection of underperformance and potential faults; thus
allowing for prompt corrective action, minimizing downtime and optimizing energy
production. Yet, specifically for FPV applications, string level monitoring sensors
are considered indispensable. This requirement allows FPV O&M teams to
identify underperforming strings with sufficient spatiotemporal granularity (time -
series data at string/comb iner box level), thus minimizing the need for on -site
interventions which are particularly costly and complex in the case of FPV, due to
their limited accessibility (need for access by boat, special equipment for marine
environments, etc.). In this sense, it would be advisable to invest upfront and
install equipment to monitor V and I at each string level.
Water quality
control
Maintaining water quality, including control of contaminants and algae propagation
are all crucial measures in the FPV O&M plan to prevent fouling and degradation
of the water environment, which in turn may have negative impact on both the
FPV performance and the local ecosystem.
Safety
inspections and
training
Safety inspections are an indispensable part of FPV O&M, aiming at protecting
the personnel working on or around (and under) the floating platform. Ongoing
training for O&M personnel, specific to FPV conditions and risks, ensures that they
are well equipped to handle routine mainte nance and respond effectively to any
issues. The water, the waves and the wind comprise the three main
(environmental) risk factors for worker safety in FPV installations.

4.3 Failure modes and effects analysis in O&M: example for FPV
Considering the relative infancy of FPV technology and, therefore, the limited experience from
in-field reliability of FPV installations throughout their operational lifecycle, there have been
limited data and rather fragmented understanding of FPV -specific failures and degradation
mechanisms. What is currently known has been summarized in detail in Chapter 3. In this
section, we take a broader view, looking at both technical and operational challenges and how
this impacts O&M using a failure modes and effects analysis (FMEA) approach. In Table 6, on
the basis of literature, public reports, research programs and  lessons learnt from
demonstrations in operational FPV installations, we provide a first FMEA for FPV systems [1],
[13], [64], [69], [108], [110], [115], [116] . Through this matrix, we identify potential flaws and

## Página 55

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
55

risks of failure/degradation in key FPV system components and assess their (indicative)
severity and risk priority number (RPN), to eventually (propose to) prioritize inspection and
mitigation actions at the design and O&M stages of FPV projects.
Table 6: Example Failure Modes and Effects Analysis (FMEA) matrix for FPV systems.
Failure mode Indicative
Occurrence
(1-4)
Indicative
severity
(1-5)
Indicative
RPN
(1-10)
Mitigation measure
Early / mid-life failures at FPV
module or array level (e.g. cell
cracks, delamination, PID,
hotspots, bypass diode
failures).
Power output loss and risk of
follow-up failures (e.g. fire).
2 3 8 Scheduled and/or data-driven
inspections (primarily visual, I-
V tracing, IR and EL images).
Repairs or replacement of
failed parts or PV module(s),
where applicable.
Soiling/debris build-up. Soiling
losses and potential hotspots.
2 2 5 Cleaning interventions at site-
specific intervals, through
manual or robotic solutions.
Deployment of anti-soiling
retrofits (e.g. coatings).
Buoyancy / float systems
failures. Loss of stability and
safety of the FPV arrays; risk
of follow-up failures e.g.
submerging or high
mechanical stresses on the
FPV arrays.
2 4 9 Scheduled and/or data-driven
inspections. Targeted
complementary inspections in
response to extreme weather
events or historical data
indications.
Anchor system failures;
Dislocation, loss of stability
and increased mechanical
stresses for the overall FPV
platform; risk of follow-up
failures e.g. on the FPV arrays
or the floats.
2 4 8 Scheduled and/or data-driven
inspections by specialized
personnel (divers) or remotely
operated vehicles (ROVs).
Targeted complementary
inspections in response to
extreme weather events or
historical data indications.
Failed or malfunctioning
electrical component, including
erroneous cabling; circuitry
cuts or shunts; risk of follow-
up failures (electrical arcs,
severe hotspots, fire).
3 4 9 Visual and electrical
inspections aided by
SCADA/monitoring system
alarms. Targeted inspections
of potential insulation faults
and cables that are fully

## Página 56

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
56

submerged or in potential
contact with water.
Inverter failure; Power losses
at PV string(s) level.
2 2-3 5 Scheduled O&M-manual
based inspections of inverters;
repairs or replacement where
applicable.
Water quality compromised;
Risk of follow-up fouling and
degradation of the local
ecosystem.
2 2 5 Implement water quality
management practices; use of
components/materials resistant
to water contamination.
Non-compliance to regulatory
framework updates
2 3 7 Establish regular audits and
follow-up of regulatory
framework at local, national
and international level.
Poorly established or
managed inventory of spare
parts
3 1-2 4 Use of return-of-
experience/historical data;
real-time tracking and update
of spare parts inventory.
Unexpected wide-scale
failures, including extreme
weather events; Extensive
failures and losses, potentially
at multiple components (e.g.
FPV arrays, anchors/mooring,
floats, inverters).
1 5 10 Deployment of emergency
response plans; Design of FPV
O&M plans for weather
resilience and preparedness,
including improved local
weather forecasts.
Monitoring system deficiency;
Misconfiguration; hardware or
software malfunction; data
quality compromised, data
gaps; Misdetection or delayed
detection of underperformance
issues; suboptimal
performance
3 1-2 5 Rigorous initial installation,
instrumentation, and
configuration, complying with
best practices and IEC
specifications. Benchmarking
with peer/similar or nearby PV
plants, to potentially uncover
undetected suboptimal
performance, due to deficient
monitoring.
Legend:
Occurrence 1 = Rare 2 = Occasional 3 = Likely 4 = Frequent
Severity 1-2 = Minor 2-3 = Minor Moderate 3 = Moderate 4 = Severe 5 = Highly severe
RPN <4 = Low priority 4-6 = Medium priority 7-9 = High priority 10 = Emergency

## Página 57

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
57

This FMEA matrix is aimed to be further and regularly updated and complemented in the future,
with future research outputs and new insights from broader return -of-experience in O&M of
real-scale FPV projects.
4.4 O&M budgeting – Cost aspects
O&M costs for FPV systems can be highly variable, based on multiple interrelated factors. In
general, when budgeting for the O&M of FPV systems, it is essential to conduct a thorough
survey including i) procurement and due diligence plans, ii) site and location (inshore, near -
shore, offshore, etc .) assessment, iii) consider the specific characteristics of the FPV
technology to be used (i.e. including its floats and anchoring/mooring technology), and iv)
account for the monitoring/inspection and maintenance needs in terms of hardware, software
and manpower, in order to ensure optimal performance and reliability throughout the whole
lifecycle of the FPV installation. An important aspect that is often overlooked in O&M budgeting
is the importance of staying upd ated on industry best practices, lessons learnt, innovations
and trends, the right tracking of which can help in identifying potential cost -saving measures
and streamline O&M schedules (switching from “per-schedule” and preventive, to data-driven
and predictive).
A representative list of key aspects and considerations when budgeting for FPV O&M projects
is given below [5], [110], [117].
• Site characteristics: accounting for factors such as the location (e.g., inland, nearshore,
offshore), water quality, microclimatic conditions and stressors, soiling, far shadings, etc.
• Technology and Design: as function of the chosen FPV technology and design, including
anchoring/mooring and buoyancy mechanisms and materials, which in turn can influence
e.g. the frequency or the complexity (and, thus, costs) of certain inspections.
• Accessibility and Logistics: for instance, remote or challenging-to-reach locations may
require specialized personnel and equipment which should increase O&M costs.
• Cleaning / Soiling mitigation needs: the choice of the soiling mitigation strategy in terms
of frequency and cleaning approach (manual or automated, waterless or water -based),
takes into consideration multiple factors, such as accessibility, FPV configuration and site
characteristics and has a direct impact on the overall O&M budget.
• Inspection of electrical components/BOS: accounting for factors such as the electrical
architecture, the type and size of inverters, the overall length of cabling, etc.
• Monitoring System / SCADA : accounting for costs of instrumentation, installation,
configuration and upkeeping of software and hardware components, as well as level of
automation. On the other hand, performance tracking and early detection of issues
through monitoring systems can contribute to streamlined cost -efficient O&M,
counterbalancing the above costs.
• Labor Costs and Training : accounting for all manned O&M activities, such as routine
inspections, cleaning and repairs interventions, upkeep of software and hardware, etc.
The chosen (or required) level of skillsets, availability and anticipated training of labor in
the project location has a direct impact on the global labor cost.
• Soft costs: accounting for insurance, regulatory compliance and warranty considerations.
• Spare parts and reserve for contingency : accounting for spare parts inventory
management and logistics, as well as for contingency funds (for instance, to address
unforeseen circumstances, prolonged downtime or emergency repairs, in the context of
emergency response plans e.g. following extreme weather events.

## Página 58

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
58

Figure 18 illustrates the breakdown of such FPV O&M costs into five main budgeting streams:
costs associated with the monitoring and inspections of all remote monitoring systems and
instrumentation (sensors, communication, etc.), inspection tools (drones, underwater vehicles
and ROVs), data analytics software and their upkeep. The key components and equipment
inspections budget encompasses all costs for inspection, repair/retrofitting, or replacement of
structural systems (mounting arrays, floating platforms, anchor ing/mooring), PV modules,
inverters, combiner boxes, cables, etc. Site management and control budgeting refers primarily
to environmental monitoring (water quality monitoring, monitoring, and assessment of impact
on aquatic life, compliance with environmental standards) and cleaning and biofouling control
plans (soiling mitigation through manual or automated systems, antifouling coatings, biofouling
monitoring). Labor costs include O&M payroll, training, and certification programs, as well as
external contractor costs for specialized tasks such as underwater interventions. Finally, soft
costs encompass regulatory compliance, safety, insurance, and financial reserves.

Figure 18. FPV O&M costs breakdown.
Yet, specific and detailed real-case figures for FPV O&M budgeting and breakdown are not
readily available, so far. NREL recently conducted a bottom -up analysis [5] of the installed
costs for FPV systems deployed on artificial water bodies under average site conditions (wind
load of about 40 m/s, snow load of 20 psf  (about 980 Pa), water depth of 50 m, water level
variation of 10 m, and swell height of 1 m); which may be a guide as well for assessing the
additional (“premium”) associated O&M costs as well, compared to standard PV. The study
estimated an installed system cost premium  of $0.26/WDC (25%) for 10 -MWDC fixed-tilt FPV
systems, compared with fixed -tilt GPV, indicating that higher structural costs related to the
floats and anchoring system are the largest contributors to this premium [5].
4.5 Outlook: O&M challenges and opportunities
As utility scale FPV is still in an early phase , especially in terms of upscaling and O&M
experience, there are several ongoing and emerging R&D challenges (and therefore
opportunities) in the framework of FPV O&M, in the following areas:
• Monitoring and remote sensing:  there is a major need for addressing consistent
challenges associated with the remote (or semi -remote) nature of FPV installations,
especially offshore ones: i) the lack of reliable data transmission on one hand; ii) on the
other hand, the complexity and high co sts of distant wide -area communication and
monitoring/sensing systems. Leveraging unmanned aerial vehicles (notably hovering
drones) and satellite technology, cloud storage and Internet of Things solutions, along with
robust remote communication protocols,  will be a differentiator for future O&M services
tailored to FPV installations.

## Página 59

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
59

• Expert dependence: in addition to the FPV remoteness and monitoring challenges, the
complex and multidisciplinary nature of FPV installations, involving several different,
distant and interdependent systems (FPV arrays, electrical systems, anchoring/mooring,
floats, etc.) sign ificantly increases the expert dependence in O&M, compared to GPV
O&M. For instance, corrective maintenance interventions in FPV platforms often require
specialized personnel (e.g. divers, marine engineers and technicians, etc.), while  FPV
inspections and analysis of FPV operational data are far more time -consuming tasks
(compared to standard PV), involving a number of different experts and equipment
operators. Emerging R&D and innovation opportunities here lie upon the development and
deployment of advanced FPV data analytics, artificial intelligence (AI) and UAV -based
inspections and autonomous interventions (e.g. drone -based imagery, drone -based
robotic cleaning), for data-driven predictive and unmanned O&M in FPV.
• Extreme weather stressors and FPV-specific degradation: marine environments and
associated microclimatic stressors are typically more aggressive and complex to assess
in FPV installations, compared to standard PV ones. Further R&D is required towards
improving the longevity of key FPV components, i.e. PV modules, anc hor/mooring and
floating structures, and submerged cables at both design (novel materials and coatings,
passive protection configurations) and post -commissioning level (retrofitting solutions),
notably against corrosion, UV exposure, and mechanical stresses. Besides, improved
weather preparedness and emergency-response plans based on data-driven approaches
are becoming indispensable for FPV installations, which are often more prone to large -
scale degradation and failures following extreme weather events , such as hurricanes,
severe storms or floods
• Environmental impact – Regulatory framework: impending concerns regarding the
impact of FPV installations and O&M on the local marine and near/inshore ecosystems
(e.g. How is the water quality and/or the aquatic flora/fauna affected under FPV arrays
shading? Which O&M tasks, such as detergent -based cleaning, should be excluded or
adapted to protect the aquatic ecosystem?) should be better investigated, assessed and
addressed, through further research and innovative alternatives. Such innovations are
focused on passive environmental- and habitat-friendly designs of FPV platforms, along
with evolving regulatory frameworks and standards for FPV O&M practices.

## Página 60

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
60

 CONCLUSION
FPV presents a significant opportunity to accelerate and facilitate the adoption of renewable
energy while mitigating the increasing pressure on land areas.
However, the present lack of established regulatory frameworks and limited long -term
experience with FPV systems creates uncertainty for developers, regulatory bodies, and
investors alike, posing significant challenges to accelerating FPV deployment. The industry is
characterized by rapid developments and high innovation rates, accompanied by a focus on
confidentiality and company -internal development which can hinder collaboration and data
sharing – crucial elements for research and development. However, t he potential for
deployment of FPV far surpasses the current market [7], giving compelling reason to believe
that the entire industry could benefit if developers, regulatory bodies and investors could lean
on more openly available data and knowledge.
This report aims to contribute to build a robust knowledge base that supports the development
of new standards, regulations, and technologies by gathering the data that is available and
illuminating gaps in current knowledge. The report summarizes the available knowledge from
scientific literature, reports and the experience of the authors, in three important aspects of
FPV power plants: energy yield, reliability, and operation and maintenance. Within each of
these fields, the focus is on addressing the areas where FPV differs from traditional ground -
based photovoltaic systems. Other important topics within FPV, such as environmental
impacts, offshore applications, recycling, calculations of deployment potentials and cost curves
are excluded from the report to limit scope and enhance readability. We recommend that these
aspects will be handled in separate reports. Targeted research efforts and access to data are
critical to close the identified knowledge gaps and this research should include, but not be
limited to:
• understanding and quantifying the unique operational conditions and stressors FPV
systems face, including wave action, wind loads, temperature, and biological fouling.
• developing and verifying models and methodologies to accurately predict how these
stressors impact FPV system performance over their lifetime and under different operating
conditions.
• develop methodologies and equipment to automate monitoring and maintenance
operations for FPV power plants
• understanding and quantifying environmental impacts of FPV systems:  evaluating the
potential effects of FPV on water quality, aquatic ecosystems, and surrounding habitats.
By addressing these research priorities, the industry can move towards a more mature and
sustainable deployment of FPV, ultimately paving the way for its widespread adoption.

## Página 61

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
61

REFERENCES
[1] SolarPower Europe, “Floating PV Best Practice Guidelines Version 1.0,” Dec. 2023.
[2] “Private Correspondence. Comment in Draft Report ‘PVPS Task 13 ST2.1 FPV Report for Internal
Review.docx’by Oktoviano Gandhi,” Nov. 25, 2024.
[3] Carlos D Rodríguez-Gallegos, “Global Floating PV Status and Potential,” Prog. Energy, vol. 7, no. 015001,
doi: DOI 10.1088/2516-1083/ad9074.
[4] M. Taglipietra, “Challenges and Opportunities in the FPV Industry in Europe,” presented at the European
Photovoltaic Solar Energy Conference and Exhibition, Vienna, Austria, Sep. 24, 2024.
[5] V. Ramasamy and R. Margolis, “Floating Photovoltaic System Cost Benchmark: Q1 2021 Installations on
Artificial Water Bodies,” NREL, Golden, CO: National Renewable Energy Laboratory, NREL/TP-7A40-80695,
Oct. 2021. doi: 10.2172/1828287.
[6] “Global floating PV status and potential Carlos D Rodríguez-Gallegos et al 2025 Prog. Energy 7 015001”.
[7] World Bank Group, ESMAP, and SERIS, “Where Sun Meets Water: Floating Solar Handbook for
Practitioners,” Washington, DC: World Bank, 2019.
[8] ASTM E1597-10, Standard Test Method for Saltwater Pressure Immersion and Temperature Testing of
Photovoltaic Modules for Marine Environments, 2019.
[9] T/CPIA 0016, High density polyethylene floating body used for photovoltaic (PV) power system on water,
2019.
[10] T/CPIA 0017, Code for design of water photovoltaic water system, 2019.
[11] T/CPIA 0018, Acceptance specification for floating photovoltaic power system, 2019.
[12] T/CPIA 0056, Code for design floating photovoltaic anchoring system, 2024.
[13] DNV GL, “Design, development and operation of floating solar photovoltaic systems,” Recommended
practice DNVGL-RP-0584, Mar. 2021.
[14] TR 100:2022, Floating photovoltaic power plants – Design guidelines and recommendations, 2022.
[15] IEC TS 62738:2018, Ground-mounted photovoltaic power plants - Design guidelines and recommendations,
2018.
[16] K. Ilgen, D. Schindler, S. Wieland, and J. Lange, “OPEN The impact of floating photovoltaic power plants on
lake water temperature and stratification,” Scientific Reports.
[17] R. L. G. Nobre et al., “Floating photovoltaics strongly reduce water temperature: A whole-lake experiment,”
Journal of Environmental Management, vol. 375, p. 124230, Feb. 2025, doi:
10.1016/j.jenvman.2025.124230.
[18] M. Melaet, “Large-scale floating photovoltaic systems impact the water quality of deep sand extraction lakes
in the Netherlands,” 2024.
[19] S. de Rijk, L. van Eck, E. van Veenendaal, M. Dionisio, A. Graef, and S. Wieland, “Monitoring Advice,
Deliverable 1.1 in HEU SuRE.”
[20] I. Nesheim, F. Clayer, A. Harby, and J. Selj, “Environmental and societal effects and impacts of hydro floating
solar power plants,” no. 8035–2024, 2024.
[21] J. Kester, J. Liu, and A. Binani, “Carbon Footprint of Floating PV Systems,” International Energy Agency
Photovoltaic Power Systems Programme, 2024. doi: 10.69766/JGAZ9626.
[22] S. Gadzanku, H. Mirletz, N. Lee, J. Daw, and A. Warren, “Benefits and Critical Knowledge Gaps in
Determining the Role of Floating Photovoltaics in the Energy-Water-Food Nexus,” Sustainability, vol. 13, no.
8, p. 4317, Apr. 2021, doi: 10.3390/su13084317.
[23] M. Sengupta, A. Habte, S. Wilbert, C. Gueymard, and J. Remund, “Best Practices Handbook for the
Collection and Use of Solar Resource Data for Solar Energy Applications: Third Edition,” IEA-PVPS 16-
02:2021, Apr. 2021. doi: 10.2172/1778700.
[24] A. Sparks, “nasapower: A NASA POWER Global Meteorology, Surface Solar Energy and Climatology Data
Client for R,” JOSS, vol. 3, no. 30, p. 1035, Oct. 2018, doi: 10.21105/joss.01035.
[25] S. Z. Golroodbari and W. Van Sark, “Simulation of performance differences between offshore and land‐
based photovoltaic systems,” Progress in Photovoltaics, vol. 28, no. 9, pp. 873–886, Sep. 2020, doi:
10.1002/pip.3276.

## Página 62

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
62

[26] B. Bjørneklett, “A solar power plant and method of installing a solar power plant,” 20210336578, Oct. 28,
2021
[27] B. Bjørneklett, “Solar power plant,” 10644645, May 05, 2020
[28] J. Stein, “PV Performance Modeling Methods and Practices: Results from the 4th PV Performance Modeling
Collaborative Workshop.,” Report IEA-PVPS T13-06:2017, Mar. 2017. doi: 10.2172/1347082.
[29] M. Dörenkämper, A. Wahed, A. Kumar, M. De Jong, J. Kroon, and T. Reindl, “The cooling effect of floating
PV in two different climate zones: A comparison of field test data from the Netherlands and Singapore,” Solar
Energy, vol. 214, pp. 239–247, Jan. 2021, doi: 10.1016/j.solener.2020.11.029.
[30] M. Dörenkämper, M. M. De Jong, J. Kroon, V. S. Nysted, J. Selj, and T. Kjeldstad, “Modeled and Measured
Operating Temperatures of Floating PV Modules: A Comparison,” Energies, vol. 16, no. 20, p. 7153, Oct.
2023, doi: 10.3390/en16207153.
[31] T. Kjeldstad, D. Lindholm, E. Marstein, and J. Selj, “Cooling of floating photovoltaics and the importance of
water temperature,” Solar Energy, vol. 218, pp. 544–551, Apr. 2021, doi: 10.1016/j.solener.2021.03.022.
[32] I. M. Peters and A. M. Nobre, “On Module Temperature in Floating PV Systems,” in 2020 47th IEEE
Photovoltaic Specialists Conference (PVSC), Calgary, AB, Canada: IEEE, Jun. 2020, pp. 0238–0241. doi:
10.1109/PVSC45281.2020.9300426.
[33] D. Faiman, “Assessing the outdoor operating temperature of photovoltaic modules,” Prog. Photovolt: Res.
Appl., vol. 16, no. 4, pp. 307–315, Jun. 2008, doi: 10.1002/pip.813.
[34] IEC 61853-2:2016, Photovoltaic (PV) module performance testing and energy rating - Part 2: Spectral
responsivity, incidence angle and module operating temperature measurements.
[35] H. Liu, V. Krishna, J. Lun Leung, T. Reindl, and L. Zhao, “Field experience and performance analysis of
floating PV technologies in the tropics,” Progress in Photovoltaics, vol. 26, no. 12, pp. 957–967, Dec. 2018,
doi: 10.1002/pip.3039.
[36] A. Driesse, J. Stein, and M. Theristis, “Improving Common PV Module Temperature Models by Incorporating
Radiative Losses to the Sky,” SAND2022-11604, 1884890, 709196, Aug. 2022. doi: 10.2172/1884890.
[37] H. Liu, V. Krishna, J. Lun Leung, T. Reindl, and L. Zhao, “Field experience and performance analysis of
floating PV technologies in the tropics,” Progress in Photovoltaics, vol. 26, no. 12, pp. 957–967, Dec. 2018,
doi: 10.1002/pip.3039.
[38] M. S. Ulset, “Thermal losses for floating PV - Wind direction dependencies,” presented at the 40th European
Photovoltaic Solar Energy Conference & Exhibition, Lisbon, Portugal, Sep. 18, 2023.
[39] D. Lindholm, T. Kjeldstad, J. Selj, E. S. Marstein, and H. G. Fjær, “Heat loss coefficients computed for
floating PV modules,” Progress in Photovoltaics, vol. 29, no. 12, pp. 1262–1273, Dec. 2021, doi:
10.1002/pip.3451.
[40] PVsyst, “Array Thermal losses.” Accessed: Nov. 05, 2024. [Online]. Available:
https://www.pvsyst.com/help/thermal_loss.htm
[41] M. Dörenkämper, D. van der Werf, K. Sinapis, M. de Jong, and W. Folkerts, “INFLUENCE OF WAVE
INDUCED MOVEMENTS ON THE PERFORMANCE OF FLOATING PV SYSTEMS,” in 36th European
Photovoltaic Solar Energy Conference and Exhibition, 2019.
[42] K. Chen et al., “Wave Induced Losses Simulation of Floating Solar Photovoltaic Systems at Open Waters,” in
Proceedings of the Thirty-third (2023) International Ocean and Polar Engineering Conference, Ottawa,
Canada: International Society of Offshore and Polar Engineers (ISOPE), Jun. 2023, pp. 670–677.
[43] V. S. Nysted et al., “Modelling wave-induced losses for floating photovoltaics: impact of design parameters
and environmental conditions,” Submitted, 2024.
[44] P. Borah, L. Micheli, and N. Sarmah, “Analysis of Soiling Loss in Photovoltaic Modules: A Review of the
Impact of Atmospheric Parameters, Soil Properties, and Mitigation Approaches,” Sustainability, vol. 15, no.
24, p. 16669, Dec. 2023, doi: 10.3390/su152416669.
[45] K. S. Anderson, C. W. Hansen, W. F. Holmgren, A. R. Jensen, M. A. Mikofski, and A. Driesse, “pvlib python:
2023 project update,” JOSS, vol. 8, no. 92, p. 5994, Dec. 2023, doi: 10.21105/joss.05994.
[46] M. Mikofski, B. Meyers, and C. Chaudhari, PVMismatch Project: https://github.com/SunPower/PVMismatch.
(2018). SunPower Corporation, Richmond, CA. [Online]. Available:
https://github.com/SunPower/PVMismatch
[47] “IEA_PVPS_T16_Solar_Res_Handbook_20211028.pdf.”

## Página 63

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
63

[48] M. Prilliman et al., “Quantifying Uncertainty in PV Energy Estimates Final Report,” NREL, NREL/TP-7A40-
84993, Mar. 2023. doi: 10.2172/1961370.
[49] BIPM et al., “Evaluation of measurement data — Guide to the expression of uncertainty in measurement.”
Joint Committee for Guides in Metrology, Sep. 2008.
[50] C. Reise, B. Müller, D. Moser, G. Belluardo, and P. Ingenhoven, “Uncertainties in PV system yield
predictions and assessments,” International Energy Agency IEA, Report IEA-PVPS T13-12:2018, 2018.
[51] C. Hansen and C. Martin, “Photovoltaic System Modeling: Uncertainty and Sensitivity Analyses,” SAND2015-
6700, 1211576, 598837, Aug. 2015. doi: 10.2172/1211576.
[52] C.-F. Chen, “Power Supply Reliability Analysis on Floating Photovoltaic Systems through Exceedance
Probability Approach,” J. Jpn. Inst. Energy, vol. 101, no. 7, pp. 138–146, Jul. 2022, doi: 10.3775/jie.101.138.
[53] G. Otnes, N. Roosloot, B. Aarseth, and J. Selj, Aspects-of-PV-reliability.png. figshare, 2024. doi:
10.6084/M9.FIGSHARE.27453069.V1.
[54] K.-A. Weiß, L. S. Bruckman, R. H. French, G. Oreski, and T. Tanahashi, “Service Life Estimation for
Photovoltaic Modules,” IEA, Report IEA-PVPS T13-16:2021, Jun. 2021.
[55] IEC 60050-191:1990, International Electrotechnical Vocabulary (IEV) - Part 191: Dependability and quality of
service, Dec. 31, 1990.
[56] M. Aghaei et al., “Review of degradation and failure phenomena in photovoltaic modules,” Renewable and
Sustainable Energy Reviews, vol. 159, p. 112160, May 2022, doi: 10.1016/j.rser.2022.112160.
[57] A. Phinikarides, N. Kindyni, G. Makrides, and G. E. Georghiou, “Review of photovoltaic degradation rate
methodologies,” Renewable and Sustainable Energy Reviews, vol. 40, pp. 143–152, Dec. 2014, doi:
10.1016/j.rser.2014.07.155.
[58] S. Lindig, I. Kaaya, K.-A. Weiss, D. Moser, and M. Topic, “Review of Statistical and Analytical Degradation
Models for Photovoltaic Modules and Systems as Well as Related Improvements,” IEEE J. Photovoltaics,
vol. 8, no. 6, pp. 1773–1786, Nov. 2018, doi: 10.1109/JPHOTOV.2018.2870532.
[59] A. Gok, C. L. Fagerholm, R. H. French, and L. S. Bruckman, “Temporal evolution and pathway models of
poly(ethylene-terephthalate) degradation under multi-factor accelerated weathering exposures,” PLoS ONE,
vol. 14, no. 2, p. e0212258, Feb. 2019, doi: 10.1371/journal.pone.0212258.
[60] R. H. French et al., “Assessment of Performance Loss Rate of PV Power Systems,” Report IEA-PVPS T13-
22:2021, Apr. 2021.
[61] N. Holland, K. Kiefer, C. Reise, E. A. S. Filho, B. Kollosch, and B. Muller, “Applying unsupervised machine
learning for the detection of shading on a portfolio of commercial roof-top power plants in Germany,” in 2022
IEEE 49th Photovoltaics Specialists Conference (PVSC), Philadelphia, PA, USA: IEEE, Jun. 2022, pp. 0223–
0227. doi: 10.1109/PVSC48317.2022.9938592.
[62] J. Dai et al., “Design and construction of floating modular photovoltaic system for water reservoirs,” Energy,
vol. 191, p. 116549, Jan. 2020, doi: 10.1016/j.energy.2019.116549.
[63] S. K. Cromratie Clemons, C. R. Salloum, K. G. Herdegen, R. M. Kamens, and S. H. Gheewala, “Life cycle
assessment of a floating photovoltaic system and feasibility for application in Thailand,” Renewable Energy,
vol. 168, pp. 448–462, May 2021, doi: 10.1016/j.renene.2020.12.082.
[64] M. Kumar, H. Mohammed Niyaz, and R. Gupta, “Challenges and opportunities towards the development of
floating photovoltaic systems,” Solar Energy Materials and Solar Cells, vol. 233, p. 111408, Dec. 2021, doi:
10.1016/j.solmat.2021.111408.
[65] R. Kanotra and R. Shankar, “Floating Solar Photovoltaic Mooring System Design and Analysis,” in OCEANS
2022 - Chennai, Chennai, India: IEEE, Feb. 2022, pp. 1–9. doi:
10.1109/OCEANSChennai45887.2022.9775352.
[66] B. Vlaswinkel, P. Roos, and M. Nelissen, “Environmental Observations at the First Offshore Solar Farm in
the North Sea,” Sustainability, vol. 15, no. 8, p. 6533, Apr. 2023, doi: 10.3390/su15086533.
[67] A. Rao, R. Pillai, M. Mani, and P. Ramamurthy, “Influence of Dust Deposition on Photovoltaic Panel
Performance,” Energy Procedia, vol. 54, pp. 690–700, 2014, doi: 10.1016/j.egypro.2014.07.310.
[68] H. Ziar et al., “Innovative floating bifacial photovoltaic solutions for inland water areas,” Progress in
Photovoltaics, vol. 29, no. 7, pp. 725–743, Jul. 2021, doi: 10.1002/pip.3367.
[69] M. K. Kaymak and A. D. Şahin, “Problems encountered with floating photovoltaic systems under real
conditions: A new FPV concept and novel solutions,” Sustainable Energy Technologies and Assessments,
vol. 47, p. 101504, Oct. 2021, doi: 10.1016/j.seta.2021.101504.

## Página 64

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
64

[70] W. Luo et al., “Performance loss rates of floating photovoltaic installations in the tropics,” Solar Energy, vol.
219, pp. 58–64, May 2021, doi: 10.1016/j.solener.2020.12.019.
[71] B. Amiot et al., “FLOATING PHOTOVOLTAICS – ON-SITE MEASUREMENTS IN TEMPERATE CLIMATE
AND LAKE INFLUENCE ON MODULE BEHAVIOR,” in 37th European Photovoltaic Solar Energy
Conference and Exhibition, 2020.
[72] R. Claus and M. López, “Key issues in the design of floating photovoltaic structures for the marine
environment,” Renewable and Sustainable Energy Reviews, vol. 164, p. 112502, Aug. 2022, doi:
10.1016/j.rser.2022.112502.
[73] R. Rebelo, L. Fialho, and M. H. Novais, “Floating photovoltaic systems: photovoltaic cable submersion and
impacts analysis,” Mar. 30, 2021, arXiv: arXiv:2103.16246. doi: 10.48550/arXiv.2103.16246.
[74] P. Hacke, P. Burton, A. Hendrickson, S. Spataru, S. Glick, and K. Terwilliger, “Effects of photovoltaic module
soiling on glass surface resistance and potential-induced degradation,” in 2015 IEEE 42nd Photovoltaic
Specialist Conference (PVSC), New Orleans, LA: IEEE, Jun. 2015, pp. 1–4. doi:
10.1109/PVSC.2015.7355711.
[75] D. C. Jordan, N. Haegel, and T. M. Barnes, “Photovoltaics module reliability for the terawatt age,” Prog.
Energy, vol. 4, no. 2, p. 022002, Apr. 2022, doi: 10.1088/2516-1083/ac6111.
[76] N. Mavraki et al., “Fouling community composition on a pilot floating solar-energy installation in the coastal
Dutch North Sea,” Front. Mar. Sci., vol. 10, p. 1223766, Dec. 2023, doi: 10.3389/fmars.2023.1223766.
Adapted under Creative Commons Attribution (CC-BY) license.
[77] N. Roosloot, J. H. Selj, and G. Otnes, “Evaluating Durability of a Double Edge Sealant in a Floating
Photovoltaic Application,” IEEE J. Photovoltaics, pp. 1–8, 2024, doi: 10.1109/JPHOTOV.2024.3417420.
[78] E. Hasselbrink et al., “Validation of the PVLife model using 3 million module-years of live site data,” in 2013
IEEE 39th Photovoltaic Specialists Conference (PVSC), Tampa, FL, USA: IEEE, Jun. 2013, pp. 0007–0012.
doi: 10.1109/PVSC.2013.6744087.
[79] S. Lindig, M. Theristis, and D. Moser, “Best practices for photovoltaic performance loss rate calculations,”
Prog. Energy, vol. 4, no. 2, p. 022003, Apr. 2022, doi: 10.1088/2516-1083/ac655f.
[80] D. C. Jordan, M. G. Deceglie, and S. Kurtz, “PV degradation methodology comparison—a basis for a
standard,” presented at the IEEE 43rd Photovoltaic Specialists Conference (PVSC), Portland, OR, USA, Jun.
2016, pp. 273–278.
[81] D. C. Jordan, C. Deline, S. R. Kurtz, G. M. Kimball, and M. Anderson, “Robust PV Degradation Methodology
and Application,” IEEE J. Photovoltaics, vol. 8, no. 2, pp. 525–531, Mar. 2018, doi:
10.1109/JPHOTOV.2017.2779779.
[82] M. G. Deceglie, “RdTools: An Open Source Python Library for PV  Degradation Analysis,” presented at the
PV Systems Symposium, Albuquerque, May 02, 2018.
[83] S. Lindig, J. Ascencio-Vasquez, J. Leloux, D. Moser, and A. Reinders, “Performance Analysis and
Degradation of a Large Fleet of PV Systems,” IEEE J. Photovoltaics, vol. 11, no. 5, pp. 1312–1318, Sep.
2021, doi: 10.1109/JPHOTOV.2021.3093049.
[84] I. Kaaya, S. Lindig, K. Weiss, A. Virtuani, M. Sidrach De Cardona Ortin, and D. Moser, “Photovoltaic lifetime
forecast model based on degradation patterns,” Progress in Photovoltaics, vol. 28, no. 10, pp. 979–992, Oct.
2020, doi: 10.1002/pip.3280.
[85] IEC 61215-2021, Terrestrial photovoltaic (PV) modules - Design qualification and type approval, 2021.
[86] IEC 61730:2023, Photovoltaic (PV) module safety qualification, Sep. 13, 2023.
[87] IEC TS 62782:2016, Photovoltaic (PV) modules - Cyclic (dynamic) mechanical load testing, Mar. 09, 2016.
[88] IEC 61701:2020, Photovoltaic (PV) modules - Salt mist corrosion testing, Jun. 11, 2020.
[89] IEC 62852:2014, Connectors for DC-application in photovoltaic systems - Safety requirements and tests,
Nov. 06, 2014.
[90] IEC 62930:2017, Electric cables for photovoltaic systems with a voltage rating of 1,5 kV DC, Dec. 13, 2017.
[91] EN 50618:2014, Electric cables for photovoltaic systems, Dec. 2014.
[92] M. Pravettoni, Reliability of modules in floating photovoltaics: Stresses, severities and tests, (Nov. 01, 2023).
Accessed: Jun. 24, 2024. [Online Video]. Available: https://youtu.be/J1gI0YGcwiQ?feature=shared
[93] P. Romer, K. B. Pethani, and A. J. Beinert, “Effect of inhomogeneous loads on the mechanics of PV
modules,” Progress in Photovoltaics, vol. 32, no. 2, pp. 84–101, Feb. 2024, doi: 10.1002/pip.3738.

## Página 65

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
65

[94] T. A. Nygaard, J. De Vaal, F. Pierella, L. Oggiano, and R. Stenbro, “Development, Verification and Validation
of 3DFloat; Aero-servo-hydro-elastic Computations of Offshore Structures,” Energy Procedia, vol. 94, pp.
425–433, Sep. 2016, doi: 10.1016/j.egypro.2016.09.210.
[95] M. Ikhennicheu, A. Blanc, B. Danglade, and J.-C. Gilloteaux, “OrcaFlex Modelling of a Multi-Body Floating
Solar Island Subjected to Waves,” Energies, vol. 15, no. 23, p. 9260, Dec. 2022, doi: 10.3390/en15239260.
[96] WAMIT, Inc., “Wamit, Inc. - The State of the Art in Wave Interaction Analysis.” Accessed: Aug. 13, 2024.
[Online]. Available: https://www.wamit.com/manualv7.4/wamit_v74manual.html
[97] H. G. Fjær, “Stresses induced by personnel stepping on PV modules mounted on a floating elastic
membrane,” presented at the 40th European Photovoltaic Solar Energy Conference & Exhibition, Lisbon,
Sep. 18, 2023.
[98] A. Otter, J. Murphy, V. Pakrashi, A. Robertson, and C. Desmond, “A review of modelling techniques for
floating offshore wind turbines,” Wind Energy, vol. 25, no. 5, pp. 831–857, May 2022, doi: 10.1002/we.2701.
[99] O. K. Segbefia, A. G. Imenes, and T. O. Sætre, “Moisture ingress in photovoltaic modules: A review,” Solar
Energy, vol. 224, pp. 889–906, Aug. 2021, doi: 10.1016/j.solener.2021.06.055.
[100] A. L. Buck, “New Equations for Computing Vapor Pressure and Enhancement Factor,” Journal of Applied
Meteorology and Climatology, vol. 20, no. 12, pp. 1527–1532, Dec. 1981, doi: 10.1175/1520-
0450(1981)020<1527:NEFCVP>2.0.CO;2.
[101] E. Annigoni, “Reliability of photovoltaic modules: from indoor testing to long-term performance
prediction,” EPFL, Lausanne, 2018. doi: 10.5075/epfl-thesis-8672.
[102] X. Zhao, H. Zhang, W. Li, X. Li, W. Fan, and Y. Zhang, “Langmuir-diffusion model: Its modification and
further application to glutinous rice flour particles,” Journal of Food Process Engineering, vol. 43, no. 9, p.
e13470, 2020, doi: 10.1111/jfpe.13470.
[103] S. Mitterhofer, C. Barretta, L. F. Castillon, G. Oreski, M. Topic, and M. Jankovec, “A Dual-Transport
Model of Moisture Diffusion in PV Encapsulants for Finite-Element Simulations,” IEEE J. Photovoltaics, vol.
10, no. 1, pp. 94–102, Jan. 2020, doi: 10.1109/JPHOTOV.2019.2955182.
[104] M. D. Kempe, A. Watts, T. Shimpi, S. Ellis, and K. Barth, “Modeling of the effectiveness of novel edge
seal designs for fast, low‐Cap‐Ex manufacturing,” Energy Science & Engineering, vol. 11, no. 7, pp. 2314–
2329, Jul. 2023, doi: 10.1002/ese3.1455.
[105] L. W. Nagel and D. O. Pederson, “SPICE (Simulation Program with Integrated Circuit Emphasis),”
University of California, Berkeley., University of California, Berkeley., UCB/ERL M382, 1973. [Online].
Available: http://www2.eecs.berkeley.edu/Pubs/TechRpts/1973/22871.html
[106] A. J. Beinert, A. Mahfoudi, F. Ensslen, C. Erban, and P. Romer, “Assessment of Thermally Induced
Stress in BIPV Modules Using FEM Simulations,” in Proceedings of the 40th European Photovoltaic Solar
Energy EUPVSEC2023, Lisbon: [object Object], 2023. doi: 10.4229/EUPVSEC2023/4BO.5.3.
[107] IEC 61724-1:2021, Photovoltaic system performance - Part 1: Monitoring., 2021.
[108] “H2020 TRUST-PV project.” [Online]. Available: https://trust-pv.eu/
[109] S. Tonnel et al., “Guidelines for design, procurement and O&M friendly concepts for floating PV,”
TRUSTPV, Jun. 2023.
[110] “H2020 SERENDI-PV project.” [Online]. Available: https://serendipv.eu/
[111] IEC 62446-2:2020., Photovoltaic (PV) systems - Requirements for testing, documentation and
maintenance - Part 2: Grid connected systems - Maintenance of PV systems., IEC 62446-2:2020., 2020.
[112] IEC 62446-1:2016, Photovoltaic (PV) systems - Requirements for testing, documentation and
maintenance - Part 1: Grid connected systems - Documentation, commissioning tests and inspection, Jan.
19, 2016.
[113] IEC TS 62446-3:2017, Photovoltaic (PV) systems - Requirements for testing, documentation and
maintenance - Part 3: Photovoltaic modules and plants - Outdoor infrared thermography, Jun. 15, 2017.
[114] IEC 60364-1:2005, Low-voltage electrical installations - Part 1: Fundamental principles, assessment of
general characteristics, definitions., 2005.
[115] S. Zhao, Y. M. Low, C. D. Rodríguez-Gallegos, and T. Reindl, “Potential Root Causes for Failures in
Floating PV Systems,” presented at the ASME 2023 42nd International Conference on Ocean, Offshore and
Arctic Engineering, Melbourne, Australia: American Society of Mechanical Engineers Digital Collection, Sep.
2023. doi: 10.1115/OMAE2023-101868.

## Página 66

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
66

[116] C. Won, W. Lawrence, D. Kim, B. Kang, K. Kim, and G. Lee, “FLOATING PV POWER SYSTEM
EVALUATION OVER FIVE YEARS (2011~2016),” presented at the 32nd European Photovoltaic Solar
Energy Conference and Exhibition, 2016, pp. 1982–1984.
[117] A. Garrod, S. Neda Hussain, A. Ghosh, S. Nahata, C. Wynne, and S. Paver, “An assessment of floating
photovoltaic systems and energy storage methods: A comprehensive review,” Results in Engineering, vol.
21, p. 101940, Mar. 2024, doi: 10.1016/j.rineng.2024.101940.

## Página 67

Task 13 Reliability and Performance of Photovoltaic Systems – Floating PV Power Plants: A Review of Energy Yield, Reliability, and Maintenance
67
