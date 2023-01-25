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
];
const slug: string[] = [
  "vignere-cipher",
  "auto-key-vignere-cipher",
  "extended-vignere-cipher",
  "affine-cipher",
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
          let slug = cipher.toLowerCase().replace(" ", "-");
          return (
            <Link href={`/${slug}`} className={styles.card} key={index}>
              <h2 className={inter.className}>{cipher}</h2>
              <p className={inter.className}>Cipher test</p>
            </Link>
          );
        })}
      </div>
    </main>
  );
}
