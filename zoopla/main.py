import generic.permutations as permutations


def solution(input: int) -> int:
    perms = permutations.solution(input)
    out = -1
    for perm in perms:
        if int(perm) > input and (int(perm) < out or out == -1):
            out = int(perm)
    return out
