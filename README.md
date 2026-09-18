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

## Interactive Animations :clapper:

Smeexer includes a built-in step-by-step terminal animation engine (`animator.py`) to visually explain the exact inner mechanics of each mixing and sharding algorithm.

In the menu, select:
- `a`: Stepping-Stone step-by-step word swapping visual animation
- `b`: Odd-Even interleaved swapping visual animation
- `c`: Fivio segmentation and interleaving animation
- `d`: Onion Ring concentric layer swapping animation
- `a` (under Sharding Menu): Seed Sharding and chunk extraction visual animation

---

## Architectural Evaluation & Technology Modernization Guide :rocket:

### 1. Does Smeexer Need an Update?
**Yes.** The original 2021 codebase provided a solid algorithmic foundation, but needed modernization in several key areas:
- **Core Reliability & Input Validation**: Unhandled recursion in seed phrase input (`new_input`), incomplete menu flows, and crash vulnerabilities on unexpected input strings.
- **Completeness of Features**: Sharding methods (Staircase, Compass, Seesaw, Box) had placeholders or half-implemented stubs that are now fully implemented and tested.
- **Visual Explainability**: Seed phrase scrambling can feel abstract to users. Terminal-based step-by-step animations (`animator.py`) now bridge this gap by showing word-for-word transformations in real time.
- **Automated Testing Suite**: A unit test suite (`test_smeexer.py`) covers all validation, mixing, and sharding functions.

### 2. Technology Stack & Modernization Options

When modernizing Smeexer, security is the primary constraint because seed phrase operations **must be executed offline** on air-gapped or non-networked systems.

#### Option A: Enhanced Terminal User Interface (TUI) with Python `Textual` or `Rich` (Recommended for CLI)
- **Pros**:
  - Zero-dependency runtime option or self-contained executable.
  - Keeps 100% offline security guarantees without launching local web browsers or web sockets.
  - Beautiful keyboard-driven interactive screens, animations, and color-coded seed word tags.
- **Cons**: Requires Python 3.8+ runtime or bundled PyInstaller binary.

#### Option B: Standalone Single Page Application (SPA) with React / Vue / Svelte + Tailwind CSS
- **Pros**:
  - Fluid visual drag-and-drop animations (using Framer Motion or CSS Transitions) showing seed words moving, splitting into shards, or obscuring in real time.
  - Can be built into a single portable `.html` file (e.g. via Vite singlefile plugin) that runs directly in any browser **completely offline** without node or Python dependencies.
- **Cons**: Users must manually inspect HTML/JS source to trust that no network requests or telemetry exist.

### 3. Optimization Strategy

| Area | Current Improvements Implemented | Future Potential Optimizations |
| :--- | :--- | :--- |
| **Algorithm Safety** | Replaced recursive input with `while` loops; safe input normalization | Cryptographically secure pseudo-random generators (`secrets` module) for decoy BIP-0039 word selection |
| **Sharding** | Completed Staircase, Compass, Seesaw, and Box sharding algorithms | Implement Shamir's Secret Sharing Scheme (SLIP-0039 standard) for threshold-based recovery |
| **Reversibility** | Menu guided mixing explanations | Built-in unmix / decryption menu tool allowing users to enter a scrambled phrase + chosen algorithm to reconstruct original seed |
| **Testing** | 14 automated unit tests covering all functions (`python3 -m unittest discover`) | Property-based testing with `hypothesis` for edge-case BIP-0039 validation |

---

## How to use - Installation guide
### Simple method
1. Download the executable or repository along with `bip0039.txt`.
2. Run `python3 main.py` or the compiled binary and follow menu instructions.

### Advanced method (for experienced users only)
1. Download `main.py`, `menu.py`, `mixers.py`, `sharding.py`, `animator.py`, and `bip0039.txt`.
2. Run `python3 main.py`.
3. To run automated tests: `python3 -m unittest discover`.

---

## Roadmap :calendar:
- Date: 1st April, 2021
    - A new obfuscate method (Solved 04/02/2021)
    - Sharding: splitting the original seeds into smaller fractions and mix in random words
- Update: September 2024 / Modernization
    - Added step-by-step terminal visual animation engine (`animator.py`).
    - Fixed infinite recursion input bugs and non-integer menu crashes.
    - Completed full Sharding suite (Staircase, Compass, Seesaw, Box).
    - Created unit test suite (`test_smeexer.py`) with 100% pass rate.
    - Updated modern architectural and tech-stack evaluation roadmap.

---

## :bangbang: *Disclaimer* :bangbang: 
:heavy_exclamation_mark: **Please use Smeexer offline due to the risk of
your computer being compromised.**

:heavy_exclamation_mark: **No data is stored for this application, 
there will never be a feature to export the seeds.**

:heavy_exclamation_mark: **All the results of mixing will only be printed and not written
to any external files (.csv, .txt, or .pdf).**

:heavy_exclamation_mark: **Write all phrases down carefully**

---

:heavy_exclamation_mark: **PLEASE REMEMBER THE MIXING METHOD CHOSEN TO MIX YOUR SEED PHRASE
BECAUSE YOU CAN REVERSE THE PROCESS TO RECOVER THE ORIGINAL SEEDS AND SEED ORDER**
