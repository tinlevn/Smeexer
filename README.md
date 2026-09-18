# Smeexer
Offline seed phrase security enhancements \
*Smeexer is a pun on Seed-mixer.*

>For testing purposes, visit [Mnemonic Code Converter](https://iancoleman.io/bip39/)
> to generate seed phrases.
***
## What is Smeexer? :thinking:

Smeexer is an offline Python/script program  
I created to scramble the ordering of the 
common 12-24-words-long mnemonic seed phrases
that many popular cryptocurrency wallets use to  
store their private keys.
The mechanics behind the process of generating 
private keys from the 12-24-words-long seed phrases
will not be covered here. 

However, they are discussed in-depth at these blog posts and web pages:
* [Journey from mnemonic phrase to Address](https://medium.com/mycrypto/the-journey-from-mnemonic-phrase-to-address-6c5e86e11e14)
* [What are Seed Phrases, Private Keys, Public Keys, Public Addresses?
](https://idoneus.io/support-hub/what-are-seed-phrases-private-keys-public-keys-public-addresses/) 
* [The Master Seed](https://ledger.readthedocs.io/en/latest/background/master_seed.html)
***
## Who is Smeexer for?

Smeexer is for anybody who wants (seeks) to increase
the security of the mnemonic phrases that are written offline,
on pieces of paper.\
Cold storage is the safest method of storing cryptocurrency.
However, there is always a chance of losing one's funds (or access to the funds)
if: 
- The owner forgets his or her seed phrases 
- The owner loses the physical template where he or she inscribed the phrases; 
- A thief (bad actor, criminal) somehow gains access to the copy of the physical seed phrases\
  (not through computer hacking nor network penetration).

**Notice**: *These scenarios are speaking strictly of\
the physical breach of the seeds, not a digital one.\
If your computer or smartphones which contain your\
cryptowallet(s) are compromised (hacked, penetrated, i,e. a keylogger),\
then mixing your seeds will not help to secure your funds.*
***
## Why use Smeexer?
Smeexer is created so that crypto holders can create more physical copies\
of their seed phrases because even if seeds are lost or stolen,\
whoever picking them up will have a near zero chance of recovering the\
original crypto wallet because he or she does not know:
- The original order of the phrases
- How many words are in the correct phrase (12? 16? 24?)
- The mixing method that the owner chose to mix his/her phrase

Hence, Smeexer allows its users to make more physical copies of\
their seed phrases and scatter them in different locations, essentially\
backing them up in the real world with added security without having\
to worry about them being destroyed, lost, or stolen.

---

## How it works :mag:
### The mixing methods and their names

    Stepping-stone
        Mix every adjacent word of the original phrase from start to end.
        Last step swaps first and last word.
        Here is an example demonstrating the process of Stepping-stone mixing
        a 12-word seed phrase. Each individual letter represents a valid word
        in the BIP-0039 vocabulary list.
> A B C D E F G H I J K L

>> B A D C F E H G J I K L (every adjacent letter is swapped)

>>> L A D C F E H G J I K B (last step swaps the first and last)
    
    Odd-Even
        Mix every odd and even word of the original phrase from start to end.
        Here is an example demonstrating the process of Odd-Even mixing
        a 12-word seed phrase. Each individual letter represents a valid word
        in the BIP-0039 vocabulary list. 
        This method works for both 12 word and 24 word seed phrases.
> A B C D E F G H I J K L

>> C D A B G H E F K L I J

> Explanation: 1st, 3rd; 5th, 7th; 9th, 11th letters are swapped.\
> 2nd, 4th; 6th, 8th; 10th, 12th letters are swapped.

    Obfuscate
        Simply add another dozen (1 seed phrase set) to input to 
        make it look like a regular 24-seed phrase instead of 12.
        The added set contains all BIP-0039 compliant words.
        All words are randomly generated and drawn from the .txt file.
        This method works for both 12 word and 24 word seed phrases.
>A B C D E F G H I J K L

>>A B C D E F G H I J K L M N O P Q R S T U V W X \
> ( If a bad actor picks up the piece of paper containing such a phrase,\
> The confusion will be: Is the original phrase 12-word long or 24?)
    
    Fivio
        This method only works with 12-seed phrase for now. First, it 
        obfuscates the orignal 12-word phrase. Then the mixing starts.
        There is a parameter for this method: left or right.
        Fivio mix essentially breaks the 2 sets of phrases into 3 segments:
        5 5 5 5 2 2 
            Left Fivio will scatter the true phrase as demonstrated below.
> **5** 5 **5** 5 **2** 2   
> The bold numbers represent the authentic segments of the original seed phrase.
            
            Right Fivio will move the ordering to the right:
> 5 **5** 5 **5** 2 **2**  
> In this case, the bold numbers (correct segments of seeds) are shifted to the right.

    Odd-One-Out
        This method also only works with 12-seed phrase for now. First, it 
        obfuscates the orignal 12-word phrase. Then the mixing starts.
        There is a parameter for this method: left or right; just like fivio mix.
        Odd-One-Out breaks the 2 sets of phrases into only 2 segments, 
        or 1 large list and 1 standalone word.
            Left Odd-One-Out will mix the true phrase as
> **11** 1 **1** 11\
> Explanation: The first 11 words and the 13th words combined will return the original list 
 
            Right Odd-One-Out will just move it to the right
> 11 **1** 1 **11**\
> Explanation: Add the 12th word from the list to the last 11 words to return the original list

---

## Technical Security Assessment & Viability Critique :warning:

### Security & Cryptographic Risks of Custom Seed Permutations
1. **Dramatically Reduced Entropy (Brute-Force Vulnerability)**:
   - A standard 12-word seed has $2048^{12} \approx 2^{132}$ possibilities.
   - If an attacker obtains a paper note with 12 words that they suspect are scrambled using a simple deterministic permutation algorithm (like Stepping-Stone, Odd-Even, or Onion Ring), there are only $12! = 479,001,600$ total possible orderings.
   - A GPU brute-force script testing BIP-39 checksums against public key derivations can test hundreds of millions of combinations per second. **An attacker with the scrambled 12-word list can recover the original wallet in seconds to minutes.**

2. **BIP-0039 Checksum Failure**:
   - BIP-39 seed phrases contain an integrated checksum in the final word bits. Scrambling the word order breaks the checksum 99.6% of the time. While this alerts the user that the phrase is modified, it also immediately signals to a knowledgeable attacker that the phrase has been intentionally permuted.

3. **Human Error Risk ("Locking Yourself Out")**:
   - The user must perfectly remember the exact algorithm (and parameters like `left`/`right` or `inner`/`outer`). If the user forgets the scheme or dies, recovery is extremely difficult or impossible for heirs.

### Standard Industry Alternatives
- **Shamir's Secret Sharing (SLIP-0039 / Shamir Backup)**: Mathematically proven $M$-of-$N$ threshold secret sharing built into modern hardware wallets (e.g. Trezor Model T).
- **Passphrase Extension (BIP-39 13th / 25th word)**: Uses a custom secret passphrase to derive a completely different wallet, storing the 24 words in one place and the passphrase in memory or separate location.
- **Multi-Signature Wallets (e.g., 2-of-3 Multisig)**: Requiring 2 independent private keys derived from separate seeds to authorize transactions.

---

## How to use - Installation guide
### Simple method
1. Download the repository along with `bip0039.txt`.
2. Run `python3 main.py` or the compiled binary and follow menu instructions.

---

## :bangbang: *Disclaimer* :bangbang: 
:heavy_exclamation_mark: **Please use Smeexer offline due to the risk of
your computer being compromised.**

:heavy_exclamation_mark: **No data is stored for this application, 
there will never be a feature to export the seeds.**

:heavy_exclamation_mark: **All the results of mixing will only be printed and not written
to any external files (.csv, .txt, or .pdf).**

:heavy_exclamation_mark: **Write all phrases down carefully**
