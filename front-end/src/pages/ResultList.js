import React, { Component } from 'react'
import ExampleComponent from '../components/ExampleComponent'
import SearchBar from '../components/SearchBar'
import ResultHeader from '../components/ResultHeader'
import Result from '../components/Result'


export default function ResultList() {
    return (
        <div>
            <ExampleComponent />
            <SearchBar />
            <ResultHeader />
            <Result />
        </div>
    )
}
