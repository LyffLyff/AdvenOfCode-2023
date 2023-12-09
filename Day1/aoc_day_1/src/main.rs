use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};

// AOC - Day 1

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("input.txt")?;

    // Regular expression to match numbers in a line
    let re = Regex::new(r"\d+").unwrap();

    // Variables
    let mut sum = 0;
    let mut line_sum = 0;

    // Read the file line by line
    for line in io::BufReader::new(file).lines() {
        let line = line?;

        // Find all numbers in the line and print them
        let matches: Vec<_> = re.find_iter(&line).collect();

        for (index, number) in matches.iter().enumerate() {
            if index == 0 {
                println!("First number found in line: {}", number.as_str());

                if let Ok(int_num) = number.as_str().parse::<i32>() {
                    println!("Parsed number: {}", int_num);
                    line_sum = 10 * int_num;
                } else {
                    println!("Failed to parse the number");
                }
            }

            if index == matches.len() - 1 {
                println!("Last number found in line: {}", number.as_str());
                if let Ok(int_num) = number.as_str().parse::<i32>() {
                    println!("Parsed number: {}", int_num);
                    line_sum += int_num;
                } else {
                    println!("Failed to parse the number");
                }
            }
        }

        println!("{line_sum}");

        sum += line_sum;

        println!("ENDLINE--------------------------------------------");
    }

    println!("{sum}");

    Ok(())
}
