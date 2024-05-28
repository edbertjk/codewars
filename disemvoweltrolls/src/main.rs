fn test(s: &str) -> String{
    s.replace(&['a','i','u','e','o'], "")
}

fn main() {
    println!("{}",test("hello wa"));
}
