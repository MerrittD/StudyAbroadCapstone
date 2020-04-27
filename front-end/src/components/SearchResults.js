import React, { Component } from 'react'
import { Table } from 'reactstrap'

class SearchResults extends Component {

    render() {
        // Make a table of programs and store it
        let filteredPrograms = this.props.state.filteredProgramList.map((program) => {
            return (
                <tr key={program.id}>
                    <td>{program.country}</td>
                    <td>{program.term}</td>
                    <td>{program.name}</td>
                    <td>{program.areaOfStudy}</td>
                    <td>{program.language}</td>
                    <td>{program.cost}</td>
                    <td><a href={"https://" + program.website} target="_blank" rel="noopener noreferrer"></a>{program.website}</td>
                </tr >
            )

        });
        // Display No Results if no results
        if (Array.isArray(filteredPrograms) && filteredPrograms.length === 0) {
            return (
                <div>
                    <h5 style={{ "textAlign": "center" }}>No Results</h5>
                </div>
            )
        }
        // Display the results in a table
        return (
            <div className="result" >
                <Table>
                    <thead>
                        <tr>
                            <th>Country</th>
                            <th>Term</th>
                            <th>Name</th>
                            <th>Area of Study</th>
                            <th>Language</th>
                            <th>Cost</th>
                            <th>Website</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredPrograms}
                    </tbody>
                </Table>
            </div>
        )
    }
}

export default SearchResults;
