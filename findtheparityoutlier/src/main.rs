fn find_outlier(values: &[i32]) -> i32 {
    let mut result_odd: i32 = 0;
    let mut result_even: i32 = 0;
    let mut odd_count: u8 = 0;
    for res in values {
        if res % 2 == 0{
            odd_count += 1;
        }
    }
    if odd_count > 1{
        result_even
    }else{
        result_odd
    }
}
fn main() {
    println!("Hello, world!");
}
