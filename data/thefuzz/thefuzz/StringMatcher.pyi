from typing import Optional, Tuple, List

OpcodeT = Tuple[str, int, int, int, int]
EditOpcodeT = Tuple[str, int, int]
MatchingBlocksT = List[Tuple[int, int, int]]


class StringMatcher:
    def _reset_cache(self) -> None:
        self._ratio: Optional[float] = None
        self._distance: Optional[int] = None
        self._opcodes: Optional[OpcodeT] = None
        self._editops: Optional[EditOpcodeT] = None
        self._matching_blocks: Optional[MatchingBlocksT] = None

    def __init__(self, isjunk: Optional[bool] = ..., seq1: str = ..., seq2: str = ...) -> None: ...
    def set_seqs(self, seq1: str, seq2: str) -> None: ...
    def set_seq1(self, seq1: str) -> None: ...
    def set_seq2(self, seq2: str) -> None: ...
    def get_opcodes(self) -> OpcodeT: ...
    def get_editops(self) -> EditOpcodeT: ...
    def get_matching_blocks(self) -> MatchingBlocksT: ...
    def ratio(self) -> float: ...
    def quick_ratio(self) -> float: ...
    def real_quick_ratio(self) -> float: ...
    def distance(self) -> int: ...