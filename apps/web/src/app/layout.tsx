import type { Metadata } from 'next';
import '../styles/globals.css';
import { Providers } from './providers';

export const metadata: Metadata = {
  title: 'LegalDesk AI — Enterprise AI Legal Operating System',
  description: 'Commercial enterprise platform for legal departments, law firms, corporate governance, and compliance teams.',
  keywords: ['Legal AI', 'Legal Operating System', 'Contract Intelligence', 'Corporate Governance', 'Legal Compliance'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-background text-foreground antialiased min-h-screen selection:bg-brand-500 selection:text-white">
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
