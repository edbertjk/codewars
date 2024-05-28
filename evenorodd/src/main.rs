pub fn even_or_odd(number: i32) -> &'static str {
    match number % 2 {
        0 => "Even",
        _ => "Odd",
    }
}
fn main() {
    println!("{}", even_or_odd(19));
}
