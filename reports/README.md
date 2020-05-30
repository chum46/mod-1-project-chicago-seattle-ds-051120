# Reports

Generated written analysis as Word Doc, HTML, PDF, LaTeX, etc.

# South King County Opportunity Youth

This project offers an updated estimate of the number of Opportunity Youth in South King County using the 2017 5-year American Community Survey [(ACS)](https://www.census.gov/programs-surveys/acs/about.html) Public Use Microdata Survey [(PUMS)](https://www.census.gov/programs-surveys/acs/technical-documentation/pums.html).

## THIS REPOSITORY

### Setup Instructions

If you are missing required software (e.g. Anaconda, PostgreSQL), please run the following command in Bash (designed for Mac computers):
```bash
# installs necessary requirements
# note: this may take anywhere from 10-20 minutes
sh src/requirements/install.sh
```

For Windows and Linux computers, you may need to manually ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/) and [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### `oy-env` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `oy-env` conda environment. To do so, please run the following commands *in your terminal*:

```bash
# create the oy-env conda environment
conda env create -f environment.yml

# activate the oy-env conda environment
conda activate oy-env

# if needed, make oy-env available to you as a kernel in jupyter
python -m ipykernel install --user --name oy-env --display-name "Python 3 (oy-env)"
```

Note that this may take 10 or more minutes depending on internet speed.

**Windows Note:** The same versions of these packages are not available for Windows computers, so all Windows users should use the `windows.yml` file instead of `environment.yml` (this file was generated on Windows 10)

**Linux Note:** The same versions of these packages are not available for Linux computers, so all Linux users should use the `linux.yml` file instead of `environment.yml` (this file was generated on Red Hat)

**Catalina Note:** You may need to modify the `prefix` at the very bottom of `environment.yml` if you are on macOS Catalina.  Run `conda env list` in your terminal to determine the appropriate path by looking at the paths of your existing conda environment(s).  Modify `environment.yml` then try running the installation commands listed above again.

On all operating systems, you will know that you have the required software if the following Bash commands do not return error or "not found" messages:
```bash
which conda
conda list geopandas
which psql
```

### Data Download

To download the relevant data, run the following command *in Python*:

```
data_collection.download_data_and_load_into_sql()
```

Note that this may take 10 or more minutes depending on internet speed.

There is an example notebook in the `notebooks/exploratory` directory with this code already added.

## BACKGROUND

Measuring the successes and barriers faced by our most vulnerable youth is a challenge in the South King County region<sup>1</sup>. While there is a lot of information gathered from K12 districts and colleges about student outcomes, few data exists among Opportunity Youth (OY): young folks between the age 16 through 24 who are disengaged from both work and school<sup>2</sup>. This population is of particular interest to The Seattle Region Partnership (SRP), a multi-sector initiative founded by the Seattle Metropolitan Chamber of Commerce, Seattle Foundation, City of Seattle, and King County<sup>3</sup>.

## PROJECT GOAL

The SRP would like an update on the estimated number of OY in South King County. According to a recent The Seattle Times article, the number of OY in South King County has remained steadfast at 19,000<sup>4</sup>. However, that estimation comes from a report that is over three years old. As Data Science Consultants, your task is to inform the SRP on the current status of OY in South King County using updated data.

## PROJECT REQUIREMENTS

At minimum, the SRP is expecting the following:

* A map that visualizes which parts of King County are a part of South King County;

* An update of the estimated number of OY in South King County. In addition the estimate, be sure to include a breakdown of the count of OY by Public Use Microdata Area (PUMA) within South King County;

* An update of the table “Opportunity Youth Status by Age” located on page 2 of the 2016 report “Opportunity Youth in the Road Map Project Region”; and

* A visualization that highlights a trend between the 2016 report and current data.

The SRP has asked that any extra time remaining be used to create the following items:

* Create a choropleth map of the count of OY by PUMA within South King County;

* For South King County, create a choropleth map that shows the percentage of jobs for workers age 29 or younger out of the total number of jobs per census block; and

* Of the census blocks where jobs for workers age 29 or younger are the majority of employed people, what are a few of the industries that employ this group of people?

* Utilize additional data sources to support your recommendations, e.g. [Census Bureau APIs](https://www.census.gov/data/developers/data-sets.html), [King County Open Data](https://data.kingcounty.gov/browse?limitTo=datasets&provenance=official), or [King County GIS Open Data](https://gis-kingcounty.opendata.arcgis.com/)

## LEARNING GOALS

The goal of this project is to showcase your newfound Python and PostgreSQL skills to generate analytical insights and communicate the high level takeaways to a non-technical audience. This project will emphasize the following learning goals:

* Break down a question into small technical tasks;

* Query data from a PostgreSQL database;

* Produce descriptive statistics;

* Visualize descriptive statistics; and

* Tell a story from the descriptive statistics.

## DELIVERABLES

To complete this project, you will need to turn in the following deliverables:

1. A public GitHub repository with a well organized directory structure (this structure has been provided for you in this project, but will not be provided in future projects)
2. An `environment.yml` file that contains all the necessary packages needed to recreate your conda environment.
    - Start with the provided `environment.yml`, then as you install any additional packages be sure to [export](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-the-environment-yml-file) the new version and commit the changes in git.
    - For Windows users, generate a `windows.yml` based on the provided `windows.yml`
    - For Linux users, generate a `linux.yml` based on the provided `linux.yml`
3. A standalone `src/` directory that stores all relevant source code.
    - Although you may not be able to achieve this goal in Mod 1, we encourage you to package code into .py files and store them in src, then import the functions into the appropriate notebooks. Be ware of premature optimization, however.  Don't try to package your code before it works.
    - All functions have docstrings that act as [professional-quality documentation](http://google.github.io/styleguide/pyguide.html#381-docstrings).
    - [Well documented](https://www.sqlstyle.guide/) SQL queries with appropriate single-line or multiline comments.
4. A user-focused `README.md` file that explains your process, methodology and findings.
    - Provide a directory of your repository so a visitor will know where to look for your report notebook, your source code, etc. 
    - Take the time to make sure that you craft your story well, and clearly explain your process and findings in a way that clearly shows both your technical expertise and your ability to communicate your results!
    - Begin with framing questions, describe your data source, include relevant, well labeled visualizations that support your conclusions, which come at the end.
5. A record of your workflow stored in `notebooks/exploratory`.  Don't be afraid to leave in error messages, so you know what didn't work!
6. One final Jupyter Notebook file stored in `notebooks/report` that focuses on visualization and presentation.
    - The very beginning of the notebook contains a description of the purpose of the notebook.
       - This is helpful for your future self and anyone of your colleagues that needs to view your notebook. Without this context, you’re implicitly asking your peers to invest a lot of energy to help solve your problem. Help them by enabling them to jump into your project by providing them the purpose of this Jupyter Notebook.
    - Explanation of the data sources and where one can retrieve them
        - Whenever possible, link to the corresponding data dictionary
    - We encourage you to import custom functions and classes from Python modules and not create them directly in the notebook.  As soon as you have a working function in one of your exploratory notebooks, copy it over to `src` so it is reusable.
    - Much of the content in the report will be shared with the README.
8. An "Executive Summary" Keynote/PowerPoint/Google Slide presentation (delivered as a PDF export) that explains what you have found for the SRP. The presentation that accompanies that deck should be 4-5 minutes, so use your space wisely.
    - Make sure to also add and commit this file as presentation.pdf of your non-technical presentation to your repository with a file name of `reports/presentation.pdf`.
    - Contain between 5-10 professional quality slides detailing:
       - A high-level overview of your methodology
       - The results you’ve uncovered
       - Any real-world recommendations you would like to make based on your findings (ask yourself--why should the executive team care about what you found? How can your findings help the company/stakeholder?)
       - Avoid technical jargon and explain results in a clear, actionable way for non-technical audiences.
    - All visualizations included in this presentation should also be exported as image files (e.g. with `plt.savefig`, not by taking a screenshot) and saved under `reports/figures/`
9. Be sure to generate at least 3 high quality, well-labeled visualizations that support your conclusions. There should be a clear takeaway from each. These visualizations will reappear in the README, jupyter notebook report, and presentation deck.

## Citations

<sup>1</sup> Yohalem, N., Cooley, S. 2016. “Opportunity Youth in the Road Map Project Region”. Community Center for Education Results. Available at: https://bit.ly/2P2XRF3.

<sup>2</sup> Anderson, T., Braga, B., Derrick-Mills, T., Dodkowitz, A., Peters, E., Runes, C., and Winkler, M. 2019. “New Insights into the Back on Track Model’s Effects on Opportunity Youth Outcomes”. Urban Institute. Available at: https://bit.ly/2BuCLr1.

<sup>3</sup> Seattle Region Partnership. 2016. “King County Opportunity Youth Overview: Demographics of opportunity youth and systemic barriers to employment”. Available at: https://bit.ly/2oRGz37.

<sup>4</sup> Morton, N. 2019. “Nearly 19,000 youth in King County are neither working nor in school. How one Seattle nonprofit is changing that.” The Seattle Times. Available at: https://bit.ly/2W5EufR.

