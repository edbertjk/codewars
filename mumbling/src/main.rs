fn reverse_words(str: &str) -> String {
    // your code here
    let string = String::from(str).split_whitespace();
    let mut result: String = String::from("");
    string.next()
    // for i in (0..string.next()).rev(){
    //     let char_result: char = str.as_bytes()[i] as char;
    //     result += &char_result.to_string();
    // }
    // result
}
fn main() {
    println!("{}", reverse_words("apple"));
}
