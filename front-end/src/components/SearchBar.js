import React, { Component } from 'react'

class SearchBar extends Component {
    render() {
        return (
            <div>
                <div class="dropdown">
                    <button class="dropbtn">Country</button>
                    <div class="dropdown-content">
                        <a href="#">Australia</a>
                        <a href="#">Chile</a>
                        <a href="#">Spain</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Language</button>
                    <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Area of Study</button>
                    <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Term</button>
                    <div class="dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
                <a href="/ResultPage"> Search</a>
            </div>
        )
    }
}

export default SearchBar;
