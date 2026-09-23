# IEA_Task12_LCA_Guidelines

Fonte original: `IEA_Task12_LCA_Guidelines.pdf`

## Página 1

Methodology Guidelines
on Life Cycle Assessment
of Photovoltaic
2020
PVPS

Report IEA-PVPS T12-18: 2020

Task 12 PV Sustainability

## Página 2

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic

What is IEA PVPS TCP?
The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organization
for Economic Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with
a belief that the future of energy security and sustainability starts with global collaboration. The programme is made up of
6.000 experts across government, academia, and industry dedicated to advancing common research and the application
of specific energy technologies.
The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCP’s within the IEA and was established in
1993. The mission of the programme is to “enhance the international collaborative efforts which facil itate the role of
photovoltaic solar energy as a cornerstone in the transition to sustainable energy systems.” In order to achieve this, the
Programme’s participants have undertaken a variety of joint research projects in PV power systems applications. The
overall programme is headed by an Executive Committee, comprised of one delegate from each country or organisation
member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.
The IEA PVPS participating countries are Austra lia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France,
Germany, Israel, Italy, Japan, Korea, Malaysia, Mexico, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain,
Sweden, Switzerland, Thailand, Turkey, and the United States of America. The European Commission, Solar Power
Europe, the Smart Electric Power Alliance (SEPA), the Solar Energy Industries Association and the Cop- per Alliance are
also members.
Visit us at: www.iea-pvps.org
What is IEA PVPS Task 12?
Task 12 aims at fostering international collaboration in safety and sustainability that are crucial for assuring that PV grows
to levels enabling it to make a major contribution to the needs of the member countries and the world. The overall objectives
of Task 12 are to 1. Quantify the environmental profile of PV in comparison to other energy technologies; 2. Investigate
end of life management options for PV systems as deployment increases and older systems are dec ommissioned; 3.
Define and address environmental health & safety and other sustainability issues that are important for market growth.
The first objective of this task is well served by life cycle assessments (LCAs) that describe the energy -, material-, and
emission-flows in all the stages of the life of PV. The second objective is addressed through analysis of including recycling
and other circular economy pathways. For the third objective, Task 12 develops methods to quantify risks and opportunities
on topics of stakeholder interest. Task 12 is operated jointly by the National Renewable Energy Laboratory (NREL) and
the University of New South Wales (UNSW Sydney). Support from DOE and UNSW are gratefully acknowledged.

 Authors
 ➢ Main Content: R. Frischknecht, P. Stolz, G. Heath, M. Raugei, P. Sinha, M. de Wild-Scholten
 ➢ Editor: R. Frischknecht

DISCLAIMER
The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous.
Views, findings and publications of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretaria t or its
individual member countries
COVER PICTURE
Left : Q-cells  Right : Phoenix Solar
ISBN 978-3-906042-99-2: Methodology Guidelines on Life Cycle Assessment of Photovoltaic Electricity

## Página 3

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
5
INTERNATIONAL ENERGY AGENCY
PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

IEA PVPS
Task 12: PV Sustainability

Report IEA-PVPS T12-18:2020
4th edition - April 2020

ISBN 978-3-906042-99-2

Operating agents:
Garvin Heath, National Renewable Energy Laboratory, Golden, CO, USA
Jose Bilbao, University of New South Wales, Sydney, Australia

Authors:
Rolf Frischknecht, Philippe Stolz, Garvin Heath, Marco Raugei,
Parikhit Sinha, Mariska de Wild-Scholten

Contributors:
Jose Bilbao, Gabriele Eder, Pierpaolo Girardi, Michael Held,
Keiichi Komoto

## Página 4

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
6
3rd edition published in 2015:

Operating agents:
Garvin Heath, National Renewable Energy Laboratory, Golden, CO, USA
Andreas Wade, SolarPower Europe, Brussels, Belgium

Authors:
Rolf Frischknecht, Garvin Heath, Marco Raugei, Parikhit Sinha,
Mariska de Wild-Scholten

2nd edition published in 2011:

Operating agent:
Vasilis Fthenakis, Brookhaven National Laboratory
Upton, New York, USA

Authors:
Vasilis Fthenakis, Rolf Frischknecht, Marco Raugei, Hyung Chul Kim,
Erik Alsema, Michael Held and Mariska de Wild-Scholten

Contributors:
Annick Anctil, Didier Beloin-Saint-Pierre, Karin Flury, Daniel Fraile,
Masakazu Ito, Werner Pölz, Parikhit Sinha, and Pieterjan
Vanbuggenhout

Citation: R. Frischknecht, P. Stolz, G. Heath, M. Raugei, P. Sinha, M.  de W ild-Scholten, 2020, Methodology
Guidelines on Life Cycle Assessment of Photovoltaic Electricity, 4th edition, IEA PVPS Task 12, International Energy
Agency Photovoltaic Power Systems Programme

## Página 5

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
7
TABLE OF CONTENTS

Executive summary ................................ ................................ ................................ ........... 8
1. Introduction ................................ ................................ ................................ ............ 10
2. Motivation and Objectives ................................ ................................ ...................... 11
3. Methodological Guidelines ................................ ................................ ..................... 12
3.1. Photovoltaics-specific aspects ................................ ................................ .... 12
3.2. Life cycle inventory modelling aspects ................................ ....................... 15
3.3. Building-integrated PV systems ................................ ................................ .. 22
3.4. Life cycle impact assessment (LCIA) ................................ .......................... 23
3.5. Interpretation ................................ ................................ ..............................  26
3.6. Reporting and communication ................................ ................................ .... 28
References ................................ ................................ ................................ ....................... 30

## Página 6

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
8
EXECUTIVE SUMMARY
Life Cycle Assessment (LCA) is a structured, comprehensive method of quantifying material -
and energy -flows and their associated emissions caused in the life cycle 1 of goods and
services. The ISO 14040 and 14044 standards provide the framework for LCA. However, this
framework leaves the individual practitioner with a range of choices that can affect the results
and thus the conclusions of an LCA study. The present ve rsion of the IEA LCA guidelines is
the result of the third update. They were developed and are updated to provide guidance on
assuring consistency, balance, and quality to enhance the credibility and reliability of the
results from LCAs on photovoltaic (PV ) electricity generation systems. The guidelines
represent a consensus among the authors—PV LCA experts in North America, Europe, Asia
and Australia—for assumptions made on PV performance, decisions on process input and
emissions allocation, methods of analysis, and reporting of the results.
Guidance is given on PV -specific parameters used as inputs in LCA and on choices and
assumptions in life cycle inventory (LCI) analysis and on implementation of modelling
approaches. A consistent approach towards system modelling, the functional unit, the system
boundaries, water use modelling and the allocation aspects enhances the credibility of PV
electricity LCA studies and enables balanced LCA -based comparisons of different electricity
producing technologies. The c urrent guidelines cover electricity production with ground
mounted, building attached as well as building integrated PV systems. They are intended to
be applied on assessing commercially deployed PV technologies.
The document discusses metrics like greenho use gas emissions (GHG), cumulative energy
demand (CED), use of mineral and metal resources, particulate matter, acidification and water
use. Guidance is given for the definition of the energy payback time (EPBT), the non-renewable
energy payback time (NRE PBT), and the environmental impact mitigation potentials (IMP).
The indicator energy return on investment (EROI) is described in a separate IEA report (Raugei
et al. 2015). The interpretation of results should account for the fact that the environmental
impacts may be significantly influenced by parameters that depend on the geographical zone
and panel orientation as well as by a system’s boundary conditions and the modelling
approach.
Transparency in reporting is therefore of the utmost importance. Followi ng the guidelines in
the chapter on the reporting and communication of the results serves the need for producing
clear, comprehensive, and transparent reports. At a minimum, the following parameters shall
be reported in captions of result figures and tables:
1) PV technology (single and multi-crystalline silicon, CdTe, CIS, micromorphous silicon);
2) Type of system (e.g., roof-top, ground mount, fixed tilt or tracker);
3) Module-rated efficiency and degradation rate;
4) Lifetime of PV and BOS;
5) Location of installation;

1 The life cycle of goods and services covers raw material and primary energy extraction, material and energy
supply, manufacture, use and end of life, including transport and waste management services where needed.

## Página 7

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
9
6) Annual irradiation and expected annual electricity production with the given orientation and
inclination or system’s performance ratio.
Further important information that should be documented in the LCA report are: the time-frame
of data; the life cycle stages included; the pl ace/country/region of production (manufacturing
components) modelled; the explicit goal of the study including technical and modelling
assumptions and the name of the entity commissioning the study; the LCA approach used if
not process-based; the LCA softw are tool (e.g., Simapro, GaBi, other); the LCI database(s)
(e.g., UVEK LCI data DQRv2:2018, ecoinvent, GaBi, ELCD, Franklin, US LCI, IDEA) and
impact category indicators used, always including the version numbers; the general
information and assumptions re lated to the production of major input materials (e.g., solar
grade silicon, aluminium (primary and/or secondary production)); and electricity source if
known.

