import styles from "@/styles/Cipher.module.scss";
import { BASE_URL } from "@/utils/desc";
import { RootForm } from "@/utils/type";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { ChangeEvent, useRef, useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function ButtonGroup({ ...props }: RootForm) {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [isGroupped, setIsGroupped] = useState<boolean>(false);
  const [File, setFile] = useState<File | null>(null);
  const { cipherKey, text, url, result } = props;

  function formatNoSpace() {
    if (!result?.current?.value) return;
    if (!isGroupped) return;
    result.current.value = result.current.value.replaceAll(" ", "");
    setIsGroupped(false);
  }

  function formatGroupped() {
    if (!result?.current?.value) return;
    if (isGroupped) return;
    var formattedText = "";
    let len = result.current.value.length;
    let resText = result.current.value;
    for (let i = 0; i < len; i++) {
      if (i > 0 && i % 5 == 0 && resText[i] != " ") formattedText += " ";
      formattedText += resText[i];
    }
    result.current.value = formattedText;
    setIsGroupped(true);
  }

  async function handleSubmit(isEncrypt: boolean) {
    let body = new FormData();
    if (File) {
      body.append("file", File);
    }
    body.append("key", cipherKey?.text?.toUpperCase() || "");
    body.append("b", cipherKey?.b?.toUpperCase() || "");
    body.append("m", cipherKey?.m?.toUpperCase() || "");
    body.append("text", text?.current?.value.toUpperCase() || "");
    if (isEncrypt) {
      body.append("encrypt", "True");
    } else {
      body.append("encrypt", "False");
    }

    const data = await fetch(BASE_URL + url, {
      method: "POST",
      body: body,
    });
    try {
      const res = await data.json();
      console.log(res);
      if (res.type == "text") {
        if (result) result.current!.value = res.result;
        toast.success(res.message);
      } else if (res.type == "filename") {
        console.log(res.result);
        const download = document.getElementById("download_link");
        download?.setAttribute("href", `${BASE_URL}static/${res.result}`);
        download?.setAttribute("download", `result.enc`);
        download?.setAttribute("target", "_blank");
        toast.success(res.message);
      } else {
        toast.error(res.message);
      }
    } catch {
      toast.error("Unexpected error");
    }
  }

  return (
    <>
      <ToastContainer closeButton={false} theme="colored" />
      <div className={styles["btn-container"]}>
        {!File && (
          <div
            className={styles["file-upload"]}
            onClick={() => {
              if (!fileRef.current) return;
              fileRef.current.click();
            }}
          >
            <p>Upload File</p>
            <FontAwesomeIcon icon={faUpload} size="2x" />
            <input
              type="file"
              name="file"
              id="file"
              hidden
              ref={fileRef}
              onChange={(event: ChangeEvent<HTMLInputElement>) => {
                event.preventDefault();
                let file = event.target.files;
                if (!file) return;
                if (!infoRef.current) return;
                infoRef.current.textContent = file[0].name;
                setFile(file[0]);
              }}
            />
          </div>
        )}
        <div
          className={styles["file-upload"]}
          style={File ? { display: "block" } : { display: "none" }}
        >
          <p>File uploaded!</p>
          <p ref={infoRef}>File uploaded!</p>
        </div>
        <button
          type="reset"
          className={styles.btn}
          onClick={() => {
            setFile(null);
          }}
        >
          Clear
        </button>
        <button type="button" className={styles.btn}>
          <a id="download_link">Download result</a>
        </button>
        <button
          type="submit"
          className={styles.btn}
          onClick={(e) => {
            e.preventDefault();
            handleSubmit(true);
          }}
        >
          <ToastContainer />
          Encrypt plaintext
        </button>
        <button
          type="submit"
          className={styles.btn}
          onClick={(e) => {
            e.preventDefault();
            handleSubmit(false);
          }}
        >
          <ToastContainer />
          Decrypt ciphertext
        </button>
        <button type="button" className={styles.btn}>
          <a id="download_cipher">Save ciphertext as file</a>
        </button>
        <div className={styles.flex}>
          <button
            type="button"
            className={`${styles.btn} ${styles["btn-format"]}`}
            onClick={formatNoSpace}
          >
            No space
          </button>
          <button
            type="button"
            className={`${styles.btn} ${styles["btn-format"]}`}
            onClick={formatGroupped}
          >
            Grouped 5
          </button>
        </div>
      </div>
    </>
  );
}
