import { Inter } from "@next/font/google";
import Link from "next/link";
import styles from "./page.module.css";

const inter = Inter({ subsets: ["latin"] });
const listOfCipher: string[] = [
  "Vigenere Cipher",
  "Auto-key Vigenere Cipher",
  "Extended Vigenere Cipher",
  "Affine Cipher",
  "Playfair Cipher",
  "Hill Cipher",
  "Enigma cipher",
];

const description: string[] = [
  "Type of substitution cipher based on the vignere table",
  "Variation of vignere cipher, the key is appended by the plaintext itself",
  "Extended version of vignere cipher using 256 characters instead of 26",
  "Expanded version of caesar cipher, using simple linear function",
  "Substitution cipher based on 5x5 square with unique algorithm",
  "Substitution cipher based on linear algebra",
  "Substitution cipher that was used by Germany in World War 2",
];

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <code className={styles.title}>
          Classical Cipher <br />
          Encryptor, Decryptor, Solver
        </code>
      </div>
      <div className={styles.grid}>
        {listOfCipher.map((cipher: string, index: number) => {
          let slug = cipher.toLowerCase().replaceAll(" ", "-");
          return (
            <Link href={`/${slug}`} className={styles.card} key={index}>
              <h2 className={`${inter.className} ${styles.heading}`}>
                {cipher}
              </h2>
              <p className={`${inter.className} ${styles.hidden}`}>
                {description[index]}
              </p>
            </Link>
          );
        })}
      </div>
    </main>
  );
}
