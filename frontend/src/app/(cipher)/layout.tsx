import "@/app/globals.css";
import Link from "next/link";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section>
      <head />
      <nav>
        <Link href="/">Back</Link>
      </nav>
      {children}
    </section>
  );
}