## Página 8

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
10
1. INTRODUCTION
Life Cycle Assessment (LCA) is a structured, comprehensive method of quantifying material-
and energy -flows and their associated emissions caused in the life cycle 2 of goods and
services. The ISO 14040- and 14044-standards provide the framework for LCA. However, this
framework leaves the individual practitioner with a range of choices that can affect the results
and thus the conclusions of an LCA study. Additional standards and guidelines have later been
published such as the ISO 21930 (Environmental Product Declaration on Construction
Products”, International Organization for Standard ization (ISO) 2017), and the Product
Environmental Footprint Category Rules (PEFCR) for PV electricity (TS PEF Pilot PV 2018).
The current IEA PVPS guidelines have been developed to offer guidance for consistency,
balance, and quality to enhance the credibility of the findings from LCAs on photovoltaic (PV)
electricity generation systems. The guidelines represent a consensus among the experts of
Task 12, whom are PV LCA experts in the United States, Europe, Asia and Australia, with
regard to assumptions on PV performance, pro-cess input and emissions allocation, impact
assessment methods, and reporting and communication of LCA-studies and their results. The
latter is of the utmost importance as parameters such as geographical zones and system
boundary conditions can significantly affect the results. Accordingly, transparency is essential
in comparing life cycle -based environmental impacts of the production of electricity (be it
produced with PV or any other electricity generation technology).
This guideline document forms the basis for the update (Frischknecht et al. 2020) of the IEA
PVPS Task 12 report T12 -04:2015 on Life cycle inventories of Photovoltaic electricity
generation (Frischknecht et al. 2015b).
The current, fourth edition of the guidelines expands the contents of the third edition, issued in
2015, with additional guidance on system parameters, building integrated PV, selected
modelling approaches, water use, recycling, and reporting requirements.

2 The life cycle of goods and services covers raw material and primary energy extraction, material and energy
supply, manufacture, use and end of life, including transport and waste management services where needed.

## Página 9

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
11
2. MOTIVATION AND OBJECTIVES
National and regional ene rgy policies require environmentally friendly electricity generating
technologies. The PV industry is experiencing rapid growth and evolution. The key
prerequisites for a life cycle assessment on environmental performance are the availability of
the most up-to-date information on PV performance and life cycle inventory (LCI) data, and of
recent, weighted -average data that accurately represent the mixture of PV technologies
available in operation in the country or region of study. The major motivation to provide these
methodological guidelines on LCA of PV electricity is due to the variety of approaches and the
need for transparent reporting of assumptions and key choices.
The following are the major objectives of this report:
• To provide guidance on how to establish the life cycle inventory of PV electricity.
• To provide guidance on which environmental impacts to address in life cycle impact
assessment and which impact category indicators to use.
• To provide guidance on how and what to document when reporting a nd interpreting
LCA of PV electricity.

## Página 10

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
12
3. METHODOLOGICAL GUIDELINES
All PV LCA studies should be accomplished according to the general LCA ISO standards
14040 and 14044 as well as to the ISO standard 14046 on water use. Deviations from the
nomenclature, procedures and methodologies compared to these standards for life cycle
assessment should be stated clearly.
The following guidelines are structured into six main areas:
• Subchapter 3.1 includes recommendations on default technical characteristics used in
the LCA of photovoltaic systems;
• Subchapter 3.2 covers aspects of modelling approaches in life cycle inventory analysis;
• Subchapter 3.3 covers aspects specific to electricity production with building integrated
PV systems;
• Subchapter 3.4 dea ls with life cycle impact assessment and which environmental
indicators to address;
• Subchapter 3.5 discusses interpretation aspects;
• Subchapter 3.6 covers issues related to reporting and communication.
3.1. Photovoltaics-specific aspects
3.1.1. Life expectancy
The recommended life expectancy used in life cycle assessments of photovoltaic components
and systems differentiates between the components:
• Modules: 30 years for mature module technologies (e.g., glass -glass or glass-Tedlar
backsheet) used in g round mounted, building attached and building integrated PV
modules3 ; life expectancy may be lower for foil-only encapsulation; this life expectancy
is based on typical PV module warranties (i.e., 20 % or less efficiency degradation after
25 years) and the expectation that modules last beyond their warranties.
• Inverters: 15 years for small plants (residential PV); 30 years with 10 % part
replacement every 10 years (the parts that are assumed to be replaced need to be
specified) for large size plants utility PV (Mason et al. 2006);
• Transformers: 30 years;
• Mounting and supporting structures: 30 years for building attached roof-top and façade
installations, and between 30 to 60 years for building integrated installations and for
ground-mount installations on metal supports. Sensitivity analyses should be carried
out by varying the service life of the ground -mount supporting structures within the
same time span;

3 Building integrated PV modules may be used longer than 30 years reflecting the longer service life of the building
elements (façades, roofs) they are used in. They will possibly show a substantially lower specific yield beyond 30
years. Whether or not building integrated PV modules have a longer service life is uncertain. A service life of 30
years is recommended due to this uncertainty and for the sake of comparability with other PV systems

## Página 11

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
13
• Cabling: 30 years;
• Manufacturing plants (capital equipment): The lifetime may be shorter than 30 ye ars
due to the rapid development of technology. Assumptions need to be listed.
3.1.2. Irradiation
The irradiation collected by modules depends on their location and orientation. Depending on
the goal of the study, four main recommendations are given:
• Analysis of systems based on average technologies or on specific products : Assume
for all ground-mounted systems that the panels on an array plane are optimally oriented
and tilted at angles equal to the latitude (except when a specific system under study is
laid out differently, which should be reported). Also, assume that roof -top installations
are optimally oriented and tilted. Assume either optimally oriented or case -specific
orientation of panels of façade systems. Additionally, 1 -axis tracking systems may be
assumed. All assumptions, especially deviations from these general recommendations,
should be reported.
• Analysis of the average of installed systems in a grid network : The average actual
orientation, shading and irradiation should be used;
• Analysis of buildin g-integrated PV systems in a given building context : annual
irradiation incident on the PV surface should be determined using state -of-the-art
modelling software (the choice of software may depend on the planning stage of the
building);
• Analysis of bifacia l PV modules : annual irradiation, in particular the additional
irradiation on the backside, should be determined using state -of-the-art modelling
software.
The International Standard IEC 61724 offers a description of irradiance (W/m2) and irradiation
(also called insolation) (kWh/m2/yr). Breyer and Schmid (2010) provide country-specific plane
of array irradiation estimates for fixed-tilt and tracking PV systems.
3.1.3. Performance ratio
The performance ratio (PR) is defined by IEC 61724 as the ratio between the sy stem’s final
yield (actual AC generation) and the reference or ideal yield (DC rated performance) and is
widely used as a performance metric to quantify the overall system losses due to temperature
effects, soiling, shading and inefficiency of its componen ts. In general, PR increases with 1)
decline in temperature and 2) early monitoring of PV systems to detect and rectify defects.
Shading, if any, and soiling would have an adverse effect on PR. This means that well -
designed, well-ventilated, well-maintained, and large -scale systems generally have a higher
PR. Average annual PR data collected from many residential systems show an upward trend
from typical 0.7 in the 1990’ies with widely ranging values, to current values between 0.8 and
0.9 with less variance (Fraunhofer ISE 2019).
Using either site -specific PR values or a default value of 0.75 is recommended for roof -top
installations and 0.80 for ground-mounted utility installations (Fthenakis et al. 2008; Mason et
al. 2006; Pfatischer 2008); these default values include degradation caused by age. The
performance ratio of building -integrated PV systems and bifacial PV panels should be
determined individually for each application, due to the impacts of irradiance for each case and
the changes in DC:AC ratios that these systems might require. When site-specific PR values

## Página 12

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
14
are used based on performance from previous years, degradation -related losses should be
added to longer-term projections of the performance.
It is recommended to use actual performance data (ac tual energy yield in kWh per kWp)  of
installed technology whenever available or make reasonable assumptions that reflect actual
performance data when analyzing the average of installed PV systems in a grid network. This
can be aided by the use of PV system  modelling software. Such software can calculate the
output of the system over the duration of the project, making the calculation of the average PR
possible.
The PR is used in combination with solar irradiation data to determine actual yields.
3.1.4. Degradation
PV modules degrade over time reducing their efficiency and hence their output over their
lifetime. Hence, the annual degradation rate must be considered when estimating the total
yield of a PV system during the assessed period. The following de gradation rates are
recommended:
• Mature module technologies: Assume a linear degradation of 0.7 % -points per year
unless long-term scientific evidence and independently verified test results prove a
different value. A degradation of 0.7 %-points per year leads to a loss in yield of 21 %
during the last year of operation, which corresponds to an average reduction of the
initial efficiency of 10.5 % over the lifetime of 30 years. When annual yields are
extrapolated from site-specific data to calculate the total yield over the lifetime, it should
be clearly stated whether annual degradation rate is considered or not.
• Use an annual degradation rate of 0.5 %-points (instead of 0.7 %-points) in a sensitivity
analysis, resulting in an average reduction in the annual yield of 7.5 %.
More information on degradation rates for different PV technologies is available in Jordan et
al. (Jordan et al. 2016). It confirms the average degradation rate of 0.7 %-points per year.
In case actual, measured yields are reported for a PV plant for its whole lifetime, then no
additional calculations are required either using degradation rates or performance ratio (see
Section 3.1.3).
3.1.5. Curtailing and DC:AC ratio
The ratio of direct current (DC) nominal output of the PV panels to the altern ate current (AC)
inverter capacity is an important factor, in particular when the DC output of the PV panels is
significantly higher than the AC capacity of the inverter. PV electricity generated by a system
with a DC output of PV panels that is 1.2 times the AC capacity of its inverter is dependent
only upon the inverter capacity and its efficiency.
Utilities may apply curtailing PV electricity to be fed into their grid for various reasons. If this
situation applies, the reference flow should be represented including the curtailed amounts of
AC electricity.
3.1.6. Back-up Systems
Back-up systems such as temporal electricity storage, hydroelectric or gas combined cycle
power plants, or hybrid PV (combinations of PV and diesel aggregates) are considered to be
outside the system boundary of PV LCA (and for any other electricity generating technology).

