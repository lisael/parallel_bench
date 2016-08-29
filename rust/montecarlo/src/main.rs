extern crate rand;
use std::thread;
use std::sync::mpsc;
use rand::distributions::{IndependentSample, Range};

fn main() {
   let loops = 100_000_000;
   let num = 4;
   let chunk = loops/num;

   let (input, out) = mpsc::channel();
   let (total_in,total_out) = mpsc::channel();

   thread::spawn( move || {
      let mut total = 0;
      for _ in 0..num{
         total = total + out.recv().unwrap();
      }
      total_in.send(total)
   });

   for _ in 0..num{
      let my_in = input.clone();
      thread::spawn( move || {
			let between = Range::new(-1f64, 1.);
			let mut rng = rand::weak_rng();

			let mut in_circle = 0;

			for _ in 0..chunk {
				 let a = between.ind_sample(&mut rng);
				 let b = between.ind_sample(&mut rng);
				 if a*a + b*b <= 1. {
					  in_circle += 1;
				 }
			}
         let _ = my_in.send(in_circle);
      });
   }

   let in_circle = total_out.recv().unwrap();
   println!("{}", 4. * (in_circle as f64) / (loops as f64));
}
