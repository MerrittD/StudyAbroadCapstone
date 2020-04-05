import React, { Component } from 'react'
import NavBar from '../components/NavBar'
import SearchBar from '../components/SearchBar'
import ResultHeader from '../components/ResultHeader'
import Result from '../components/Result'


export default function ResultPage() {
    return (
        <div>
            <ResultHeader />
            <Result />
        </div>
    )
}