## Página 13

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
15
The environmental performance of the combination of electricity generating technologies is
best assessed at the level of a utility’s (or micro-grid’s) power plant portfolio (see also Section
3.2.2). If a back-up system is included in a PV LCA, it should be explicitly and clearly described.
3.2. Life cycle inventory modelling aspects
3.2.1. System models
The appropriate system model depends on the goal of the LCA. Depending on the study’s goal
and scope, an attributional, decisional or consequential approach can be chosen (Frischknecht
& Stucki 2010; Sonnemann & Vigon 2011). Up to now, most LCAs are based on the
attributional approach.
The following goals can be distinguished which l end themselves to the use of different types
of LCAs on PV electricity (in parentheses):
A. Reporting environmental impacts of PV currently installed in a utility’s network,
comparisons of different PV systems, or of electricity -generating technologies
(retrospective / attributional LCA)
B. Choice of a PV electricity -supplier, switch of raw material or energy suppliers (short -
term prospective / decisional LCA)
C. Future energy supply situation: comparison of future PV systems or of future electricity-
generating technologies (use long-term prospective LCA / future attributional LCA to
model future static situations)
D. Large scale, long-term energy supply transition: large scale-up of PV in electricity grids
of nations and regions (use consequential LCA to model such transitions)
The following recommendations apply on all goals:
• The product system shall be divided into foreground - and background-processes. In
line with Sonnemann & Vigon (2011) the following definitions are proposed:
o Foreground processes are those which t he decision-maker or product-owner can
influence directly.
o Background processes are all remaining processes of the particular product
system.
o Additional discussion on background/foreground can be found in (Frischknecht
1998).
• We recommend using the conv entional process -based LCA developed by SETAC
(1993) and standardized by the ISO (International Organization for Standardization
(ISO) 2006a, b).
• Input-Output-based LCA method: This approach is not followed in this subtask within
IEA PVPS. More confidence in employing it is needed before its application is
recommend. This recommendation is in line with the Global Guidance Principles for
Life Cycle Assessment Databases published by the UNEP-SETAC Life Cycle Initiative
(Sonnemann & Vigon 2011).
• Hybrid method (combining Input -Output LCA and process based LCA, see e.g.
Hertwich et al. 2014; Wiedmann et al. 2011): If a hybrid approach is chosen, report
transparently and provide justification for using it.

## Página 14

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
16

The following recommendations apply to goal A described above (i.e., Reporting
environmental impacts of PV currently installed; comparisons of PV systems):
• Assume the present average electricity grid mix for the relevant country (e.g., Europe
(EU 28, including Norway and Switzerland), United States, Korea, China, or Japan)
when modelling the manufacture of current PV components. Specify the year for which
the data are valid.
• If a PV material is produced in a specific country, by a limited number of companies, or
if the PV material production generally involves a specific type of electricity supply, then
an argument can be made for selecting a country or company -specific electricity mix.
An example here is hydropower for producing silicon feedstock in Norway.
• However, country- or company-specific cases must be clearly reported so that data are
not unintentionally projected to different scales and regions.
The following recommendations apply to goal B (Choice of a PV electricity-supplier; switch of
feedstock or energy suppliers):
• Assume an annual marginal  electricity grid mix for the relevant country. Specify the
time span for which the changes in the grid mix are applicable. Use grid mix data from
relevant national or regional electricity scenario reports to derive the marginal mix (see
Frischknecht & Stucki (2010) for an example).
• Specify the environmental performance and energy efficiency of the power plants
contributing to this marginal electricity mix. The performance of these specific power
plants may differ from national or utility portfolio averages.
• Specify mid-term future, marginal market mixes of PV material feedstocks, chemicals,
energy carriers etc. which may contribute significantly to the PV life cycle -based
environmental impacts and where average and marginal mixes may differ substantially.
The following recommendations apply to goal C (Future energy supply situation):
• Use an annual-average future electricity mix for the relevant country when modelling
future production of PV components. Specify the year for which the forecasted data are
applicable. Use grid mix data from relevant national or regional electricity future
scenario reports.
• Specify the environmental performance and energy efficiency of the power plants
contributing to this future electricity mix. Being power plants operated in the future, they
should represent possible future states (see e.g. Frischknecht et al. 2015a).
• If a PV material is expected to be produced in a specific country, by a limited number
of companies, or if the material production generally uses a specific type of  electricity
supply, an argument can be made for choosing a country - or company -specific
electricity mix, e.g., hydropower for producing silicon feedstock production in Norway.
However, in prospective analyses, the availability of country -specific resources to the
projected market volumes must be documented. Country - or company-specific cases
must be identified clearly, so that data are not used unintentionally for projections to
different market volumes and regions.
• Adapt the efficiency of material supply -, transport-, and waste -management-services
so that they represent a possible future state, consistent with the underlying energy -
policy scenario (see e.g. Frischknecht & Stucki 2010; Frischknecht et al. 2015a;
Hertwich et al. 2014).

## Página 15

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
17

The following recomme ndations apply to goal D (Large scale, long -term energy supply
transition):
• Identify the main and significant changes in the economy (world -wide) which are
caused by a large scale -up of PV panel installation and production and consequently
electricity prod uction. This may be done by expert interviews, general or partial
equilibrium models, or backcasting techniques.
• Identify marginal technologies within the most relevant markets affected by the
changes in the economy. Use forecasting reports published by of ficial bodies or
industry associations.
• Establish life cycle inventories of these marginal technologies.
• Adapt the efficiency of future production of materials, transport -, and waste -
management-services so that they represent a possible future state, consi stent with
the underlying economic scenario (see e.g. Frischknecht & Stucki 2010; Frischknecht
et al. 2015a; Hertwich et al. 2014).
• Further aspects such as rebound effects and spillover effects may be taken into
account using economic models (e.g., general or partial equilibrium models), scenario
techniques or other suitable approaches (Girod 2009).
• Because consequential LCA is an emerging field and has not typically been applied to
PV, analysts should conduct a careful literature review to be aware of the latest
developments in the field (see e.g. Ekvall & Weidema 2004, Suh & Yang 2014,
Zamagni et al. 2012). Examples of consequential LCAs are, for instance, Vázquez -
Rowe et al. 2013, Lund et al. 2010, and Blanc (ed.) (2015).
3.2.2. Functional unit and reference flow
The functional unit allows consistent comparisons to be made of various PV systems and of
other electricity-generating systems that can provide the same function. We recommend using
the ISO’s language to distinguish between “functional unit” 4 and “reference flow”. The
reference flow 5 is used as the denominator of the cumulative emissions and resource
consumptions and the environmental impacts of the product system under study, whereas the
functional unit specifies the quantified performance of a product system.
We recommend the following functional unit for PV systems:
• AC electricity delivered to the grid quantified in kWh for comparison of PV technologies,
module technologies, and electricity-generating technologies in general (goals A to D).
For PV systems with dedicated transformers (e.g., utility solar farms), use the
electricity-output downstream of the transformer.

4 The functional unit is the quantified performance of a product system for use as a reference unit ( International
Organization for Standardization (ISO) 2006a, Clause 3.20).
5 The reference flow is a measure of the outputs from processes in a given product system required  to fulfil the
function expressed by the functional unit (International Organization for Standardization (ISO) 2006a, Clause 3.29).

## Página 16

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
18
Alternatively, the reference flows “m 2” or “kWp (rated power)” may be used. However, these
reference flows are not suitable for comparisons of other technologies to PV nor for
comparisons among PV technologies.
• m2 module can be used for quantifying the environmental impacts of the construction
and end of life efforts of PV systems attached to or integrated in a particular build ing,
including building integrated PV (BIPV) building elements, or of supporting structures
(excluding PV modules and inverters). Square metre (m2) shall not be used for
comparisons among PV and BIPV technologies covering manufacture, use and end of
life, because of differences in module and inverter efficiencies and performance ratios.
• kWp (rated power, DC) is used for quantifying the environmental impacts of electrical
parts, including inverter, transformer, wire, grid connection and grounding devices. The
kWp may also serve as the reference flow in quantifying the environmental impacts of
an individual module technology. However, the comparisons of module technologies
should not be based on nominal power (kWp) figures because the amount of kWh fed
to the grid may differ between the systems analysed.
The location, the module technology used, the voltage level, and whether and how the
transmission and distribution losses are accounted for, shall be specified.
AC electricity may differ in dispatchability an d intermittency. Electricity production with one
particular technology (PV or wind or nuclear) hardly meets all the demand at all times; thus
mixtures of power generating technologies are typically deployed. Aspects of dispatchability or
intermittency of AC electricity produced with different technologies shall not be addressed on
a technology level but on the level of grid mixes provided by utilities (see also Carbajales-Dale
et al. 2015).
3.2.3. System boundaries
This section defines the scope of the analysis for the product system of PV and BIPV electricity.
It offers guidance on what to include and exclude from the life cycle inventory analysis.
The following parts should be included in the system boundaries (stages according to EN
15804, 2013):
Product stage (Modules A1 to A3):
• Raw material and energy supply;
• Manufacture of the panels;
• Manufacture of the mounting system;
• Manufacture of the cabling;
• Manufacture of the inverters;
• Manufacture of all further components needed to produce electricity and supply it to
the grid (e.g., transformers for utility-scale PV).
Manufacturing in the product stage of the LCI should cover the following: energy- and material-
flows caused by manufacturing and warehousing, climate control, ventilation, lighting for
production halls, on-site emissions and their abatement, and on -site waste treatments. PV
manufacturing equipment should be included if data are available.

