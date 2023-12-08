use std::fs;
use std::io;
use reqwest;
use tokio;

const AOC_BASE_URL: &str = "https://adventofcode.com";

#[tokio::main]
pub async fn download_input() { 
    let session_cookie = get_session_cookie();

    let client = reqwest::Client::new();

    let response = client
    .get(format!("{AOC_BASE_URL}/2015/day/1/input"))
    .header("Cookie", format!("session={session_cookie}"))
    .send()
    .await
    .unwrap()
    .text()
    .await;

    println!("{:?}", response);

}

fn get_session_cookie() -> String {
    let fpath = "../../.session-cookie";

    let session_cookie = fs::read_to_string(fpath)
    .expect("Failed to read session cookie from");

    return session_cookie;
}