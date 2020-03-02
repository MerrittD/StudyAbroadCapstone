import React, { Component } from 'react'

/* Dropdown filters */
class SearchBar extends Component {

    constructor() {
        super();
    }

    render() {
        let programs = this.props.state.programs;
        let optionItems = programs.map((program) =>
            <option key={program.name}>{program.country}</option>
        );
        return (
            <div>
                <select>
                    {optionItems}
                </select>
                <a href="/ResultPage"> Search</a>
            </div>
        )
    }
}

export default SearchBar;