## Página 17

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
19
Construction stage (Modules A4 and A5):
• Transports to the PV power plant site (where the PV plant will be operated);
• Construction and installation, including foundation, supporting structures and fencing.
Use stage (Module B):
• Auxiliary electricity demand;
• Cleaning of panels;
• Maintenance;
• Repair and replacements, if any.
End of life stage (Module C):
• Deconstruction, dismantling;
• Transports;
• Waste processing;
• Recycling (see Section 3.2.5) and reuse;
• Disposal.
The following parts should be excluded:
• Commuting by employees (transportation to and from work);
• Administration, marketing, and research and development (R&D) activities.
3.2.4. Modelling water use
Water use and PV systems
Water use occurs during all life cycle stages of PV electricity. Water is used in industrial
processes of the supply chains of PV panels, for cleaning purposes during the operation of PV
systems and in the end of life stage in PV panel recycling.
Main reference and definitions
The main reference for modelling water use is the international standard on water footprint
(International Organization for Standardization (ISO) 2014). The terms used in this document
refer to the ISO standard on water footprint.
Water use inventory
This section explains how water consumption 6 can be quantified from inventory data (unit
processes) (see also Flury et al. 2012). Both water withdrawal or water consumption are often
assessed because both are relevant to different water -related impacts. Nevertheless, if one
has to choose, the IEA PVPS Task 12 experts consider water consumption preferential as a
single indicator, in particular with regard to water scarcity. This is in line with the Environmental
Footprint method, which assesses water consumption with the AWARE indicator 7 (see

6 Water removed from,  but not returned to, the same drainage basin  (ISO 14046, International Organization for
Standardization (ISO) 2014
7 The AWARE indicator is recommended by the Life Cycle Initiative, hosted by UN Environment.

## Página 18

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
20
Subchapter 3.4). Following this, how to establish a water consumption inventory is described
in this section. The basic information can however easily be used to quantify water withdrawal,
if considered more appropriate and if the inventory information available is complete.
The life cycle inventory data should include the entire water balance (including rainwater). To
do so, new elementary flows with country and/or regional codes must be introduced so that a
regional assessment is possible. Input of water is now no longer differentiated by source, but
rather subsumed under one elementary flow. Embodied water, i.e., water contained i n
products, is also considered a water input.
Tab. 3.1 provides an overview of elementary flows required for an industrial and agricultural
process as an example. The water input (1 + 2) should match the water output (sum of 3 to 7).
If rain water is also covered, it must be taken into account in the output as well, i.e., included
in the amount of evaporated (3), discharged (4, 5), infiltrated (6) and embodied (7) water,
respectively.
The following is the minimum information required for a complete inventor y and a flexible
assessment of processes:
• Water withdrawal, country- or region-specific (1)
• Evaporation: emission of water into the air, country-specific (3)
• Water released to the sea (and thus being lost), (5)
• Water contained in the product, country-specific (2, 7)

Tab. 3.1 Elementary flows for a complete inventory of water used in industrial and
agricultural processes
No. Elementary flow Industrial process Agricultural process
Input
1 Water, unspecified natural
source, country XY
Water for production process
(e.g. cleaning devices,
containers, etc.)
Water for irrigation
- Water, rain Not taken into account Taken into account for
complete inventory
2 Water, embodied, country
XY
Water embodied in raw
materials (including water
supply from water works)
Water embodied in seeds
Output
3 Water, country XY (emitted
to air)
Emission: water vaporized
during the production process
Emission: evaporated
irrigation water from farmed
fields
4 Water, river/lake Discharged directly from the
industry into surface waters
Discharged from fields into
surface waters
5 Water, sea Discharged directly from
industry into the sea
Discharged from the fields into
the sea
6 Water, soil Direct infiltration in the soil Infiltration in the soil from
fields
7 Water, embodied, country
XY Water embodied in the product Water embodied in the
product
Total
 Water withdrawal 1 1
 Consumptive water use 3+5+7-2 = 1-4-6 3+5+7-2 = 1-4-6

## Página 19

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
21
3.2.5. Modelling allocation and recycling
Consistent allocation rules are demanded for all multifunction processes (those simultaneously
producing several different products, e.g., electronic and off-grade silicon supply), recycling of
materials (e.g., using recy cled aluminium or copper), and employing waste heat (e.g., heat
recovery in municipal-waste incinerators). We recommend following the ISO standard 14044,
Clause 4.3.4 “Allocation” (International Organization for Standardization (ISO) 2006b).
It is recommended to perform several analyses on material recycling using the recycled content
(cut-off) allocation approach as default and the end-of-life (avoided burden) recycling approach
in a sensitivity analysis. A description and characterisation of both approach es is given in
Frischknecht (Frischknecht 2010). An example of the application of the recycled content and
the end of life approach to the current generation recycling of PV modules is provided in Stolz
et al. (2018). The life cycle inventories of PV systems published by Frischknecht et al. (2015b
and 2020) are based on the recycled content approach and should be combined with the
corresponding life cycle inventories for PV module recycling. The end -of-life approach is
recommended to be used when identifying the environmentally preferable end-of-life treatment
option of PV panels.
Building integrated PV (BIPV) is a special case of multifunctionality as these PV modules serve
as weather protection and energy producing elements. If required, an allocation of the
manufacturing efforts of BIPV panels shall be done based on clearly described criteria,
avoiding the derivation and application of credits as much as possible (see Subchapter 3.3).
In case system expansion (International Organization for Standardization (ISO) 2006b, Clause
4.3.4.2) is applied and environmental benefits and environmental impacts beyond the system
boundary are quantified (e.g., using the end-of-life (avoided burden) recycling approach), these
benefits and loads shall be reported separately. The benefits and impacts shall be quantified
in relation to the net amount of surplus secondary materials or fuels leaving the product system
(all outputs of a secondary material minus all inputs of that secondary material, see also EN
15804 (2013)).8
For the case of consequential LCAs (goal D in Section 3.2.1), allocation of multi -output and
recycling processes are typically based on system expansion according to, e.g., Ekvall &
Weidema (2004). In such cases the identification of technol ogies being displaced is key and
choices and assumptions should be reasoned and described.
3.2.6. Databases
The IEA PVPS Task 12 does not recommend any particular LCI database. However, in
choosing an LCI database, of the utmost importance is the transparency of the documentation
and availability of the unit process information and data.
The Swiss partners committed themselves to implementing the LCI data compiled within Task
12, Subtask 2 “LCA” (Frischknecht et al. 2015b) into a database used by the public authorities,
thereby facilitating the distribution of up -to-date and transparent LCI information on
photovoltaics. As of now, data are supplied in EcoSpold v1 format and following the ecoinvent

8 In end of life allocation, the benefit of recycling is realized from recycled material displacing primary production in
the future, with the environmental burdens and benefits of recycling allocated to the product producing the waste at
its end of life . In recycled content allocation, the recycling benefit is realized by the product using the recycled
content in its production

## Página 20

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
22
v2 guidelines and the KBOB guidelines 9. The Subtask 2 LCA partners  acknowledge and
support this commitment.
Product Environmental Footprint (PEF) studies shall use the secondary datasets listed in the
PEFCR (TS PEF Pilot PV 2018). The PEF -compliant datasets are freely available for use in
PEF studies. They can be downlo aded on different nodes of the Life Cycle Data Network 10.
Most of these datasets are at least partially aggregated, i.e. showing the life cycle inventory
results from cradle to gate rather than individual gate to gate unit process data.
3.3. Building-integrated PV systems
3.3.1. Goal and scope
Building-integrated photovoltaics (BIPV) may contribute to reducing the environmental footprint
of buildings during their entire life cycle (i.e., manufacture, construction, operation and end of
life). Environmental life cycle assessment may help to quantify the environmental footprint of
BIPV by answering the following questions:
• How big is the environmental footprint of a BIPV building element?
• How big is the environmental footprint of BIPV-generated electricity?
• How does the environmental performance of a building with BIPV compare to a building
with identical characteristics but without BIPV?
The life cycle assessment methodology of BIPV depends on the question to be answered. In
the following sections the main steps are exp lained for the questions about environmental
footprint of BIPV-generated electricity.
3.3.2. General recommendations
• The present PV LCA methodology guidelines and the EROI methodology guidelines
(Raugei et al. 2015) shall be applied unless otherwise stated in this Subchapter.
• The BIPV module, the substructure, cabling, and electronics should be modelled in
individual unit processes.
• Efficiency of BIPV modules should be based on manufacturer’s data.
• Any proven difference in lifetime of the BIPV elements versus t raditional PV modules
should be considered.
• The LCA of the manufacture of BIPV modules should as far as possible and feasible
be based on primary data.

9 As of October 2019, the Swiss Federal Offices and ecoinvent are  working on merging the contents of ecoinvent
data v3.6 (ecoinvent Centre 2019) and UVEK LCI data DQRv2:2018 (KBOB et al. 2018).
10 https://ec.europa.eu/environment/eussd/smgp/PEFCR_OEFSR_en.htm (accessed on 16.10.2019).

## Página 21

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
23
3.3.3. BIPV electricity
We recommend the LCA of BIPV electricity to adhere to the following terms:
• Functional unit: 1 kWh of AC electricity produced by BIPV on a specific building.
• Scope: The LCA should include the BIPV module (building element), the substructure
(specific to the BIPV building element), cabling and electronics (inverters,
microinverters, optimisers, etc.).
• Life cycle phases: the LCA should cover material supply and module production,
installation and mounting, operation, and EOL management.
• We recommend calculating the electricity production (specific yield) of BIPV installed
on a specific building using state-of-the-art modelling software (the choice of software
may depend on the planning stage of the building) or using measurements covering
several years.
• Other operational aspects like cleaning and regular inspections should be taken  into
account in the operation phase.
• Allocation: we recommend determining the share of the environmental footprint of the
BIPV building element attributable to the electricity production, by identifying the active
elements required to produce electricity  (semiconductor material, EVA foil, cabling,
electronics). The remaining parts (weather protection: glass layer; substructure) are
attributed to the building.
3.4. Life cycle impact assessment (LCIA)
In environmental life cycle impact assessment of PV electric ity, the midpoint indicators of the
PEFCR (TS PEF Pilot PV 2018; European Commission 2017; Fazio et al. 2018) should be
used.
The default midpoint indicators are complemented by additional indicators to quantify the
radiotoxicity potential of nuclear waste, the renewable and non-renewable cumulative energy
demand and the biodiversity damage potential caused by land use. The last indicator is
intended to replace the land use indicator used in the PEFCR. The biodiversity damage
potential caused by land use reached the level of “recommendation“ in the harmonisation effort
of life cycle impact assessment indicators within the Life Cycle Initiative hosted by UN
Environment (see Frischknecht & Jolliet 2016). The indicators are shown in Tab. 3.2.

## Página 22

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
24
Tab. 3.2 List of life cycle impact assessment indicators to be addressed in PV LCA
studies (TS PEF Pilot PV 2018; European Commission 2017; Fazio et al. 2018; Zampori
& Pant 2019) CFC: Chlorofluorocarbon; kBq : kilo Bequerel; NMVOC: non methane
volatile organic carbon; Sb: Antimony; n.i.: not indicated in Zampori & Pant (2019)
Impact category Indicator Unit  Recommended default LCIA method Robust-
ness
Indicators required according to the PEF guide and PEFCR
Climate change
Radiative forcing as Global
Warming Potential
(GWP100)
kg CO2 eq Baseline model of 100 years of the IPCC
(based on IPCC 2013)
I
Ozone depletion Ozone Depletion Potential
(ODP)
kg CFC-
11 eq
Steady-state ODPs 1999 as in WMO
assessment
I
Human toxicity,
cancer
Comparative Toxic Unit
for humans (CTUh) CTUh USEtox model (Rosenbaum et al. 2008) III
Human toxicity,
non- cancer
Comparative Toxic Unit
for humans (CTUh) CTUh USEtox model (Rosenbaum et al. 2008) III
Particulate
matter Impact on human health  disease
incidence
UNEP recommended model (Fantke et al.
2016)
I
Ionising
radiation, human
health
Human exposure
efficiency relative to U235 kBq U235
Human health effect model as developed
by Dreicer et al. 1995 (Frischknecht et al.
2000)
II
Photochemical
ozone formation,
human health
Tropospheric ozone
concentration increase
kg
NMVOC eq
LOTOS-EUROS model (Van Zelm et al.
2008) as implemented in ReCiPe
II
Acidification Accumulated Exceedance
(AE) mol H+ eq Accumulated Exceedance (Posch et al.
2008; Seppälä et al. 2006)
II
Eutrophication,
terrestrial
Accumulated Exceedance
(AE) mol N eq Accumulated Exceedance (Posch et al.
2008; Seppälä et al. 2006)
II
Eutrophication,
freshwater
Fraction of nutrients
reaching freshwater end
compartment (P)
kg P eq EUTREND model (Struijs et al. 2009) as
implemented in ReCiPe
II
Eutrophication,
marine
Fraction of nutrients
reaching marine end
compartment (N)
kg N eq EUTREND model (Struijs et al. 2009) as
implemented in ReCiPe
II
Ecotoxicity,
freshwater
Comparative Toxic Unit
for ecosystems (CTUe) CTUe USEtox model (Rosenbaum et al. 2008) III
Land use PEFCR indicator/method replaced by biodiversity loss indicator, see additional
indicators below

Water use
User deprivation potential
(deprivation-weighted
water consumption)
m3 world
eq
Available WAter REmaining (AWARE)
(Boulay et al. 2017)
III
Resource use,
minerals and
metals
Abiotic resource depletion
(ADP ultimate reserves) kg Sb eq CML 2002 (Guinée et al. 2001) and (van
Oers et al. 2002)
III
Resource use,
fossils
Abiotic resource depletion
– fossil fuels (ADP-fossil) MJ CML 2002 (Guinée et al. 2001) and (van
Oers et al. 2002)
III

## Página 23

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
25
Additional indicators
Land use Biodiversity loss PDF years Chaudhary et al. 2015; Chaudhary et al.
2016; Chaudhary & Brooks 2018
n.i.
Cumulative
energy demand,
renewable
Gross energy content of
renewable primary
energy resources
MJ oil eq. Frischknecht et al. 2015d
n.i.
Cumulative
energy demand,
non-renewable
Gross energy content of
non-renewable primary
energy resources
MJ oil eq. Frischknecht et al. 2015d
n.i.
Nuclear waste Radiotoxicity index, RTI m3 HAA e
q.
Frischknecht & Büsser Knöpfel 2013,
2014
n.i.

Most of the indicators listed in Tab. 3.2 are described in Hauschild et al. (2011). Some practical
aspects related to selected impact category indicators are described below.
Climate change: The most recent global warming potential (GWP) factors published by the
IPCC (2013, Chapter 8) should be used. Global Temperature increase potential (GTP) has
additionally been recommended as a useful metric in LCA (Cherubini et al. 2016). In line with
the Kyoto protocol and international agreements (United Nations 1998), GWP 100 year is
recommended as default and GTP 100 for use in sensitivity analyses.
Water use: This indicator should assess water scarcity due to c onsumptive water use. The
water turbined in hydroelectric power plants shall be excluded from the assessment. However,
the share of water evaporated from water reservoirs of hydroelectric power plants should be
included. Depending on the LCI database used,  the characterisation factors for the impact
category “water use” of the PEF method may need to be adapted or amended in order to
quantify water consumption and account for all relevant elementary flows. More information
may be obtained from the database providers.
Cumulative Energy Demand (CED) : The indicator “CED, non -renewable” (MJ oil -eq.)11
includes fossil and nuclear and the indicator “CED, renewable” (MJ oil -eq.) includes
hydropower, solar, wind, geothermal, and biomass. The indicators are quantifying the amount
or primary energy harvested (Frischknecht et al. 2007a; Frischknecht et al. 2007b;
Frischknecht et al. 2015c). It should always be stated which energy sources are included in
the CED indicator result. See also the discussion of CED in the context of Task 12 Net Energy
Analysis Guidelines (Raugei et al. 2015).
Long-term emissions contributing to human toxicity, ionising radiation, eutrophication,
and ecotoxicity: The quantification of the environmental impacts should be based on the
emissions occurring within 100 years. Environmental impacts due to long--term emissions, i.e.
beyond 100 years, may be quantified. If so, long-term environmental impacts shall be reported
separately.
In addition to the indicator -specific recommendations above, when using life cycle impact
assessment methods that use impact pathway analysis to estimating environmental damage,
be transparent about methodology and assumptions or clearly refer to the method and its
version applied.
To quantify environmental external  costs, we recommend using the generic external cost
factors published by the NEEDS project (NEEDS 2009).

11 The unit “MJ oil-eq” indicates that the cumulative energy demand is a life cycle impact category indicator similar
to the abiotic depletion potential which is expressed in kg Sb-eq (Frischknecht et al. 2015c).

## Página 24

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
26
3.5. Interpretation
3.5.1. Introduction
According to the ISO Standards on life cycle assessment, interpretation is the final phase of
the LCA procedure, in which the results of an LCI (life cycle inventory analysis) or an LCIA (life
cycle impact assessment), or both, are summarized and discussed as a basis for conclusions,
recommendations and decision-making in accordance with the definition of the goal and scope
of the LCA.
Some of the impact indicators described above and calculated in the impact assessment phase
may further be processed into energy payback times (EPBT, see Section 3.5.2), or
environmental impact mitigation potentials (IMPs) such as climate change (see Section 3.5.3),
or into energy return on investment (EROI) figures.
The two following sections describe the energy and the non -renewable energy payback time
indicators and then the environmental impact mitigation indicator. The reporting requirements
described in Section 3.6. apply to these indicators too. In contrast to com-mon life cycle impact
category indicators, the payback and mitigation indicators are very much dependent on the
context, i.e. on the energy and environmental efficiency of the el ectricity supplying system
assumed to be replaced by photovoltaics. Information and recommendations on the Energy
Return on Investment (EROI) indicator is given in the IEA PVPS report on Net Energy Analysis
(Raugei et al. 2015).
3.5.2. Energy Payback Time (EPBT) and Non-Renewable Energy Payback Time
(NREPBT)
Energy payback time is defined as the period required for a renewable energy system to
generate the same amount of energy (in terms of primary energy equivalent) that was used to
produce the system itself.
Energy Payback Time = (Emat + Emanuf + Etrans + Einst + EEOL) / ((Eagen / ȠG)– EO&M)
where,
Emat Primary energy demand (in MJ oil-eq) to produce materials comprising PV system
Emanuf Primary energy demand (in MJ oil-eq) to manufacture PV system
Etrans Primary energy demand (in MJ oil-eq) to transport materials used during the life cycle
Einst Primary energy demand (in MJ oil-eq) to install the system
EEOL Primary energy demand (in MJ oil-eq) for end-of-life management
Eagen Mean annual electricity generation
EO&M Annual primary energy demand (in MJ oil-eq) for operation and maintenance
ȠG Grid efficiency, the primary energy to electricity conversion efficiency at the demand
side (kWh electricity per MJ oil-eq)
The reasoning and assumptions applied to identify the relevant grid mix shall be documented.
Based on the above definition, there are two existing conceptual approaches to calculate the
EPBT of PV power systems.

## Página 25

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
27
1. PV as replacement of all energy resources used in the power grid mix.  This approach
calculates the time needed to compensate for the total (renewable and non -renewable)
primary energy required during the life cycle of a PV system (except the direct solar
radiation input during the operation phase, which is disregarded and thus not accounted
for as  part of EO&M). The annual electricity generation (Eagen) is converted into its
equivalent primary energy, based on the efficiency of electricity conversion at the demand
side, using the current average or average non -renewable (in attributional LCAs) or t he
long term marginal (in decisional/consequential LCAs) grid mix where the PV plant is being
installed.
2. PV as replacement of the non -renewable energy resources used in the power grid mix .
This approach calculates the EPBT by using the non -renewable primary energy only (as
recommended by Frischknecht et al. (1998)); renewable primary energy is not accounted
for, neither on the demand side (during manufacturing), nor during the operation ph ase.
This approach calculates the time needed to compensate for the non -renewable energy
required during the life cycle of a PV system. The annual electricity generation (Eagen) is
likewise converted to primary energy equivalent considering the non-renewable primary
energy to electricity conversion efficiency of the average or average non -renewable (in
attributional LCAs) or the long term marginal (in decisional/ consequential LCAs) grid mix
where the PV plant is being installed. The result of using this approach shall be identified
as Non -Renewable Energy Payback Time (NREPBT) to clearly distinguish it from the
EPBT derived from the 1st approach. The formula of NREPBT is identical to that of EPBT
described above except replacing “primary energy” with “non-renewable primary energy”.
Accordingly, grid efficiency, ηG, accounts for only non-renewable primary energy.

Both EPBT and NREPBT depend on the grid mix underlying the electri city conversion on the
demand side; however, excluding the renewable primary energy makes NREPBT more
sensitive to local or regional (e.g., product-specific use of hydro-power) conditions, which may
not be extrapolated to large global scales. On the other hand, EPBT metric with an average
large-scale (e.g. EU, or US, or World) grid conversion efficiency may not capture local or
regional conditions.
The calculated EPBT and NREPBT do not differ significantly in case the power plant mix of a
country or region is dominated by non-renewable power generation. However, as an increasing
share of renewable energies is expected in future power grid mixes as well as within the PV
supply chain, the two opposing effects of a reduction in the CED of PV and an increase in grid
efficiency will require careful consideration (Raugei 2011, 2013), and the numerical values of
EPBT or NREPBT may come to vary considerably according to the chosen approach.
Therefore, it is important to choose the approach that most accurately desc ribes the system
parameters and satisfies the goal of the LCA study. LCA practitioners may want to apply both
approaches and compare the results for transparency and clarity. In any case, it is mandatory
to specify the approach on which the calculation is based. In addition, specify the reference
system, e.g., today’s European electricity mix, today’s European non-renewable electricity (the
European electricity mix excluding electricity produced with renewable energies) mix or the
national electricity-supply mix in accordance to the system modelling and the goal of the LCA
(attributional/decisional/consequential). Specify and give the reference for the primary energy-
to-electricity conversion factor, and specify the energy contents of energy resources used t o
quantify the non-renewable and renewable cumulative energy demand.

## Página 26

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
28
3.5.3. Environmental impact mitigation potentials (IMP)
Environmental impact mitigation potentials (IMP) are quantified similar to the energy payback
times. This may comprise mitigation potentials regarding climate change impacts or high-level
nuclear waste (Jungbluth et al. 2008). These IMPs are quantified on a life time basis of the PV
system. On one hand the life cycle -based impacts potentially avoided with the lifetime
production of electricity with a PV system in a given economic, national or regional context are
quantified. On the other hand, the life cycle -based impacts caused by material supply,
manufacturing, installation, operation, maintenance and end -of-life management are
determined. Below the formula to quantify the climate change mitigation potential is shown.
Climate Change IMP = CCagen * G – (CCmat + CCmanuf + CCtrans + CCinst + CCEOL + CCO&M)
where,
CCmat Climate change impact (in kg CO2 -eq) of producing materials comprising PV
system
CCmanuf Climate change impact (in kg CO2-eq) of manufacturing PV system
CCtrans Climate change impact (in kg CO2 -eq) of transporting materials used during the
life cycle
CCinst Climate change impact (in kg CO2-eq) of installing the system
CCEOL Climate change impact (in kg CO2-eq) of end-of-life management
CCagen Life time electricity generation (in kWh)
CCO&M Life time climate change impact (in kg CO2-eq) of operation and maintenance
G Climate change impact (in kg CO2-eq/kWh) of grid electricity at the demand side
The impact assessment method applied should be clearly referenced, and the reference
system, e.g., today’s European electricity mix, today’s European non-renewable electricity mix
or the national electricity supply mix should be specified.
3.6. Reporting and communication
The life cycle assessment, energy payback time, environmental impact mitigation potential
results should come along with information about key parameters and other important aspects
characterising the PV system(s) analysed. The  list of items is separated in key parameters
required in the captions of figures and tables showing the results of the LCA (items 1 to 6) and
further important aspects which should be documented elsewhere in the same LCA report.
Key parameters to be documented in captions of figures and tables:
1. PV technology (e.g., single and multi-crystalline silicon, CdTe, CIS, amorphous silicon,
micromorphous silicon);
2. Type of system (e.g., roof -top (attached or integrated), ground mount, fixed tilt or
tracker);
3. Module-rated efficiency and degradation rate;
4. Lifetime of PV and balance of system (BOS);
5. Location of installation;

## Página 27

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
29
6. Annual irradiation, and expected annual electricity production with the given orientation
and inclination or system’s performance ratio;
Important aspects to be documented in the LCA report:
7. Time-frame of data;
8. Life cycle stages included;
9. The place/country/region of production modelled;
10. Type of electricity used and modelled in the supply chain (e.g., average grid medium
voltage European grid (Entso-e), site-specific power use (e.g., hydropower, coal));
11. Explicit goal of the study including
o Purpose of the study;
o Technical and modelling assumptions (e.g., historical or prospective LCA,
prototype or commercial production, current performance or ex pected future
development);
o Type of LCA model applied (attributional, consequential, etc.);
o The name of the entity commissioning the study;
12. LCA approach used (process -based, environmentally -extended input -output tables,
hybrid analysis);
13. LCA tool used (e.g., Simapro, GaBi, other), LCI database(s) used (e.g., UVEK LCI data
DQRv2:2018, ecoinvent, GaBi, ELCD, Franklin, NREL, IDEA, other), and impact
category indicators used, always including the version numbers;
14. Assumptions related to the production of major input materials, e.g. solar grade silicon,
aluminium (primary and/or secondary production), and electricity source if known.
Since a major part of the environmental impacts of PV systems is due to emissions from the
“background system”, (i.e., from producin g electricity and from the production of commodity
materials like glass, aluminium, plastics, and steel), separating the contributions of
“background” and “foreground” is recommended.

## Página 28

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
30
REFERENCES
Blanc I. (ed.) (2015) EcoSD Annual Workshop Consequential LCA. MINES ParisTech, Paris.
Boulay A.-M., Bare J., Benini L., Berger M., Lathuillière M., Manzardo A., Margni M., Motoshita M.,
Núñez M., Pastor A. V., Ridoutt B., Oki T., Worbe S. and Pfister S. (2017) The WULCA
consensus characterization model for water scarcity footprints: assessing impacts of water
consumption based on Available WAter REmaining (AWARE). In: The International Journal of
Life Cycle Assessment, pp. 1-11, 10.1007/s11367-017-1333-8.
Breyer C. and Schmid J. (2010) Population Density and Area Weighted Solar Irradiation: Global
Overview on Solar Resource Conditions for Fixed Tilted, 1-Axis and 2-Axes PV Systems. In
proceedings from: 25th EU PVSEC, Valencia, Spain.
Carbajales-Dale M., Raugei M., Fthenakis V. and Barnhart C. (2015) Energy return on investment
(EROI) of solar PV: an attempt at reconciliation. In: Proceedings of the IEEE, 103(7), pp., DOI:
10.1109/JPROC.2015.2438471.
Chaudhary A., Verones F., de Baan L. and Hellweg S. (2015) Quantifying Land Use Impacts on
Biodiversity: Combining Species–Area Models and Vulnerability Indicators. In: Environmental
Science & Technology, 49(16), pp. 9987-9995.
Chaudhary A., Pfister S. and Hellweg S. (2016) Spatially Explicit Analysis of Biodiversity Loss due to
Global Agriculture, Pasture and Forest Land Use from a Producer and Consumer Perspective.
In: Environmental Science & Technology, 50, pp. 3928–3936.
Chaudhary A. and Brooks T. M. (2018) Land Use Intensity-Specific Global Characterization Factors to
Assess Product Biodiversity Footprints. In: Environmental Science and Technology, ES&T, 52,
pp. 5094-5104, DOI: 10.1021/acs.est.7b05570.
Cherubini F., Fuglestvedt J. S., Gasser T., Reisinger A., Cavalett O., Huijbregts M., Johansson D. J. A.,
Jørgensen S. V., Raugei M., Schivley G., Størmman A., Tanaka K. and Levasseur A. (2016)
Bridging the gap between impact assessment methods and climate science. In:
Environmental Science and Policy, 64, pp. 129-140.
Dreicer M., Tort V. and Manen P. (1995) ExternE, Esternalities of Energy. Vol. Vol. 5 Nuclear (ed.
European Commission DGXII S., Research and development JOULE). Centre d'étude sur
l'Evaluation de la Protection dans le domaine nucléaire (CEPN), Luxembourg.
ecoinvent Centre (2019) ecoinvent data v3.6. ecoinvent Association, Zürich, Switzerland, retrieved
from: www.ecoinvent.org.
Ekvall T. and Weidema B. (2004) System Boundaries and Input Data in Consequential Life Cycle
Inventory Analysis. In: Int. J. Life Cycle Assess, 9(3), pp. 161-171, retrieved from: DOI:
10.1007/BF02994190.
EN 15804 (2013) EN 15804:2012+A1:2013 - Sustainability of construction works - Environmental
product declarations - Core rules for the product category of construction products.
European Committee for Standardisation (CEN), Brussels.
European Commission (2017) PEFCR Guidance Document - Guidance for the development of Product
Environmental Footprint Category Rules (PEFCRs), version 6.3, December 2017. European
Commission.
Fantke P., Evans J. S., Hodas N., Apte J. S., Jantunen M. J., Jolliet O. and McKone T. E. (2016) Health
impacts of fine particulate matter. In: Global Guidance for Life Cycle Impact Assessment
Indicators. UNEP, Paris.
Fazio S., Biganzioli F., De Laurentiis V., Zampori L., Sala S. and Diaconu E. (2018) Supporting
information to the characterisation factors of recommended EF Life Cycle Impact Assessment
methods, version 2, from ILCD to EF 3.0. PUBSY No. JRC114822. European Commission, Ispra.

## Página 29

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
31
Flury K., Frischknecht R., Muñoz I. and Jungbluth N. (2012) Recommendation for Life cycle inventory
analysis for water use and consumption. ESU-services Ltd., treeze Ltd., Unilever, Zürich,
Uster, London.
Fraunhofer ISE (2019) Photovoltaics Report (14 November 2019). Fraunhofer Institute for Solar
Energy System, ISE, Freiburg, Germany, retrieved from: www.ise.fraunhofer.de.
Frischknecht R. (1998) Life Cycle Inventory Analysis for Decision-Making: Scope-Dependent Inventory
System Models and Context-Specific Joint Product Allocation. 3-9520661-3-3. Eidgenössische
Technische Hochschule Zürich, Switzerland.
Frischknecht R., Braunschweig A., Hofstetter P. and Suter P. (2000) Modelling human health effects
of radioactive releases in Life Cycle Impact Assessment. In: Environmental Impact Assessment
Review, 20(2), pp. 159-189.
Frischknecht R., Althaus H.-J., Dones R., Hischier R., Jungbluth N., Nemecek T., Primas A. and Wernet
G. (2007a) Renewable Energy Assessment within the Cumulative Energy Demand Concept:
Challenges and Solutions. In proceedings from: SETAC Europe 14th LCA case study
symposium: Energy in LCA - LCA of Energy, 3-4 December 2007, Gothenburg, Sweden.
Frischknecht R., Jungbluth N., Althaus H.-J., Bauer C., Doka G., Dones R., Hellweg S., Hischier R.,
Humbert S., Margni M. and Nemecek T. (2007b) Implementation of Life Cycle Impact
Assessment Methods. ecoinvent report No. 3, v2.0. Swiss Centre for Life Cycle Inventories,
Dübendorf, CH, retrieved from: www.ecoinvent.org.
Frischknecht R. (2010) LCI modelling approaches applied on recycling of materials in view of
environmental sustainability, risk perception and eco-efficiency. In: Int J LCA, 15(7), pp. 666-
671, retrieved from: DOI: 10.1007/s11367-010-0201-6.
Frischknecht R. and Stucki M. (2010) Scope-dependent modelling of electricity supply in life cycle
assessments. In: Int J LCA, 15(8), pp. 806-816, retrieved from: DOI: 10.1007/s11367-010-
0200-7.
Frischknecht R. and Büsser Knöpfel S. (2013) Swiss Eco-Factors 2013 according to the Ecological
Scarcity Method. Methodological fundamentals and their application in Switzerland.
Environmental studies no. 1330. Federal Office for the Environment, Bern, retrieved from:
http://www.bafu.admin.ch/publikationen/publikation/01750/index.html?lang=en.
Frischknecht R. and Büsser Knöpfel S. (2014) Ecological scarcity 2013—new features and its
application in industry and administration—54th LCA forum, Ittigen/Berne, Switzerland,
December 5, 2013. In: Int J LCA, 19(6), pp. 1361-1366, 10.1007/s11367-014-0744-z.
Frischknecht R., Itten R. and Wyss F. (2015a) Life Cycle Assessment of Future Photovoltaic Electricity
Production from Residential-scale Systems Operated in Europe. International Energy Agency,
Geneva.
Frischknecht R., Itten R., Sinha P., de Wild Scholten M., Zhang J., Fthenakis V., Kim H. C., Raugei M.
and Stucki M. (2015b) Life Cycle Inventories and Life Cycle Assessments of Photovoltaic
Systems. International Energy Agency (IEA) PVPS Task 12.
Frischknecht R., Wyss F., Buesser S., Lützkendorf T. and Balouktsi M. (2015c) Cumulative energy
demand in LCA: the energy harvested approach. In: Int J LCA, online first, pp., DOI:
10.1007/s11367-015-0897-4.
Frischknecht R., Wyss F., Büsser Knöpfel S., Lützkendorf T. and Balouktsi M. (2015d) Cumulative
energy demand in LCA: the energy harvested approach. In: The International Journal of Life
Cycle Assessment, 20(7), pp. 957-969, 10.1007/s11367-015-0897-4, retrieved from:
http://dx.doi.org/10.1007/s11367-015-0897-4.
Frischknecht R. and Jolliet O. (ed.) (2016) Global Guidance on Environmental Life Cycle Impact
Assessment Indicators, Volume 1. United Nations Environment Programme, UNEP, Paris.
Frischknecht R., Stolz P., Sinha P., de Wild Scholten M., Zhang J., Fthenakis V., Kim H. C., Raugei M.

## Página 30

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
32
and Stucki M. (2020) Life Cycle Inventories and Life Cycle Assessments of Photovoltaic
Systems. International Energy Agency (IEA) PVPS Task 12.
Fthenakis V. M., Kim H. C. and Alsema E. (2008) Emissions from Photovoltaic Life Cycles. In:
Environmental Science and Technology, 42, pp. 2168-2174.
Girod B. (2009) Integration of Rebound Effects into LCA - Analysis of the Environmental Impact of
Product-Consumption Interactions. Swiss Federal Institute of Technology (ETH), Zurich.
Guinée J. B., (final editor), Gorrée M., Heijungs R., Huppes G., Kleijn R., de Koning A., van Oers L.,
Wegener Sleeswijk A., Suh S., Udo de Haes H. A., de Bruijn H., van Duin R., Huijbregts M. A. J.,
Lindeijer E., Roorda A. A. H. and Weidema B. P. (2001) Life cycle assessment; An operational
guide to the ISO standards; Part 3: Scientific Background. Ministry of Housing, Spatial
Planning and Environment (VROM) and Centre of Environmental Science (CML), Den Haag
and Leiden, The Netherlands, retrieved from:
www.leidenuniv.nl/cml/ssp/projects/lca2/lca2.html.
Hauschild M., Goedkoop M., Guinée J., Heijungs R., Huijbregts M. A. J., Jolliet O., Margni M. and De
Schryver A. (2011) Recommendations for Life Cycle Impact Assessment in the European
context - based on existing environmental impact assessment models and factors. European
Commission - DG Joint Research Centre, JRC, Institute for Environment and Sustainability
(IES), retrieved from: http://lct.jrc.ec.europa.eu/assessment/projects.
Hertwich E., Gibon T., Bouman E. A., Arvesen A., Suh S., Heath G. A., Bergesen J. D., Ramirez A., Vega
M. I. and Shi L. (2014) Integrated life-cycle assessment of electricity-supply scenarios
confirms global environmental benefit of low-carbon technologies. In: PNAS, 112(20), pp.
6277–6282, DOI: 10.1073/pnas.1312753111.
International Organization for Standardization (ISO) (2006a) Environmental management - Life cycle
assessment - Principles and framework. ISO 14040:2006; Second Edition 2006-06, Geneva,
Switzerland.
International Organization for Standardization (ISO) (2006b) Environmental management - Life cycle
assessment - Requirements and guidelines. ISO 14044:2006; First edition 2006-07-01,
Geneva, Switzerland.
International Organization for Standardization (ISO) (2014) Environmental management - Water
footprint - Principles, requirements and guidelines. ISO 14046. International Organization for
Standardization, ISO, Geneva, Switzerland.
International Organization for Standardization (ISO) (2017) Sustainability in buildings and civil
engineering works — Core rules for environmental product declarations of construction
products and services. ISO 21930:2017; Second edition 2017-07. International Organization
for Standardization (ISO), Geneva, Switzerland.
IPCC (2013) The IPCC fifth Assessment Report - Climate Change 2013: the Physical Science Basis.
Working Group I, IPCC Secretariat, Geneva, Switzerland.
Jordan D. C., Kurtz S. R., VanSant K. and Newmiller J. (2016) Compendium of photovoltaic
degradation rates. In: Prog. in Photov.: Res. and Appl., 24(online), pp. 978–989, DOI:
10.1002/pip.2744.
Jungbluth N., Frischknecht R. and Tuchschmid M. (2008) Life cycle assessment of photovoltaics in the
ecoinvent data v2.01. In proceedings from: 23rd European Photovoltaic Solar Energy
Conference and Exhibition, 1-5 September 2008, Valencia.
KBOB, eco-bau and IPB (2018) UVEK Ökobilanzdatenbestand DQRv2:2018. Koordinationskonferenz
der Bau- und Liegenschaftsorgane der öffentlichen Bauherren c/o BBL Bundesamt für Bauten
und Logistik, retrieved from: www.ecoinvent.org.
Lund H., Mathiesen B. V., Christensen P. and Schmidt J. H. (2010) Energy system analysis of marginal
electricity supply in consequential LCA. In: Int J LCA, 14(3), pp. 260-271, DOI:

## Página 31

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
33
10.1007/s11367-010-0164-7.
Mason J. M., Fthenakis V. M., Hansen T. and Kim H. C. (2006) Energy Pay-Back and Life Cycle CO2
Emissions of the BOS in an Optimized 3.5 MW PV Installation. In: Progress in Photovoltaics
Research and Applications, 14, pp. 179-190.
NEEDS (2009) NEEDS - New Energy Externalities Developments for Sustainability. Retrieved 29.6.2009
retrieved from: www.needs-project.org.
Pfatischer R. (2008) Evaluation of predicted and real operational data of different thin-film
technologies. In proceedings from: OTTI Thin Film User Forum, 28.01.2009, 9. April 2009,
Würzburg, retrieved from: energie.otti.de/thin_film_photovoltaics/.
Posch M., Seppälä J., Hettelingh J. P., Johansson M., Margni M. and Jolliet O. (2008) The role of
atmospheric dispersion models and ecosystem sensitivity in the determination of
characterisation factors for acidifiying and eutrophying emissions in LCIA. In: Int J LCA(13),
pp. 477-486.
Raugei M. (2011) Energy pay-back time: methodological caveats and future scenarios. In: Progress in
Photovoltaics: Research and Applications(21), pp. 797-801.
Raugei M. (2013) Energy pay-back time: methodological caveats and future scenarios. In: Progress in
Photovoltaics: Research and Applications(21), pp. 797-801.
Raugei M., Frischknecht R., Olson C., Sinha P. and Heath G. (2015) Methodology Guidelines on Net
Energy Analysis of Photovoltaic Electricity. Subtask 20 "LCA", IEA PVPS Task 12, retrieved
from: http://iea-pvps.org/index.php?id=56#c87.
Rosenbaum R. K., Bachmann T. M., Gold L. S., Huijbregts A. J., Jolliet O., Juraske R., Koehler A., Larsen
H. F., MacLeod M., Margni M., McKone T. E., Payet J., Schuhmacher M., van de Meent D. and
Hauschild M. Z. (2008) USEtox - the UNEP-SETAC toxicity model: recommended
characterisation factors for human toxicity and freshwater ecotoxicity in life cycle
assessment. In: International Journal of Life Cycle Assessment, 13(7), pp. 532-546.
Seppälä J., Posch M., Johansson M. and Hettelingh J. P. (2006) Country-dependent Characterisation
Factors for Acidification and Terrestrial Eutrophication Based on Accumulated Exceedance as
an Impact Category Indicator. In: Int J LCA, 11(6), pp. 403-416.
SETAC (1993) Guidelines for Life-Cycle Assessment: A "Code of Practice". In proceedings from: SETAC
Workshop, held at Sesimbra, Portugal, 31 March - 3 April 1993, Society of Environmental
Toxicology and Chemistry (SETAC), Brussels, Belgium and Pensacola (Florida, USA).
Sonnemann G. and Vigon B. (ed.) (2011) Global guidance principles for life cycle assessment
databases; A basis for greener processes and products. United Nations Environment
Programme, UNEP, Paris.
Stolz P., Frischknecht R., Wambach K., Sinha P. and Heath G. (2018) Life Cycle Assessment of Current
Photovoltaic Module Recycling. IEA-PVPS Task 12, International Energy Agency Photovoltaic
Power Systems Programme, Report IEA-PVPS T12-13:2018, retrieved from: http://www.iea-
pvps.org/index.php?id=9&eID=dam_frontend_push&docID=4254.
Struijs J., Beusen A., van Jaarsveld H. and Huijbregts M. A. J. (2009) Aquatic Eutrophication. In: ReCiPe
2008 A life cycle impact assessment method which comprises harmonised category indicators
at the midpoint and the endpoint level. Report I: Characterisation factors (Ed. Goedkoop M.,
Heijungs R., Heijbregts M. A. J., De Schryver A., Struijs J. and Van Zelm R.).
Suh S. and Yang Y. (2014) On the uncanny capabilities of consequential LCA. In: Int J LCA, 18(6), pp.
1179-1184 DOI: 10.1007/s11367-014-0739-9.
TS PEF Pilot PV (2018) Product Environmental Footprint Category Rules (PEFCR): Photovoltaic
Modules used in Photovoltaic Power Systems for Electricity Generation. treeze Ltd.,
commissioned by the Technical Secretariat of the PEF Pilot "Photovoltaic Electricity
Generation", Uster, Switzerland.

## Página 32

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
34
United Nations (1998) KYOTO PROTOCOL TO THE UNITED NATIONS FRAMEWORK CONVENTION ON
CLIMATE CHANGE.
van Oers L., de Koning A., Guinée J. B. and Huppes G. (2002) Abiotic resource depletion in LCA. Road
and Hydraulic Engineering Institute, Amsterdam.
Van Zelm R., Huijbregts M. A. J., Den Hollander H. A., Van Jaarsveld H. A., Sauter F. J., Struijs J., Van
Wijnen H. J. and Van de Meent D. (2008) European characterization factors for human health
damage of PM10 and ozone in life cycle impact assessment. In: Atmos Environ, 42, pp. 441-
453.
Vázquez-Rowe I., Rege S., Marvuglia A., Thénie J., Haurie A. and Benetto E. (2013) Application of
three independent consequential LCA approaches to the agricultural sector in Luxembourg.
In: Int J LCA, 18(8), pp. 1593-1604, DOI: 10.1007/s11367-013-0604-2
Wiedmann T. O., Suh S., Feng K., Lenzen M., Acquaye A., Scott K. and Barrett J. R. (2011) Application
of hybrid life cycle approaches to emerging energy technologies--the case of wind power in
the UK. In: Environ. Sci. Technol., 45(13), pp. 5900-5007, DOI: 10.1021/es2007287.
Zamagni A., Guinée J., Heijungs R., Masoni P. and Raggi A. (2012) Lights and shadows in
consequential LCA. In: Int J LCA, 16(7), pp. 904-918 DOI: 10.1007/s11367-012-0423-x.
Zampori L. and Pant R. (2019) Suggestions for updating the Product Environmental Footprint (PEF)
method. JRC115959. Publications Office of the European Union, Luxemburg.

## Página 33

Task 12 PV Sustainability – Methodology Guidelines on Life Cycle Assessment of Photovoltaic
1

Insert a QR
code linking to
the report.
Delete the
green frame
after.
