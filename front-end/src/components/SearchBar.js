import React, { Component } from 'react'
import SearchResults from './SearchResults'
import { FormGroup, Label, Input, Button } from 'reactstrap'
import axios from 'axios'

/* Dropdown filters */
class SearchBar extends Component {
    /* Constructor to initialize props passed down */
    constructor(props) {
        super(props);
        this.state = {
            filters: {
                termFilter: 'Any',
                countryFilter: 'Any',
                areaOfStudyFilter: 'Any',
                languageFilter: 'Any'
            },
            filteredProgramList: [],
            displayResults: false
        }
    }

    /* Takes out all duplicates of the array passed in */
    getUnique(arr) {

        return arr.filter((e, i) => arr.indexOf(e) >= i)
    }


    /* Perform a get request with filters */
    onSearch = (displayRes) => {
        // const options = {
        //      if = any, pass 'None', otherwise the filter
        //     'loc': this.state.filters.countryFilter
        // }
        // figure out axios
        axios.get('https://my-json-server.typicode.com/MasonTDaniel/capstonedummydata/allPrograms')
            .then(response => {
                console.log('about to search, displayResults: ' + this.state.displayResults)
                this.setState({
                    filteredProgramList: response.data,
                    displayResults: displayRes
                });
                console.log('searched, displayResults: ' + this.state.displayResults)
            }, (error) => {
                console.log(error);
            });

    }


    render() {
        // Take in the passed down program array and store it for easy access
        let programs = this.props.state.programs;

        /* The following code blocks labeled 1, 2, 3, and 4 each create an array (4 total)
            These arrays hold all available program terms, countries, areas of study, and languages respectively, with no duplicates
            e.g. code block 1. will create an array such as [Spring, Summer, Fall] */


        /* 1. Fill an array with all possible terms (by mapping through every program) */
        let allProgramTerms = programs.map((program) =>
            program.term
        );
        // Remove all duplicate terms 
        allProgramTerms = this.getUnique(allProgramTerms)
        //  Sort the terms into alphabetical order 
        allProgramTerms.sort()
        // Add 'Any' option to the beginning of the array
        allProgramTerms.unshift('Any')
        //  Make it into an array of options so that we can insert them into our dropdown (below) 
        allProgramTerms = allProgramTerms.map((programTermValue, i) =>
            <option key={i}>{programTermValue}</option>
        );

        /* 2. Repeat for countries */
        let allProgramCountries = programs.map((program) =>
            program.country
        );
        allProgramCountries = this.getUnique(allProgramCountries)
        allProgramCountries.sort()
        allProgramCountries.unshift('Any')
        allProgramCountries = allProgramCountries.map((programCountryValue, i) =>
            <option key={i}>{programCountryValue}</option>
        );

        /* 3. Repeat for areas of study */
        let allProgramAreasOfStudy = programs.map((program) =>
            program.areaOfStudy
        );
        allProgramAreasOfStudy = this.getUnique(allProgramAreasOfStudy)
        allProgramAreasOfStudy.sort()
        allProgramAreasOfStudy.unshift('Any')
        allProgramAreasOfStudy = allProgramAreasOfStudy.map((programAreaOfStudyValue, i) =>
            <option key={i}>{programAreaOfStudyValue}</option>
        );

        /* 4. Repeat for languages */
        let allProgramLanguages = programs.map((program) =>
            program.language
        );
        allProgramLanguages = this.getUnique(allProgramLanguages)
        allProgramLanguages.sort()
        allProgramLanguages.unshift('Any')
        allProgramLanguages = allProgramLanguages.map((programLanguageValue, i) =>
            <option key={i}>{programLanguageValue}</option>
        );

        /* Display 4 dropdowns (populated with terms, countries, areas of study, and languages respectively) and a Search button */
        return (
            <div>
                <div style={{ "justifyContent": "space-evenly", "margin": "3rem" }} className="form-inline">
                    <div>
                        <FormGroup >
                            <Label style={{ "marginRight": "0.5rem" }} for="termFilter">Term</Label>
                            <Input type="select" value={this.state.filters.termFilter} onChange={(e) => {
                                let { filters } = this.state;
                                filters.termFilter = e.target.value;
                                this.setState({ filters });
                            }}>
                                {allProgramTerms}
                            </Input>
                        </FormGroup>
                    </div>
                    <div className="mr-20 ml-20">
                        <FormGroup>
                            <Label style={{ "marginRight": "0.5rem" }} for="countryFilter">Country</Label>
                            <Input type="select" id="countryFilter" value={this.state.filters.countryFilter} onChange={(e) => {
                                let { filters } = this.state;
                                filters.countryFilter = e.target.value;
                                this.setState({ filters });
                            }}>
                                {allProgramCountries}
                            </Input>
                        </FormGroup>
                    </div>
                    <div className="mr-20 ml-20">
                        <FormGroup >
                            <Label style={{ "marginRight": "0.5rem" }} for="areaOfStudyFilter">Area of Study</Label>
                            <Input type="select" id="areaOfStudyFilter" value={this.state.filters.areaOfStudyFilter} onChange={(e) => {
                                let { filters } = this.state;
                                filters.areaOfStudyFilter = e.target.value;
                                this.setState({ filters });
                            }}>
                                {allProgramAreasOfStudy}
                            </Input>
                        </FormGroup>
                    </div>
                    <div className="mr-20 ml-20">
                        <FormGroup >
                            <Label style={{ "marginRight": "0.5rem" }} for="languageFilter">Language</Label>
                            <Input type="select" id="languageFilter" value={this.state.filters.languageFilter} onChange={(e) => {
                                let { filters } = this.state;
                                filters.languageFilter = e.target.value;
                                this.setState({ filters });
                            }}>
                                {allProgramLanguages}
                            </Input>
                        </FormGroup>
                    </div >

                    <Button className="btn" style={{ "background": "#FFCD00", "border": "none", "color": "#000000", "marginLeft": "7px" }} onClick={this.onSearch.bind(this, true)}>Search
                    </Button>
                    {console.log('current filters: ' + this.state.filters)}
                </div>
                <div>
                    {this.state.displayResults && <SearchResults state={this.state} />}
                </div>
            </div>
        )
    }
}

export default SearchBar;
