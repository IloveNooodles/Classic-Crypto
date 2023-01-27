import styles from "@/styles/Root.module.scss";
import CipherList from "./(component)/cipher-list";

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
        <CipherList />
      </div>
    </main>
  );
}
