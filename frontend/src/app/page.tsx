import { Inter } from "@next/font/google";
import Link from "next/link";
import { description, listOfCipher } from "../utils/desc";
import styles from "./page.module.css";

const inter = Inter({ subsets: ["latin"] });

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
