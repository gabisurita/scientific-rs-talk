#![feature(specialization)]

use pyo3;
use pyo3::wrap_function;
use pyo3::prelude::*;
use numpy::PyArray1;


#[pyfunction]
fn sort(array: &PyArray1<i64>) -> Vec<usize> {
    let arr = array.as_array();
    let max = arr.iter().max().unwrap();

    let mut counts = vec![0; *max as usize + 1];

    for value in arr.iter() {
        counts[*value as usize] += 1;
    }

    counts.iter().enumerate().flat_map(|(value, count)|
        std::iter::repeat(value).take(*count as usize)
    ).collect()
}


#[pymodinit]
fn counting_sort(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_function!(sort)).unwrap();
    Ok(())
}
