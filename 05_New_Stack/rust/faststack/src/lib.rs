use pyo3::prelude::*;
use rand::prelude::*;

#[pyfunction]
fn generar_unit_sales(dow: u8, is_holiday: bool) -> u32 {
    let mut base = thread_rng().gen_range(0..100);
    if dow == 5 || dow == 6 {
        base = ((base as f32) * 1.5) as u32;
    }
    if is_holiday {
        base = ((base as f32) * 1.3) as u32;
    }
    let noise: f32 = thread_rng().gen_range(0.5..1.5);
    let val = ((base as f32) * noise) as u32;
    val
}

#[pyfunction]
fn generar_batch(dows: Vec<u8>, holidays: Vec<bool>) -> Vec<u32> {
    let n = dows.len();
    let mut out = Vec::with_capacity(n);
    for i in 0..n {
        let mut base = thread_rng().gen_range(0..100);
        if dows[i] == 5 || dows[i] == 6 {
            base = ((base as f32) * 1.5) as u32;
        }
        if holidays.get(i).copied().unwrap_or(false) {
            base = ((base as f32) * 1.3) as u32;
        }
        let noise: f32 = thread_rng().gen_range(0.5..1.5);
        out.push(((base as f32) * noise) as u32);
    }
    out
}

#[pymodule]
fn faststack(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generar_unit_sales, m)?)?;
    m.add_function(wrap_pyfunction!(generar_batch, m)?)?;
    Ok(())
}
