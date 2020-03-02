import React, { Component } from 'react'
import NavBar from '../components/NavBar'
import SearchBar from '../components/SearchBar'

class Browse {
    render() {
        return (
            <div>
                <NavBar />
                <SearchBar />
            </div>
        )
    }
}

export default Browse;